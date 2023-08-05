<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:date="http://xml.apache.org/xalan/java/java.util.Date"
    xmlns:java_lang="http://xml.apache.org/xalan/java/java.lang"
    exclude-result-prefixes="date java_lang">
    <xsl:output method="html" indent="yes" version="4.0"/>
    
    <xsl:param name="STR_BoostLogFile"><!--<xsl:message terminate="yes">Error! Please set STR_BoostLogPath param</xsl:message>--></xsl:param>
    
    <xsl:template match="/">
        <html>
            <head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html;charset=utf-8" /><title><xsl:value-of select="TestResult/TestSuite/@name" /> Tests Reports</title></head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js" type="text/javascript"></script>
            <script type="text/javascript">
                function show_alt(elt, event) {
                    var text = elt.attr("fake");
                    var nb_lines = (text.match(/\n/g) || []).length;

                    if (nb_lines > 0)
                    {
                        text = "&lt;div style='white-space:pre'&gt;" + text + "&lt;/div&gt;";
                        $("#alt_test").css("height", nb_lines * 22);
                    }
                    else
                    {
                        $("#alt_test").css("height", "auto");
                    }
                    $("#alt_test").html(text);
                    $("#alt_test").css("left", event.clientX - 10);
                    $("#alt_test").css("top", event.clientY - 10);
                    $("#alt_test").css("display", "block");
                    return false;
                }
                function hide_alt(elt, event) {
                    $("#alt_test").css("display", "none");
                    return false;
                }
                function swap_test(id) {
                    var obj = document.getElementById("div_" + id);
                    if (obj != null) {
                       if (obj.style.display == "none") $("#div_" + id).fadeIn();
                       else $("#div_" + id).fadeOut();
                    }
                    return false;
                }
                function swap_result(id) {
                    var obj = document.getElementById(id + "_detail");
                    if (obj != null) {
                       if (obj.style.display == "none") $('#' + id + "_detail").fadeIn();
                       else $('#' + id + "_detail").fadeOut();
                    }
                    return false;
                }
                function open_arbo(lvl1, lvl2, lvl3) {
                    var obj = document.getElementById("div_" + lvl1);
                    if (obj != null) $("#div_" + lvl1).fadeIn();
                    obj = document.getElementById("div_" + lvl1 + lvl2);
                    if (obj != null) $("#div_" + lvl1 + lvl2).fadeIn();
                    obj = document.getElementById(lvl1 + lvl2 + lvl3 + "_detail");
                    if (obj != null) $('#' + lvl1 + lvl2 + lvl3 + "_detail").fadeIn();
                    return false;
                }
            </script>
            <style type="text/css">
                .clear {clear:both; font-size:1px; line-height:1px; height:1px}
                body {position:relative}
                #alt_test {position:absolute; top:0; left:0; width:auto; height:20px; background-color:#333; color:#fff; padding:1px 2px 1px 2px; font-size:0.9em}

                span.passed_ok {color:green; font-weight:bold}
                span.passed_ko {color:red; font-weight:bold}
                span.skipped {color:orange; font-weight:bold}
                /* resume */
                div.content div.resume {border:2px solid #666; padding: 2px 10px 2px 10px}
                div.content div.resume ul li {clear:both}
                div.content div.resume ul ul li {margin:2px 0 2px 0; font-size:0.9em}
                div.content div.resume ul ul li div.title {margin: 0 10px 0 0}
                div.content div.resume div.info, div.content div.resume div.error, div.content div.resume div.skipped, div.content div.resume div.message {width: 30px; font-size:0.7em; margin: 0 2px 0 2px; padding: 2px 0 0 0}
                div.content div.resume div.info a, div.content div.resume div.error a, div.content div.resume div.skipped a, div.content div.resume div.message a {display:block; text-align:center; text-decoration:none; color:#fff; font-weight:bold; padding:1px 0 1px 0}
                div.content div.resume div.info a {background-color:green}
                div.content div.resume div.error a {background-color:red}
                div.content div.resume div.skipped a {background-color:orange}
                div.content div.resume div.message a {background-color:#999}
                /* detail */
                div.content div.detail a.link_title {text-decoration:none; color:#333}
                div.content div.detail a.link_title:hover {text-decoration:underline; color:#666}
                table.resume_test {border-collapse: collapse; border-spacing: 0; font-size:0.8em}
                table.resume_test tr th, table.resume_test tr td {border:1px solid #333; padding:1px 2px 1px 2px}
                ul.testsuite {border:1px dotted #999; list-style-type:none}
                ul.testsuite li {margin: 0 0 10px 0}
                ul.testcase {border:1px dotted #999; list-style-type:none}
                ul.testcase li {margin: 0 0 10px 0}
                div.testresult {padding: 2px 0 2px 0; font-size:0.8em;}
                div.content div.detail div.info, div.content div.detail div.error, div.content div.detail div.skipped, div.content div.detail div.message {width: 30px; font-size:0.9em; margin: 0 2px 0 2px; padding: 2px 0 0 0; float:left !important;}
                div.content div.detail div.info a, div.content div.detail div.error a, div.content div.detail div.skipped a, div.content div.detail div.message a {display:block; text-align:center; text-decoration:none; color:#fff; font-weight:bold; padding:1px 0 1px 0}
                div.content div.detail div.info a {background-color:green}
                div.content div.detail div.error a {background-color:red}
                div.content div.detail div.message a {background-color:#999}
                div.content div.detail div.resultdetail {float:left !important;  background-color:#eee; padding: 10px 10px 10px 10px}
                div.content div.detail div.resultdetail span.line {font-size:0.8em; color:#666}
            </style>
            <body>
                <h1><xsl:value-of select="TestResult/TestSuite/@name" /> Tests Reports</h1>
                <div class="content">
                    <xsl:for-each select="TestResult">
                        <div class="resume">
                            <h3>Abstract of tests <xsl:value-of select="TestSuite/@name"/></h3>
                            <xsl:for-each select="TestSuite">
                                PASSED : <span class="passed_ok"><xsl:value-of select="@test_cases_passed" /></span>
                                <xsl:if test="@test_cases_failed > 0"> / FAILED : <span class="passed_ko"><xsl:value-of select="@test_cases_failed" /></span></xsl:if> 
                                <xsl:if test="@test_cases_aborted > 0"> / ABORTED : <span class="passed_ko"><xsl:value-of select="@test_cases_aborted" /></span></xsl:if> 
                                <xsl:if test="@test_cases_skipped > 0"> / SKIPPED : <span class="skipped"><xsl:value-of select="@test_cases_skipped" /></span></xsl:if> 
                                <ul>
                                    <xsl:for-each select="TestSuite">
                                        <li><div style="float:left">TestSuite <xsl:value-of select="@name" /></div></li>
                                        <xsl:variable name="suitename" select="@name" />
                                        <ul>
                                            <xsl:for-each select="TestCase">
                                                <xsl:variable name="casename" select="@name" />

                                                <li>
                                                    <div style="float:left" class="title">TestCase <xsl:value-of select="@name" /></div>

                                                    <xsl:choose>
                                                        <xsl:when test="@result='skipped'">
                                                            <div class="skipped" style="float:left"><a href="#div_{$suitename}{$casename}" onclick="open_arbo('{$suitename}','{$casename}','0');" onmouseover="show_alt($(this), event);" onmouseout="hide_alt($(this), event);" fake="skipped">*0*</a></div>
                                                        </xsl:when>
                                                        <xsl:when test="@result='aborted'">
                                                            <xsl:variable name="testCaseContent" select="document($STR_BoostLogFile)/TestLog/TestSuite/TestSuite[@name=$suitename]/TestCase[@name=$casename]/Error"/>

                                                            <div class="error" style="float:left">
                                                            <a href="#{$suitename}{$casename}0" onclick="open_arbo('{$suitename}','{$casename}','0');" onmouseover="show_alt($(this), event);" onmouseout="hide_alt($(this), event);" fake="{$testCaseContent}">-0-</a></div>
                                                        </xsl:when>
                                                        <xsl:otherwise>
                                                            <xsl:for-each select="document($STR_BoostLogFile)/TestLog/TestSuite/TestSuite[@name=$suitename]/TestCase[@name=$casename]/*">
                                                                <xsl:variable name="iCountTestCase" select="position()" />

                                                                <xsl:if test="name()='Info'"><div class="info" style="float:left"><a href="#{$suitename}{$casename}{$iCountTestCase}" onclick="open_arbo('{$suitename}','{$casename}','{$iCountTestCase}');" onmouseover="show_alt($(this), event);" onmouseout="hide_alt($(this), event);" fake="{.}">+<xsl:value-of select="$iCountTestCase" />+</a></div></xsl:if>
                                                                <xsl:if test="name()='Error'"><div class="error" style="float:left"><a href="#{$suitename}{$casename}{$iCountTestCase}" onclick="open_arbo('{$suitename}','{$casename}','{$iCountTestCase}');" onmouseover="show_alt($(this), event);" onmouseout="hide_alt($(this), event);" fake="{.}">-<xsl:value-of select="$iCountTestCase" />-</a></div></xsl:if>
                                                                <xsl:if test="name()='Message'"><div class="message" style="float:left"><a href="#{$suitename}{$casename}{$iCountTestCase}" onclick="open_arbo('{$suitename}','{$casename}','{$iCountTestCase}');" onmouseover="show_alt($(this), event);" onmouseout="hide_alt($(this), event);" fake="{.}">.<xsl:value-of select="$iCountTestCase" />.</a></div></xsl:if>
                                                            </xsl:for-each>                                                            
                                                        </xsl:otherwise>
                                                    </xsl:choose>

                                                </li>
                                            </xsl:for-each>
                                        </ul>
                                    </xsl:for-each>
                                </ul>
                            </xsl:for-each>
                        </div>
                        <div class="detail">
                            <xsl:for-each select="TestSuite">
                                <h3>Detail of tests <xsl:value-of select="@name"/></h3>
                                <table class="resume_test">
                                    <tr><th colspan="2">Abstract of tests <xsl:value-of select="@name"/></th></tr>
                                    <tr><td>Result</td><td>
                                    <xsl:choose>
                                        <xsl:when test="@result='failed' or @result='aborted'"><span class="passed_ko"><xsl:value-of select="@result" /></span></xsl:when>
                                        <xsl:when test="@result='passed'"><span class="passed_ok"><xsl:value-of select="@result" /></span></xsl:when>
                                        <xsl:otherwise><span class="skipped"><xsl:value-of select="@result" /></span></xsl:otherwise>
                                    </xsl:choose>
                                    </td></tr>
                                    <tr><td>Assertions passed</td><td><xsl:if test="@assertions_passed='0'">0</xsl:if><xsl:if test="@assertions_passed!='0'"><span class="passed_ok"><xsl:value-of select="@assertions_passed" /></span></xsl:if></td></tr>
                                    <tr><td>Assertions failed</td><td><xsl:if test="@assertions_failed='0'">0</xsl:if><xsl:if test="@assertions_failed!='0'"><span class="passed_ko"><xsl:value-of select="@assertions_failed" /></span></xsl:if></td></tr>
                                    <tr><td>Expected failures</td><td><xsl:if test="@expected_failures='0'">0</xsl:if><xsl:if test="@expected_failures!='0'"><span class="passed_ko"><xsl:value-of select="@expected_failures" /></span></xsl:if></td></tr>
                                    <tr><td>Test cases passed</td><td><xsl:if test="@test_cases_passed='0'">0</xsl:if><xsl:if test="@test_cases_passed!='0'"><span class="passed_ok"><xsl:value-of select="@test_cases_passed" /></span></xsl:if></td></tr>
                                    <tr><td>Test cases failed</td><td><xsl:if test="@test_cases_failed='0'">0</xsl:if><xsl:if test="@test_cases_failed!='0'"><span class="passed_ko"><xsl:value-of select="@test_cases_failed" /></span></xsl:if></td></tr>
                                    <tr><td>Test cases skipped</td><td><xsl:if test="@test_cases_skipped='0'">0</xsl:if><xsl:if test="@test_cases_skipped!='0'"><span class="skipped"><xsl:value-of select="@test_cases_skipped" /></span></xsl:if></td></tr>
                                    <tr><td>Test cases aborted</td><td><xsl:if test="@test_cases_aborted='0'">0</xsl:if><xsl:if test="@test_cases_aborted!='0'"><span class="passed_ko"><xsl:value-of select="@test_cases_aborted" /></span></xsl:if></td></tr>
                                </table>
                                <xsl:for-each select="TestSuite">
                                    <xsl:variable name="suitename" select="@name" />
                                    <ul class="testsuite">
                                        <li>
                                            <h4><a class="link_title" href="javascript:;" onclick="return swap_test('{$suitename}');">TestSuite <xsl:value-of select="@name" /></a></h4>
                                            <div id="div_{$suitename}" style="display:none">
                                                <table class="resume_test">
                                                    <tr><th colspan="2">Abstract of test suite</th></tr>
                                                    <tr><td>Result</td><td><xsl:if test="@result='failed'"><span class="passed_ko"><xsl:value-of select="@result" /></span></xsl:if><xsl:if test="@result!='failed'"><span class="passed_ok"><xsl:value-of select="@result" /></span></xsl:if></td></tr>
                                                    <tr><td>Assertions passed</td><td><xsl:if test="@assertions_passed='0'">0</xsl:if><xsl:if test="@assertions_passed!='0'"><span class="passed_ok"><xsl:value-of select="@assertions_passed" /></span></xsl:if></td></tr>
                                                    <tr><td>Assertions failed</td><td><xsl:if test="@assertions_failed='0'">0</xsl:if><xsl:if test="@assertions_failed!='0'"><span class="passed_ko"><xsl:value-of select="@assertions_failed" /></span></xsl:if></td></tr>
                                                    <tr><td>Expected failures</td><td><xsl:if test="@expected_failures='0'">0</xsl:if><xsl:if test="@expected_failures!='0'"><span class="passed_ko"><xsl:value-of select="@expected_failures" /></span></xsl:if></td></tr>
                                                    <tr><td>Test cases passed</td><td><xsl:if test="@test_cases_passed='0'">0</xsl:if><xsl:if test="@test_cases_passed!='0'"><span class="passed_ok"><xsl:value-of select="@test_cases_passed" /></span></xsl:if></td></tr>
                                                    <tr><td>Test cases failed</td><td><xsl:if test="@test_cases_failed='0'">0</xsl:if><xsl:if test="@test_cases_failed!='0'"><span class="passed_ko"><xsl:value-of select="@test_cases_failed" /></span></xsl:if></td></tr>
                                                    <tr><td>Test cases skipped</td><td><xsl:if test="@test_cases_skipped='0'">0</xsl:if><xsl:if test="@test_cases_skipped!='0'"><span class="skipped"><xsl:value-of select="@test_cases_skipped" /></span></xsl:if></td></tr>
                                                    <tr><td>Test cases aborted</td><td><xsl:if test="@test_cases_aborted='0'">0</xsl:if><xsl:if test="@test_cases_aborted!='0'"><span class="passed_ko"><xsl:value-of select="@test_cases_aborted" /></span></xsl:if></td></tr>
                                                </table>
                                                <br />
                                        <xsl:for-each select="TestCase">
                                            <xsl:variable name="casename" select="@name" />

                                            <ul class="testcase">
                                                <li>
                                                    <h5><a class="link_title" href="javascript:;" onclick="return swap_test('{$suitename}{$casename}');">TestCase <xsl:value-of select="@name" /></a></h5>
                                                    <div id="div_{$suitename}{$casename}" style="display:none">
                                                        <table class="resume_test">
                                                            <tr><th colspan="2">Abstract of TestCase</th></tr>
                                                            <tr><td>Result</td><td>
                                                            <xsl:choose>
                                                                <xsl:when test="@result='failed' or @result='aborted'"><span class="passed_ko"><xsl:value-of select="@result" /></span></xsl:when>
                                                                <xsl:when test="@result='passed'"><span class="passed_ok"><xsl:value-of select="@result" /></span></xsl:when>
                                                                <xsl:otherwise><span class="skipped"><xsl:value-of select="@result" /></span></xsl:otherwise>
                                                            </xsl:choose>
                                                            </td></tr>
                                                            <tr><td>Assertions passed</td><td><xsl:if test="@assertions_passed='0'">0</xsl:if><xsl:if test="@assertions_passed!='0'"><span class="passed_ok"><xsl:value-of select="@assertions_passed" /></span></xsl:if></td></tr>
                                                            <tr><td>Assertions failed</td><td><xsl:if test="@assertions_failed='0'">0</xsl:if><xsl:if test="@assertions_failed!='0'"><span class="passed_ko"><xsl:value-of select="@assertions_failed" /></span></xsl:if></td></tr>
                                                            <tr><td>Expected failures</td><td><xsl:if test="@expected_failures='0'">0</xsl:if><xsl:if test="@expected_failures!='0'"><span class="passed_ko"><xsl:value-of select="@expected_failures" /></span></xsl:if></td></tr>
                                                            <tr><td>Temps d'éxécution</td><td><xsl:value-of select="document($STR_BoostLogFile)/TestLog/TestSuite/TestSuite[@name=$suitename]/TestCase[@name=$casename]/TestingTime" /></td></tr>
                                                        </table>

                                                        <xsl:if test="@result!='skipped'">
                                                            <xsl:variable name="testCaseResult" select="@result"/>

                                                            <xsl:for-each select="document($STR_BoostLogFile)/TestLog/TestSuite/TestSuite[@name=$suitename]/TestCase[@name=$casename]/*">
                                                                <xsl:variable name="iCountTestCase" select="position()" />
                                                                <xsl:if test="name()='Info'">
                                                                    <div class="testresult" id="{$suitename}{$casename}{$iCountTestCase}" style="clear:both">
                                                                        <div class="info"><a href="javascript:;" onclick="return swap_result('{$suitename}{$casename}{$iCountTestCase}');">+<xsl:value-of select="$iCountTestCase" />+</a></div>
                                                                        <div class="resultdetail" id="{$suitename}{$casename}{$iCountTestCase}_detail" style="display:none; clear:both">
                                                                            <b>Information :</b><br />
                                                                            <xsl:value-of select="." /><br />
                                                                            <span class="line">line <xsl:value-of select="@line" /> in <xsl:value-of select="@file" /></span>
                                                                        </div>
                                                                    </div>
                                                                </xsl:if>
                                                                <xsl:if test="name()='Error'">
                                                                    <xsl:choose>
                                                                        <xsl:when test="($testCaseResult)='aborted'">
                                                                            <div class="testresult" id="{$suitename}{$casename}0" style="clear:both">
                                                                                        <div class="error"><a href="javascript:;" onclick="return swap_result('{$suitename}{$casename}0');">-<xsl:value-of select="0" />-</a></div>
                                                                                        <div class="resultdetail" id="{$suitename}{$casename}0_detail" style="display:none; clear:both">
                                                                                            <b>Abortion :</b><br />
                                                                                            <div style="white-space:pre"><xsl:value-of select="." /></div>
                                                                                            <span class="line">line <xsl:value-of select="@line" /> in <xsl:value-of select="@file" /></span>
                                                                                        </div>
                                                                                    </div>
                                                                        </xsl:when>
                                                                        <xsl:otherwise>
                                                                            <div class="testresult" id="{$suitename}{$casename}{$iCountTestCase}" style="clear:both">
                                                                                <div class="error"><a href="javascript:;" onclick="return swap_result('{$suitename}{$casename}{$iCountTestCase}');">-<xsl:value-of select="$iCountTestCase" />-</a></div>
                                                                                <div class="resultdetail" id="{$suitename}{$casename}{$iCountTestCase}_detail" style="display:none; clear:both">
                                                                                    <b>Error :</b><br />
                                                                                    <div style="white-space:pre"><xsl:value-of select="." /></div>
                                                                                    <span class="line">line <xsl:value-of select="@line" /> in <xsl:value-of select="@file" /></span>
                                                                                </div>
                                                                            </div>
                                                                        </xsl:otherwise>
                                                                    </xsl:choose>
                                                                </xsl:if>
                                                                <xsl:if test="name()='Message'">
                                                                    <div class="testresult" id="{$suitename}{$casename}{$iCountTestCase}" style="clear:both">
                                                                        <div class="message"><a href="javascript:;" onclick="return swap_result('{$suitename}{$casename}{$iCountTestCase}');">.<xsl:value-of select="$iCountTestCase" />.</a></div>
                                                                        <div class="resultdetail" id="{$suitename}{$casename}{$iCountTestCase}_detail" style="display:none; clear:both">
                                                                            <b>Message :</b><br />
                                                                            <xsl:value-of select="." /><br />
                                                                            <span class="line">line <xsl:value-of select="@line" /> in <xsl:value-of select="@file" /></span>
                                                                        </div>
                                                                    </div>
                                                                </xsl:if>
                                                            </xsl:for-each>
                                                        </xsl:if>
                                                    </div>
                                                    <br class="clear" />
                                                </li>
                                            </ul>
                                        </xsl:for-each>
                                            </div>
                                        </li>

                                    </ul>
                                </xsl:for-each>
                            </xsl:for-each>
                        </div>
                    </xsl:for-each>
                </div>
                <div style="height:1000px"></div> <!-- pour que les ancres de la fin s'affiche en haut de la page -->
                <div id="alt_test" style="display:none"></div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
