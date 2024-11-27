"""Read and Show Excel workbook details

This script will open an Excel Workbook and then show some details about the workbook.  It uses configuration files, and references the data/ directory.

"""

import argparse
import configparser
import os
import excel_workbook
import logging
import coloredlogs

#: This effectively defines the root of the project and so adding ..\, etc. is not needed in config files
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

#: Directory that contains configuration files
CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')

#: Directory were data files/extracts/reports will be stored
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, 'data')

#: Directory were data files/extracts/reports will be stored
EXCEL_FILE_DIR = os.path.join(PROJECT_ROOT_DIR, 'excel_files')

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
    source_spreadsheet_name = "sample.xlsx"
    source_spreadsheet_file = os.path.join(EXCEL_FILE_DIR, source_spreadsheet_name)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_file',type=str,help="The spreadsheet file to print the columns of",
                        nargs='?',default=source_spreadsheet_file)
    parser.add_argument('--config', '-c', dest='filename_config', action='store', default=FILENAME_INPUT_CONFIG,
                        help='Config file for generating AWS User Access Report - Default is Environment variable CONFIG_FILE_PATH')
    args=parser.parse_args()
    config = configparser.ConfigParser()
    logging.info("Reading config file [%s]", args.filename_config)
    # Confirm config file exists before reading
    try:
        with open(args.filename_config) as f:
            config.read(args.filename_config)
    except Exception as e:
        logging.error("Error Reading config file [%s]: [%s]", args.filename_config, str(e))
        raise ValueError("Error Reading config file [%s]: [%s]", args.filename_config, str(e))
    header_row = config.get('data_dictionary', 'header_row', fallback=DEFAULT_HEADER_ROW)
    first_col = config.get('data_dictionary', 'first_col',fallback=DEFAULT_FIRST_COL)
    last_col = config.get('data_dictionary', 'last_col',fallback=DEFAULT_LAST_COL)
    logging.info("Getting excel info header row:[%s], first col [%s], last col [%s]", header_row,first_col,last_col)
    excel_wb = excel_workbook.ExcelWorkbook(source_spreadsheet_file)
    excel_ws = excel_wb.get_worksheets()
    for ws in excel_ws:
        print(str(ws))
    # open_poam_ws = poam_wb[in_open_poam_worksheet_name]
    # For a worksheet, get the table data to create the data dictionary object

    # get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()
