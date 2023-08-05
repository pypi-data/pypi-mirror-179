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


# Global variables
# equivalent $(dirname $0)
sThisShellPath=${0%/*}

source "$sThisShellPath/../../../development/AggloToolKit/shell/src/utils/atkFileSystem.sh"

# Check the parameters
ParamOK=true
if [ $# != 2 ] && [ $# != 3 ];
then
    echo "Commmand syntax : autReportUnitTest asReportPath asReportName [Verbose]"
    echo "example : ../../autRunUnitTest.sh ../src/test/STR_TU testUTReport [Verbose]"
    ParamOK=false
fi


if $ParamOK ;
then
    # Init parameters
    asReportPath=$1
    asReportName=$2
    sHtmlReportPath=$asReportPath/$asReportName".html"
    sBoostReportPath_Summary=$asReportPath/$asReportName"_Summary.xml"
    sBoostReportPath_Log=$asReportPath/$asReportName"_Log.xml"
   
    # Generate the html report
    $sThisShellPath/generateReport.sh $asReportPath $asReportName "Html"

    if [ $# = 3 ] && [ $3 = "Verbose" ];
    then
        $sThisShellPath/generateReport.sh $asReportPath $asReportName "StdOut"
    fi

    # List the generated files
    sHtmlReportPath=$(getPathAbsolute "$sHtmlReportPath")
    sBoostReportPath_Summary=$(getPathAbsolute "$sBoostReportPath_Summary")
    sBoostReportPath_Log=$(getPathAbsolute "$sBoostReportPath_Log")
    echo
    echo "****************************************************************"
    echo "************************ GENERATED FILES ***********************"
    echo "****************************************************************"
    echo "** Complete report (.html) : $sHtmlReportPath"
    echo "** Boost result (.xml)     : $sBoostReportPath_Summary"
    echo "** Boost log (.xml)        : $sBoostReportPath_Log"
    echo "****************************************************************"
    
fi

