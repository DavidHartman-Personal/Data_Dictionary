# constants.py
import os

"""This module defines project-level constants."""

#: This effectively defines the root of the project and so adding ..\, etc. is not needed in config files
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

#: Directory that contains configuration files
CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')

#: Directory were data files/extracts/reports will be stored
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, 'data')

#: Directory were output files can be stored
OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, 'output_files')

#: Directory were data files/extracts/reports will be stored
EXCEL_FILE_DIR = os.path.join(PROJECT_ROOT_DIR, 'input_files')

#: Default source excel file name
SOURCE_FILE_DEFAULT = os.path.join(EXCEL_FILE_DIR, 'source.xlsx')

#: Configuration file path.  Uses environment variable if none is defined.
FILENAME_INPUT_CONFIG = os.environ.get('CONFIG_FILE_PATH',
                                       os.path.join(CONF_DIR, 'data_dictionary.conf'))

DEFAULT_SPREADSHEET = "C:\\Users\\DHARTMAN\\Documents\\Programming\\PycharmProjects\\Data_Dictionary\\input_files\\po_sample.xlsx"

#: Default Excel cell/row/col for a data dictionary worksheet
DEFAULT_HEADER_ROW = '1'
DEFAULT_FIRST_COL = 'A'
DEFAULT_LAST_COL = 'B'
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

#
# columns=['Field Name', 'Field Type', 'Model Level', 'UI Audit', 'Required',
#        'USAID Required', 'USAID Model - Regular PO', 'Regular PO',
#        'Distribution Order', 'Repleneshiment Order', 'Format', 'Max Length',
#        'Description']

SOURCE_DATA_DICT_MAPPING = {
    'source_worksheet_name': 'PurchaseOrder_IB',
    'entity_name': "PURCHASE_ORDER_IB",
    'subject_area': "Transaction: Order Management",
    'environment': "Data Generation",
    'source_file_name': "C:\\Users\\DHARTMAN\\Documents\\Programming\\PycharmProjects\\Data_Dictionary\\input_files\\po_sample.xlsx",
    # worksheet columns are mapped to data dictionary attributes, e.g. 'Field Name' is the Attribute.name
    'attribute_column_mapping': {
        'name': "Field Name",
        'data_type': "Field Type",
        'required': "Required",
        'description': "Description",
        'max_length': "Max Length",
        'mask': "Format"
    }
}
