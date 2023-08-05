<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:date="http://xml.apache.org/xalan/java/java.util.Date"
    xmlns:java_lang="http://xml.apache.org/xalan/java/java.lang"
    exclude-result-prefixes="date java_lang">

    <xsl:output method="text"/>
    
    <xsl:param name="STR_BoostLogFile"><!--<xsl:message terminate="yes">Error! Please set STR_BoostLogPath param</xsl:message>--></xsl:param>
    <xsl:param name="STR_BoostSummaryFile"><!--<xsl:message terminate="yes">Error! Please set STR_BoostSummaryFile param</xsl:message>--></xsl:param>
    
    <xsl:template match="/">
        <xsl:for-each select="TestResult">
            <xsl:for-each select="TestSuite">
                <xsl:text>&#xA;****************************************************************&#xA;</xsl:text>
                <xsl:text>*************** START UNIT TEST </xsl:text><xsl:value-of select="@name" /><xsl:text> ***************&#xA;</xsl:text>
                <xsl:text>****************************************************************&#xA;</xsl:text>
                <xsl:text>&#x09;----------------------------&#xA;</xsl:text>
                <xsl:text>&#x09;| RESUME OF UNIT TEST&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Result : </xsl:text><xsl:value-of select="@result" /><xsl:text>&#x09;&#x09;&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Assertions passed : </xsl:text><xsl:value-of select="@assertions_passed" /><xsl:text>&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Assertions failed : </xsl:text><xsl:value-of select="@assertions_failed" /><xsl:text>&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Expected failures : </xsl:text><xsl:value-of select="@expected_failures" /><xsl:text>&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Test cases passed : </xsl:text><xsl:value-of select="@test_cases_passed" /><xsl:text>&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Test cases failed : </xsl:text><xsl:value-of select="@test_cases_failed" /><xsl:text>&#x09;&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Test cases skipped : </xsl:text><xsl:value-of select="@test_cases_skipped" /><xsl:text>&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;| Test cases aborted : </xsl:text><xsl:value-of select="@test_cases_aborted" /><xsl:text>&#x09;|&#xA;</xsl:text>
                <xsl:text>&#x09;----------------------------&#xA;</xsl:text>
                <xsl:for-each select="TestSuite">
                    <xsl:text>&#xA;&#x09;*************************************************************&#xA;</xsl:text>
                    <xsl:text>&#x09;* Start TestSuite </xsl:text><xsl:value-of select="@name" /><xsl:text>&#xA;</xsl:text>
                    <xsl:variable name="suitename" select="@name" />
                    <xsl:for-each select="TestCase">
                        <xsl:text>&#x09;*&#xA;</xsl:text>
                        <xsl:text>&#x09;*&#x09;**********************************************************&#xA;</xsl:text>
                        <xsl:text>&#x09;*&#x09;* Start TestCase </xsl:text><xsl:value-of select="@name" /><xsl:text>&#xA;</xsl:text>
                        <xsl:text>&#x09;*&#x09;*&#xA;</xsl:text>
                        <xsl:variable name="casename" select="@name" />
                        <xsl:for-each select="document($STR_BoostLogFile)/TestLog/TestSuite/TestSuite[@name=$suitename]/TestCase[@name=$casename]/*">
                                <xsl:if test="name()='Error'"><xsl:text>&#x09;*&#x09;*&#x09;!!! ERROR !!! : </xsl:text><xsl:value-of select="." /><xsl:text>( line </xsl:text><xsl:value-of select="@line" /><xsl:text> in </xsl:text><xsl:value-of select="@file" /><xsl:text>)&#xA;</xsl:text></xsl:if>
                                <xsl:if test="name()='Message'"><xsl:text>&#x09;*&#x09;*&#x09;</xsl:text><xsl:value-of select="." /><xsl:text>&#xA;</xsl:text></xsl:if>
                        </xsl:for-each>
                        <xsl:text>&#x09;*&#x09;*&#xA;</xsl:text>
                        <xsl:text>&#x09;*&#x09;* End TestCase </xsl:text><xsl:value-of select="@name" /><xsl:text>&#xA;</xsl:text>
                        <xsl:text>&#x09;*&#x09;**********************************************************&#xA;</xsl:text>
                    </xsl:for-each>
                    <xsl:text>&#x09;*&#xA;</xsl:text>
                    <xsl:text>&#x09;* End TestSuite </xsl:text><xsl:value-of select="@name" /><xsl:text>&#xA;</xsl:text>
                    <xsl:text>&#x09;*************************************************************&#xA;&#xA;</xsl:text>
                </xsl:for-each>
                <xsl:text>****************************************************************&#xA;</xsl:text>
                <xsl:text>**************** END TEST UNITAIRE </xsl:text><xsl:value-of select="@name" /><xsl:text> ****************&#xA;</xsl:text>
                <xsl:text>****************************************************************&#xA;</xsl:text>
            </xsl:for-each>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
