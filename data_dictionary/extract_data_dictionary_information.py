"""This script is used to extract various details related to DataDictionary information from various sources

This script is used to extract various details related to DataDictionary information from various sources.
This includes spreadsheets, Documents, CSV files, etc.
The intention is to use the information to create a complete mapping and configurations of the various sources of information
related to Data Dictionary details.
The information will be captured in a dictionary that can then be utilized by other scripts/modules/etc. to extract
all metadata needed to create a complete data dictionary.

"""

import argparse
import configparser
import os
import logging
import coloredlogs
from data_dictionary import constants
from openpyxl import load_workbook, worksheet
import pandas as pd
import json
import pprint as pp
from model import DataDictionary as dd
from pathlib import Path
import numpy as np
from excel_workbook import show_excel_file_details

coloredlogs.install(level=logging.DEBUG,
                    fmt="%(asctime)s %(hostname)s %(name)s %(filename)s line-%(lineno)d %(levelname)s - %(message)s",
                    datefmt='%H:%M:%S')


def get_excel_file_worksheets(spreadsheet_file: Path):
    """Gets details of an Excel file.

    This function will extract details of an Excel file.  The details will be returned in a TBD data structure.

    Args:
      spreadsheet_file (Path): The worksheet name

    Returns:
      None
    """
    logging.info("Getting worksheets")
    excel_wb = load_workbook(filename=spreadsheet_file, data_only=True)
    for worksheet in excel_wb.worksheets:
        logging.info("Workbook worksheet: %s", worksheet.title)


def read_in_data_dictionary(data_dictionary_source_file: Path) -> dd:
    """Create a DataDictionary instance using the classmethod for creating instance from JSON file.

    TODO: (P3) Add steps to confirm JSON file is structured as required.

    Args:
        data_dictionary_source_file (Path): Location of existing data dictionary JSON File.
    Returns:
         DataDictionary: Data dictionary object
    """
    logging.info("Reading in data dictionary...")
    data_dict_from_json = dd.DataDictionary.create_data_dictionary_from_json(data_dictionary_source_file)
    return data_dict_from_json


def create_data_dictionary_markdown_files() -> None:
    """Creates markdown files based on DataDictionary instance

    Returns:
        None
    """
    input_file_name = "po_sample.xlsx"
    output_file_name = "data_dictionary.json"
    dd_output_file = constants.OUTPUT_FOLDER / output_file_name

    dd_1 = read_in_data_dictionary(constants.TEST_DATA_FILE)
    dd_1.write_data_dictionary(dd_output_file)
    dd_1.create_markdown_files(constants.MARKDOWN_FILE_DIR, force_overwrite=True)


def main():
    """The main method for this script.

    """

    def process_args():
        logging.info("Processing command line Arguments")
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('input_file', type=str, help="The spreadsheet file to print the columns of",
                            nargs='?', default=constants.DEFAULT_SPREADSHEET)
        parser.add_argument('--config', '-c', dest='filename_config', action='store',
                            default=constants.FILENAME_INPUT_CONFIG,
                            help='Config file for generating AWS User Access Report - Default is Environment variable CONFIG_FILE_PATH')
        args = parser.parse_args()
        return args.filename_config

    config_filename = process_args()

    def get_configs(config_filename_in):
        logging.info("Getting config file values from [%s]", str(config_filename_in))
        config = configparser.ConfigParser()
        try:
            with open(config_filename_in) as f:
                config.read(config_filename)
        except Exception as e:
            logging.error("Error Reading config file [%s]: [%s]", config_filename, str(e))
            raise ValueError("Error Reading config file [%s]: [%s]", config_filename, str(e))
        header_row_out = config.get('po_sample', 'header_row', fallback=constants.DEFAULT_HEADER_ROW)
        first_col_out = config.get('po_sample', 'first_col', fallback=constants.DEFAULT_FIRST_COL)
        last_col_out = config.get('po_sample', 'last_col', fallback=constants.DEFAULT_LAST_COL)
        source_file_name_out = config.get('po_sample', 'source_file_name', fallback=constants.DEFAULT_SPREADSHEET)
        source_worksheet_name_out = config.get('po_sample', 'source_worksheet_name')
        return header_row_out, first_col_out, last_col_out, source_file_name_out, source_worksheet_name_out

    (header_row, first_col, last_col, source_spreadsheet_file, source_worksheet_name) = get_configs(config_filename)
    input_file_name = "po_sample.xlsx"
    output_file_name = "data_dictionary.json"
    test_spreadsheet = constants.SOURCE_FOLDER / input_file_name
    dd_output_file = constants.OUTPUT_FOLDER / output_file_name
    data_dict = dd.DataDictionary(name="USAID_Data_Dictionary",
                                  description="USAID Data Dictionary for One Network system",
                                  subject_area="All",
                                  environment="All",
                                  source_filename=test_spreadsheet
                                  )
    # create_entities_from_excel_worksheet(test_spreadsheet, data_dict)
    data_dict.write_data_dictionary(dd_output_file)


if __name__ == "__main__":
    pil_logger = logging.getLogger('PIL')
    pil_logger.setLevel(logging.INFO)
    for source_spreadsheet in constants.SOURCE_SPREADSHEETS:
        logging.info("Getting worksheets for: %s using panda DataFrame", str(source_spreadsheet))
        # get_excel_file_worksheets(source_spreadsheet)
        # worksheets = show_excel_file_details.get_worksheets(source_spreadsheet)
        # excel_poib_data = pd.read_excel(source_spreadsheet,
        #                             sheet_name=constants.SOURCE_DATA_DICT_MAPPING['source_worksheet_name']).replace(
        # np.nan, None)

        # for name, sheet in excel_poib_data.items():
        #     logging.info("Worksheet: %s", str(name))
        #
        sheets_dict = pd.read_excel(source_spreadsheet, sheet_name=None)


        # all_sheets = []
        # for name, sheet in sheets_dict.items():
        #     # sheet['sheet'] = name
        #     logging.info("Worksheet: %s",str(name))
        #     # sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
        #     all_sheets.append(str(name))

        # full_table = pd.concat(all_sheets)
        # full_table.reset_index(inplace=True, drop=True)
        #
        # print(full_table)



    # main()

    # ************* Steps that were used to created markdown files ********************************
    # input_file_name = "po_sample.xlsx"
    # output_file_name = "data_dictionary.json"
    # test_spreadsheet = constants.SOURCE_FOLDER / input_file_name
    # dd_output_file = constants.OUTPUT_FOLDER / output_file_name
    #
    # dd_1 = read_in_data_dictionary(constants.TEST_DATA_FILE)
    # dd_1.write_data_dictionary(dd_output_file)
    # dd_1.create_markdown_files(constants.MARKDOWN_FILE_DIR, force_overwrite=True)
    # *************  ********************************
    #
    # excel_poib_data = pd.read_excel(test_spreadsheet,
    #                                 sheet_name=constants.SOURCE_DATA_DICT_MAPPING['source_worksheet_name']).replace(
    #     np.nan, None)
    # entity = dd.Entity(name=constants.SOURCE_DATA_DICT_MAPPING['entity_name'],
    #                    description=constants.SOURCE_DATA_DICT_MAPPING['entity_name'],
    #                    subject_area=constants.SOURCE_DATA_DICT_MAPPING['subject_area'],
    #                    environment=constants.SOURCE_DATA_DICT_MAPPING['environment']
    #                    )
    # for row_label, row in excel_poib_data.iterrows():
    #     entity_attribute = dd.Attribute(
    #         name=row[constants.SOURCE_DATA_DICT_MAPPING['attribute_column_mapping']['name']],
    #         description=row[constants.SOURCE_DATA_DICT_MAPPING['attribute_column_mapping']['description']],
    #         data_type=row[constants.SOURCE_DATA_DICT_MAPPING['attribute_column_mapping']['data_type']],
    #         subject_area=constants.SOURCE_DATA_DICT_MAPPING['subject_area'],
    #         environment=constants.SOURCE_DATA_DICT_MAPPING['environment'],
    #         max_length=row[constants.SOURCE_DATA_DICT_MAPPING['attribute_column_mapping']['max_length']],
    #     )
    #     entity.add_attribute(entity_attribute)
    # data_dict.add_entity(entity)
