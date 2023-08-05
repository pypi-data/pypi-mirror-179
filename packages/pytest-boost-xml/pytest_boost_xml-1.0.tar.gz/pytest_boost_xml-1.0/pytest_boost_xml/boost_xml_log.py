############################################################################
## 
## Copyright (C) 2025 Plaisic and/or its subsidiary(-ies).
## Contact: eti.laurent@gmail.com
## 
## This file is part of the Agglo project.
## 
## AGGLO_BEGIN_LICENSE
## Commercial License Usage
## Licensees holding valid commercial Agglo licenses may use this file in 
## accordance with the commercial license agreement provided with the 
## Software or, alternatively, in accordance with the terms contained in 
## a written agreement between you and Plaisic.  For licensing terms and 
## conditions contact eti.laurent@gmail.com.
## 
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
## 
## In addition, the following conditions apply: 
##     * Redistributions in binary form must reproduce the above copyright 
##       notice, this list of conditions and the following disclaimer in 
##       the documentation and/or other materials provided with the 
##       distribution.
##     * Neither the name of the Agglo project nor the names of its  
##       contributors may be used to endorse or promote products derived 
##       from this software without specific prior written permission.
## 
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR 
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED 
## TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
## PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
## LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
## NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
## SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
## 
## AGGLO_END_LICENSE
## 
############################################################################

from inspect import getframeinfo, stack
from itertools import count
from py.xml import Namespace as XmlNamespace, raw as xml_raw


__all__ = ["AttBoostXmlLog"]    
    
class AttBoostXmlLog(XmlNamespace):
    def __init__(self, report_title):
        self.__report_title = report_title
        self.__xml_test_suites = []
        self.__current_suite_path = ""
    

    @property
    def __current_test_case(self):
        return self.__xml_test_suites[-1][-1]
    

    def start_suite(self, path, name):
        self.__current_suite_path = path
        self.__xml_test_suites.append(AttBoostXmlLog.TestSuite(name=name))


    def add_test_case(self, name):
        # Create a new xml test case
        xml_test_case = AttBoostXmlLog.TestCase(name=name)

        self.__xml_test_suites[-1].append(xml_test_case)


    def close_test_case(self, report):
        # In case of tests case failure
        if report.failed:
            error = report.longrepr.reprcrash.message
            failed_assertion = ""
            message = ""
            explanation = ""

            # Compute failure reason
            try:
                failed_assertion, explanation = error.split("\n +  where ")
                explanation = explanation.replace(" +  ", "")

                # If there is a message in assertion
                if failed_assertion.startswith("AssertionError"):
                    message, failed_assertion = failed_assertion.replace("AssertionError: ", "").split("\n")
            # Case where error was not caused by an assert
            except ValueError:
                explanation = error

            self.__append_assertion_result(report.longrepr.reprcrash.lineno, (failed_assertion, message, explanation), False)

        # Append test case execution time
        self.__current_test_case.append(AttBoostXmlLog.TestingTime(f"{round(getattr(report, 'duration', 0), 6):6f}"))


    def add_passed_assertion(self, line, assertion):
        self.__append_assertion_result(line, assertion, True)


    def add_report_info(self, message):
        caller = None
        formated_data = xml_raw(f"<![CDATA[{message}]]>")
        line = "unknown"

        try:
            stack_ = stack()

            # Look for test item in call stack. Start from 3 levels above this function
            for stack_idx in count(3):
                # If current stack level is the current test suite
                if stack_[stack_idx].filename == self.__current_suite_path.as_posix():
                    line = stack_[stack_idx].lineno
                    break
        # Case where assertion was not found in call stack
        except IndexError:
            pass
        finally:
            del stack_

        self.__current_test_case.append(AttBoostXmlLog.Message(formated_data, file=self.__current_suite_path, line=line))


    def write(self, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            xml_root = AttBoostXmlLog.TestSuite(self.__xml_test_suites, name=self.__report_title)

            file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
            file.write(AttBoostXmlLog.TestLog(xml_root).unicode())

 
    def __append_assertion_result(self, line, assertion, result):
        formated_data = ""
        result_tag = None
        
        # Compute data
        if result:
            formated_data = xml_raw(f"<![CDATA[check {assertion} passed]]>")
            result_tag = AttBoostXmlLog.Info
        else:
            assertion, message, explanation = assertion

            # If test case failed on assert
            if assertion:
                formated_data = f"check {assertion} failed"
                if message:
                    formated_data += f"\n{message}"
                if explanation:
                    formated_data += f"\nwhere:\n{explanation}"
            # If test case failed on exception
            else:
                formated_data += explanation
            formated_data = xml_raw(f"<![CDATA[{formated_data}]]>")
            result_tag = AttBoostXmlLog.Error

        # Append xml tag
        self.__current_test_case.append(result_tag(formated_data, file=self.__current_suite_path, line=line))
