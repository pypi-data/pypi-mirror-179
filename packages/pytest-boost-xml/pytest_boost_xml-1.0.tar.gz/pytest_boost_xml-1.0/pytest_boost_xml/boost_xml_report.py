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

from py.xml import Namespace as XmlNamespace

    
__all__ = ["AttBoostXmlReport"]

class _TestResult:
    def __init__(self, total, current):
        self.total = total
        self.current = current


class AttBoostXmlReport(XmlNamespace):
    def __init__(self, report_title):
        self.__report_title = report_title
        self.__xml_test_suites = []
        self.__results = {"assertions_passed":_TestResult(0,0), 
                          "assertions_failed":_TestResult(0,0), 
                          "test_cases_passed":_TestResult(0,0), 
                          "test_cases_skipped":_TestResult(0,0), 
                          "test_cases_failed":_TestResult(0,0), 
                          "test_cases_aborted":_TestResult(0,0)}
        self.__nb_passed_assertions = 0


    @property
    def __current_test_suite(self):
        result = None

        try:
            result = self.__xml_test_suites[-1]
        except IndexError:
            pass

        return result


    def start_suite(self, name):
        # Update status of the previous test suite
        self.__close_current_test_suite()
           
        # Instanciate a new test suite
        self.__xml_test_suites.append(AttBoostXmlReport.TestSuite(name=name, result="passed", assertions_passed=0, assertions_failed=0, expected_failures=0, 
                                                                  test_cases_passed=0, test_cases_failed=0, test_cases_skipped=0, test_cases_aborted=0))


    def add_test_case(self, name):
        self.__current_test_case = name


    def close_test_case(self, report):
        nb_assertions_failed = 0
        test_case_result = ""

        if report.when == "setup":
            test_case_result = "aborted" if report.failed else "skipped"
        else:
            test_case_result = "failed" if report.failed else "passed"
            nb_assertions_failed = int(bool(report.failed))

        # Create a new xml test case in current test suite
        self.__current_test_suite.append(AttBoostXmlReport.TestCase(name=self.__current_test_case, result=test_case_result, 
                                                                    assertions_passed=self.__nb_passed_assertions, 
                                                                    assertions_failed=nb_assertions_failed, expected_failures=0))

        # Compute number of failures for current suite
        if report.passed:
            self.__results["test_cases_passed"].current += 1
        elif report.failed:
            if report.when == "call":
                self.__results["test_cases_failed"].current += 1
            else:
                self.__results["test_cases_aborted"].current += 1
        elif report.skipped:
                self.__results["test_cases_skipped"].current += 1
        self.__results["assertions_passed"].current += self.__nb_passed_assertions
        self.__results["assertions_failed"].current += nb_assertions_failed
        self.__nb_passed_assertions = 0


    def add_passed_assertion(self):
        self.__nb_passed_assertions += 1


    def write(self, file_path):
        # Close the last test suite
        self.__close_current_test_suite()

        with open(file_path, "w", encoding="utf-8") as file:
            global_result = "failed" if (self.__results["test_cases_failed"].total or self.__results["test_cases_aborted"].total) else \
                            "passed" if self.__results["test_cases_passed"].total else "skipped"
            xml_root = AttBoostXmlReport.TestSuite(self.__xml_test_suites, name=self.__report_title, result=global_result,
                                                   assertions_passed=self.__results["assertions_passed"].total, 
                                                   assertions_failed=self.__results["assertions_failed"].total, 
                                                   expected_failures=0, test_cases_passed=self.__results["test_cases_passed"].total, 
                                                   test_cases_failed=self.__results["test_cases_failed"].total, 
                                                   test_cases_skipped=self.__results["test_cases_skipped"].total, 
                                                   test_cases_aborted=self.__results["test_cases_aborted"].total)

            file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
            file.write(AttBoostXmlReport.TestResult(xml_root).unicode())

        
    def __close_current_test_suite(self):
        if self.__current_test_suite:
            test_suite_result = "failed" if self.__results["test_cases_failed"].current else "passed"
            
            self.__current_test_suite.attr.result = test_suite_result

            for counter_type, counter in self.__results.items():
                # Update test suite
                setattr(self.__current_test_suite.attr, counter_type, counter.current)

                # Reset test suite counter
                counter.total += counter.current
                counter.current = 0
