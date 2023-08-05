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
#TempDir=/tmp
TempDir=.

# getShellPath
#~ function getShellPath()
#~ {
	#~ ShellPath=${0%/*}
#~ 
    #~ return $ShellPath
#~ }


function exists()
{
    if [ -e "$1" ]; then
        echo "true"
    else
        echo "false"
    fi
}


function isDirectory()
{
    if [ -d "$1" ]; then
        echo "true"
    else
        echo "false"
    fi
}


function isFile()
{
    if [ -f "$1" ]; then
        echo "true"
    else
        echo "false"
    fi
}


function getPath()
{
    Path="$1"
    
    # TODO factoriser
    if [ "$(exists $Path)" == "true" ]; then
        bIsFile=$(isFile $Path)

        if [ "$bIsFile" == "true" ]; then
            sNewPath="${Path%/*}"
            if [ "$sNewPath" == "$Path" ]; then
                Path="."
            else
                Path="$sNewPath"
            fi
        else
            cLastChar=${Path:(-1)}
            if [ "$cLastChar" == "/" ]; then
                Path="${Path%/*}"
            fi
        fi
    else
        sNewPath="${Path%/*}"
        if [ "$sNewPath" == "$Path" ]; then
            Path="."
        else
            Path="$sNewPath"
        fi
    fi
    
    echo "$Path"
}



# TODO c'est bizarre cette methode ne fonctionne pas
# function getPath()
# {
    # asPath=$1
    # sRes=""
    
    # if [ "$(exists $asPath)" == "true" ]; then
        # bIsFile=$(isFile $asPath)

        # # If given artefact is an existing file
        # if [ "$bIsFile" == "true" ]; then
            # # Retrieve path
            # sRes="${asPath%/*}"
            
            # # No '/' was found in given path : given artefact was only a file name
            # if [ "$sRes" == "$asPath" ]; then
                # sRes="."
            # fi
        # # If given artefact is an existing directory
        # else
            # # Remove final '/' if needed
            # cLastChar=${asPath:(-1)}
            # if [ "$cLastChar" == "/" ]; then
                # sRes="${asPath%/*}"
            # fi
        # fi
    # else
        # # Given artefact doesn't exist, there is no way to know if it's a file or a directory
        # # Retrieve path
        # sRes="${asPath%/*}"
            
        # # No '/' was found in given path : given artefact was only a file name
        # if [ "$sRes" == "$asPath" ]; then
            # asPath="."
        # fi
    # fi
    
    # echo "$sRes"
# }

function getPathRelative()
{
    PathIn=$1
    
    getPathFromTo "." "$PathIn"
}


function getPathAbsolute()
{
    PathIn=$1
    bExists=$(exists $PathIn)
    
    # TODO gerer le cas d'un repertoir inexistant
    if [ "$bExists" == "true" ]; then
        Path=$(getPath $PathIn)
        bIsFile=$(isFile $PathIn)
        
        # We could use readlink -m "$PathIn", however this solution is more portable
        SaveCurrentDir=$(pwd)
        cd "$Path"
        AbsolutePath=$(pwd)
        cd "$SaveCurrentDir"
        
        if [ $bIsFile == "true" ]; then
            AbsolutePath=$AbsolutePath"/"$(getFileName $PathIn)
        fi
        echo $AbsolutePath
    fi
}


# TODO obtenir soir le path, soit le path + filename
# TODO faire fonctionner egalement quand le path n'existe pas
function getPathFromTo()
{
    PathSource=$(getPathAbsolute "$1")/
    PathFileDest=$(getPathAbsolute "$2")/
    abPathOnly="false"
	PathFromTo="" # for now

    if [ $# == 3 ]; then
        abPathOnly=$3
    fi

    # Ensure PathSource is a directory path, not a file path
    if [ "$(isFile $PathSource)" == "true" ]; then
        PathSource=$(getPath "$PathSource")
    fi
	CommonParent=$PathSource

    while [[ "${PathFileDest#$CommonParent}" == "${PathFileDest}" ]]; do
        # no match, means that candidate common part is not correct
        # go up one level (reduce common part)
        #TODO supprimer dirname
        CommonParent=$(dirname "$CommonParent")

        # and record that we went back, with correct / handling
        if [[ -z $PathFromTo ]]; then
            PathFromTo=".."
        else
            PathFromTo="../$PathFromTo"
        fi
    done

    if [[ $CommonParent == "/" ]]; then
        # special case for root (no common path)
        PathFromTo="$PathFromTo/"
    fi

    # since we now have identified the common part, compute the non-common part
    ForwardPart="${PathFileDest#$CommonParent}"

    # Aggregate forward and backward parts
    if [[ -n $PathFromTo ]] && [[ -n $ForwardPart ]]; then
        PathFromTo="$PathFromTo$ForwardPart"
    elif [[ -n $ForwardPart ]]; then
        # Extra forward slash removal
        # PathFromTo="${ForwardPart:1}"
        # Extra backward slash removal
        PathFromTo="${ForwardPart%/*}"
    fi

	cLastChar=${PathFromTo:(-1)}
	if [ "$cLastChar" == "/" ]; then
		PathFromTo="${PathFromTo%/*}"
	fi
	
	if [ "$PathFromTo" == "" ]; then
		PathFromTo="."
	fi
	
    if [ "$abPathOnly" == "true" ]; then
        PathFromTo=$(getPath $PathFromTo)
    fi

    echo "$PathFromTo"
}


function getLastItem()
{
    asPath="$1"
    
    sItemName="${asPath##*/}"
    echo "$sItemName"
}


function getFileName()
{
    PathFileIn="$1"
    bIsFile=$(isFile $PathFileIn)
    
    if [ $bIsFile == "true" ]; then
        FileName="${PathFileIn##*/}"
        echo "$FileName"
    fi
}


function getFileNameNoExtension()
{
    PathFileIn=$1
    bIsFile=$(isFile $PathFileIn)
    
    if [ $bIsFile == "true" ]; then
        FileName=$(getFileName "$PathFileIn")
        FileNameNoExt=${FileName%.*}
        
        echo "$FileNameNoExt"
    fi
}


function getFileExtension()
{
    PathFileIn=$1
    bIsFile=$(isFile $PathFileIn)
    
    if [ $bIsFile == "true" ]; then
        sExtension="${PathFileIn##*.}"
        
        echo "$sExtension"
    fi
}


# function isUnix()
# {
    # # return 0 (true) if first line ends in CR
    # isDosFile() {
        # [[ $(head -1 "$1") == *$'\r' ]]  
# }
    # if [ -d "$1" ]; then
        # echo "true"
    # else
        # echo "false"
    # fi
# }


# function isWindows()
# {
    # if [ -f "$1" ]; then
        # echo "true"
    # else
        # echo "false"
    # fi
# }

# TODO
function removeFile()
{
    asParentDir=$1
    asPattern=$1
    abRecursive=$1
}


# TODO
function removeDir()
{
    asParentDir=$1
    asPattern=$1
    abRecursive=$1
}


