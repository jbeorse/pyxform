"""
xls2xform converts properly formatted Excel documents into XForms for
use with ODK Collect. xl2xform is called at the command line using::

    python xls2xform.py path-to-excel-file

This will create a new XForm in the directory containing the excel
file.
"""
import os, sys, random
from builder import create_survey_from_path

if __name__ == '__main__':
    path_to_excel_file = sys.argv[1]
    survey = create_survey_from_path(path_to_excel_file)
    directory, filename = os.path.split(path_to_excel_file)
    path_to_xform = os.path.join(directory, survey.get_name() + ".xml")
    survey.print_xform_to_file(path_to_xform, False)
