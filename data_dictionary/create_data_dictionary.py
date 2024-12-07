"""Create a data dictionary object from an Excel Workbook that contains data/details.

This script data from an Excel workbook to create a data dictionary object.

"""

import argparse
import configparser
import os
from excel_workbook.excel_workbook import ExcelWorkbook
from model.DataDictionary import DataDictionaryData, EntityData, AttributeData
import logging
import coloredlogs

#: This effectively defines the root of the project and so adding ..\, etc. is not needed in config files
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

#: Directory that contains configuration files
CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')

#: Directory were data files/extracts/reports will be stored
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, 'data')

#: Directory were data files/extracts/reports will be stored
EXCEL_FILE_DIR = os.path.join(PROJECT_ROOT_DIR, 'input_files')

#: Configuration file path.  Uses environment variable if none is defined.
FILENAME_INPUT_CONFIG = os.environ.get('CONFIG_FILE_PATH',
                                       os.path.join(CONF_DIR, 'excel.conf'))

#: Default Excel cell/row/col for a data dictionary worksheet
DEFAULT_HEADER_ROW='1'
DEFAULT_FIRST_COL='A'
DEFAULT_LAST_COL='B'

coloredlogs.install(level=logging.DEBUG,
                    fmt="%(asctime)s %(hostname)s %(name)s %(filename)s line-%(lineno)d %(levelname)s - %(message)s",
                    datefmt='%H:%M:%S')

def main():
    """The main method for this script.

    """
    source_spreadsheet_name = "po_sample.xlsx"
    source_spreadsheet_file = os.path.join(EXCEL_FILE_DIR, source_spreadsheet_name)
    def process_args():
        logging.info("Processing command line Arguments")
    config_filename = process_args()
    def get_configs(config_filename):
        logging.info("Getting config file values")

    (header_row, first_col, last_col) = get_configs(config_filename)
    logging.info("Creating ExcelWorkbook [%s]", source_spreadsheet_file)
    excel_wb = ExcelWorkbook(source_spreadsheet_file)
    excel_ws = excel_wb.get_worksheets()
    logging.info("Getting excel info header row:[%s], first col [%s], last col [%s]", header_row,first_col,last_col)
    for ws in excel_ws:
        logging.info("Getting Workshet [%s]", str(ws))
        print(str(ws))
    # open_poam_ws = poam_wb[in_open_poam_worksheet_name]
    # For a worksheet, get the table data to create the data dictionary object
    # get_spreadsheet_cols(args.input_file, print_cols=True)

if __name__ == "__main__":
    main()
