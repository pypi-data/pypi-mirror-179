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

from subprocess import CalledProcessError
from pathlib import Path
from pkg_resources import resource_filename as extract_file
from pytest import fixture
from agglo_tk.utils import AtkCommandRunner, SILENT
from .boost_xml_log import AttBoostXmlLog
from .boost_xml_report import AttBoostXmlReport

    
__all__ = ["AttBoostXmlPlugin"]    

class AttBoostXmlPlugin:
    """
    Listens to pytest hooks to generate boost xml reports for unit tests.
    """

    def __init__(self, report_path, report_filename, report_title):
        self.__report_path = report_path
        self.__report_filename = report_filename
        self.__summary_file_path = Path(f"{report_path}/{report_filename}_Summary.xml")
        self.__log_file_path = Path(f"{report_path}/{report_filename}_Log.xml")
        self.__html_file_path = Path(f"{report_path}/{report_filename}.html")
        self.__boost_xml_log = AttBoostXmlLog(report_title)
        self.__boost_xml_report = AttBoostXmlReport(report_title)
        self.__current_suite_name = ""
        self.__current_item = None


    def pytest_runtest_call(self, item):
        self.__append_test_case(item)

        
    def pytest_assertion_pass(self, item, lineno, orig, expl):
        self.__boost_xml_log.add_passed_assertion(lineno, orig)
        self.__boost_xml_report.add_passed_assertion()


    def pytest_runtest_makereport(self, item, call):
        self.__current_item = item


    def pytest_runtest_logreport(self, report):
        # If test case was skipped test or failed during setup
        if report.skipped or (report.failed and ("setup" == report.when)):
            # Append a test case and close it at the same time
            self.__append_test_case(self.__current_item, report)

        # If test case was executed
        elif "call" == report.when:
            # Close test case
            self.__boost_xml_log.close_test_case(report)
            self.__boost_xml_report.close_test_case(report)

        
    def pytest_sessionfinish(self):
        generate_html_path = extract_file("pytest_boost_xml", "xsl/generateReport.sh")

        # Ensure report path exist
        Path(self.__report_path).mkdir(parents=True, exist_ok=True)

        # Generate boost xml report and boost xml traces files
        extract_file("pytest_boost_xml", "xsl/atkFileSystem.sh")
        extract_file("pytest_boost_xml", "xsl/convertBoostXmlToHtml.xsl")
        self.__boost_xml_log.write(self.__log_file_path)
        self.__boost_xml_report.write(self.__summary_file_path)
        try:
            AtkCommandRunner().execute(f"{generate_html_path} {self.__report_path} {self.__report_filename} Html")
        except CalledProcessError:
            self.__html_file_path = "html generation failed, maybe xslt is not installed"

        self.__current_item = None
        self.__current_suite_name = ""

        
    def pytest_terminal_summary(self, terminalreporter):
        terminalreporter.write_sep("-", f"generated xml summary file: {self.__summary_file_path}")
        terminalreporter.write_sep("-", f"generated xml log file: {self.__log_file_path}")
        terminalreporter.write_sep("-", f"generated html report file: {self.__html_file_path}")


    def add_report_info(self, message):
        self.__boost_xml_log.add_report_info(message)

    
    def __append_test_case(self, item, report=None):
        node_id_names = item.nodeid.split("::")
        # sFileName = ""
        suite_name = ""
        test_case_name = ""
        is_new_test_suite = False

        # Compute test suite and test cases' names
        # TODO mieux choper les noms, numeros de ligne...
        node_id_names = [x.replace(".py", "") for x in node_id_names if x != '()']
        suite_name = node_id_names[0].split("/")[-1]
        test_case_name = node_id_names[-1]
        is_new_test_suite = (not self.__current_suite_name) or (suite_name != self.__current_suite_name)

        # If test case belongs to a new test suite
        if is_new_test_suite:
            self.__current_suite_name = suite_name

            # Instanciate a new test suite
            self.__boost_xml_log.start_suite(item.path, suite_name)
            self.__boost_xml_report.start_suite(suite_name)
        
        # Append test case to the current test suite
        self.__boost_xml_log.add_test_case(test_case_name)
        self.__boost_xml_report.add_test_case(test_case_name)

        # If test case already has a report (case of skip or abortion)
        if report:
            # Close test case
            self.__boost_xml_log.close_test_case(report)
            self.__boost_xml_report.close_test_case(report)

        