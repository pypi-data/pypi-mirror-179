#!/bin/bash

# Global variables
# equivalent $(dirname $0)
sThisShellPath=${0%/*}
source "$sThisShellPath/atkFileSystem.sh"

# Check the parameters
ParamOK=true
if [ $# != 3 ];
then
    echo "Commmand syntax : sThisShellPath ReportPath ReportName {Html|Text|StdOut}"
    echo "example : ../../output/reportUnitTest.sh ../src/test/STR_TU ReportFile Html"
    ParamOK=false
fi


if $ParamOK ;
then
    # Init parameters
    ReportPath=$1
    ReportName=$2
    asMode=$3
    BoostReportFile_Log=$ReportPath/$ReportName"_Log.xml"
    BoostReportFile_Summary=$ReportPath/$ReportName"_Summary.xml"
    BoostReportFile=$ReportPath/$ReportName
    sConvertBoostXslFile=""
    sConvertBoostOption=""
   
    BoostLogFileRelative=$(getPathFromTo "$sThisShellPath" "$BoostReportFile_Log")
    sConvertBoostOption=" --stringparam STR_BoostLogFile $BoostLogFileRelative"
    if [ $asMode = "Html" ];
    then
        BoostReportFile=$BoostReportFile".html"
        sConvertBoostXslFile="$sThisShellPath/convertBoostXmlToHtml.xsl"
    elif [ $asMode = "Text" ] || [ $asMode = "StdOut" ];
    then
        BoostReportFile=$BoostReportFile".txt"
        sConvertBoostXslFile="$sThisShellPath/convertBoostXmlToTxt.xsl"
        # TODO ajout du file name a la fin du path relatif:workaround car getPathFromTo ne marche pas bien en particulier pour aller vers un fichier
        BoostSummaryFileRelative=$(getPathFromTo "$sThisShellPath" "$BoostReportFile_Summary")"/"$(getFileName "$BoostReportFile_Summary")
        sConvertBoostOption=$sConvertBoostOption" --stringparam STR_BoostSummaryFile $BoostSummaryFileRelative"
    fi

    # Generate the report
    if [ $asMode = "StdOut" ];
    then
        # TODO gerer la coloration
        xsltproc $sConvertBoostOption $sConvertBoostXslFile $BoostReportFile_Summary
    else
        xsltproc $sConvertBoostOption $sConvertBoostXslFile $BoostReportFile_Summary > $BoostReportFile
    fi
    
fi
