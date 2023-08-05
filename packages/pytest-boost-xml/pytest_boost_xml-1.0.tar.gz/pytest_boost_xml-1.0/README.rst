========
Overview
========

This plugin generates report in the boost format, containing informations about passed assertions and extra information messages.


Installation
============
Install with pip::

    pip install pytest-boost-xml

Uninstalling
------------

Uninstall with pip::

    pip uninstall pytest-boost-xml

Usage
=====

pytest.ini file must be configured with pytest_assertion_pass hook activated::

	[pytest]
	enable_assertion_pass_hook=true

pytest command line parameters are::

    pytest --boost_xml=path_to_reports [--boost_xml_filename=report_file_name] [--boost_xml_report_title=report_title]

with:

* report_file_name: base name for generated files. Default is 'boostReport'
* report_title: title of generated report files. Default is ''

An actual pytest call like::

    pytest --boost_xml=reports --boost_xml_filename=campaign --boost_xml_report_title=my_project

would produce reports like::

    reports
       |
       |---- campaign_Log.xml
       |
       |---- campaign_Summary.xml
       |
       |---- campaign.html
