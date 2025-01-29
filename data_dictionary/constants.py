"""Constants for Data Dictionary project
TODO: Replace os path calls with pathlib calls.
"""
# constants.py
import os
from pathlib import Path

# from data_dictionary.create_data_dictionary import EXCEL_FILE_DIR

"""This module defines project-level constants."""

#: This effectively defines the root of the project and so adding ..\, etc. is not needed in config files
# PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT_DIR = Path(__file__).parents[1].resolve()

#: Directory that contains configuration files
CONF_DIR = PROJECT_ROOT_DIR / 'conf'

# CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')
# CONF_DIR = PROJECT_ROOT_DIR

#: Directory were data files/extracts/reports will be stored
DATA_DIR = PROJECT_ROOT_DIR / 'data'

#: Directory were output files can be stored
OUTPUT_DIR = PROJECT_ROOT_DIR / 'output'
# OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, 'output_files')

#: Directory were data files/extracts/reports will be stored
# EXCEL_FILE_DIR = os.path.join(PROJECT_ROOT_DIR, 'input_files')
INPUT_FILE_DIR = PROJECT_ROOT_DIR / 'input_files'

#: Default source excel file name
# SOURCE_FILE_DEFAULT = os.path.join(EXCEL_FILE_DIR, 'source.xlsx')
SOURCE_FILE_DEFAULT = INPUT_FILE_DIR / 'source.xlsx'

#: Configuration file path.  Uses environment variable if none is defined.
# FILENAME_INPUT_CONFIG = os.environ.get('CONFIG_FILE_PATH',
#                                        os.path.join(CONF_DIR, 'data_dictionary.conf'))

FILENAME_INPUT_CONFIG = CONF_DIR / 'data_dictionary.conf'

DEFAULT_SPREADSHEET = INPUT_FILE_DIR / 'po_sample.xlsx'

SOURCE_FOLDER = Path.home() / 'Documents' / 'Programming' / 'PycharmProjects' / 'Data_Dictionary' / 'input_files'
PLAYBOOK_FOLDER = Path.home() / 'Documents' / 'Playbook'
OUTPUT_FOLDER = Path.home() / 'Documents' / 'Programming' / 'PycharmProjects' / 'Data_Dictionary' / 'output_files'
TESTS_FOLDER = Path.home() / 'Documents' / 'Programming' / 'PycharmProjects' / 'Data_Dictionary' / 'tests'
TEST_DATA_FOLDER = Path.home() / 'Documents' / 'Programming' / 'PycharmProjects' / 'Data_Dictionary' / 'tests' / 'test_data'
DOCS_FOLDER = Path.home() / 'Documents' / 'Programming' / 'PycharmProjects' / 'Data_Dictionary' / 'docs'
MARKDOWN_FILE_DIR = OUTPUT_FOLDER / 'markdown'

TEST_DATA_FILE = TEST_DATA_FOLDER / 'data_dictionary.json'

TAB_SEPARATOR = "\t"
COMMA_SEPARATOR = ", "
MARKDOWN_ATTRIBUTE_HEADER_ROW = ["Attribute Name", "Description", "Data Type", "Required"]

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

SOURCE_DATA_DICT_MAPPING = dict(source_worksheet_name='OMS.SalesOrder_IBv4.0',
                                entity_name="OMS_SALES_ORDER",
                                subject_area="Transaction: Order Management",
                                environment="Data Generation",
                                source_file_name="C:\\Users\\DHARTMAN\\Documents\\Programming\\PycharmProjects\\Data_Dictionary\\input_files\\AllUSAIDInterfaces-Release Date -11-15-2024.xlsx",
                                attribute_column_mapping={
                                    'name': "Field Name",
                                    'data_type': "Field Type",
                                    'required': "Required",
                                    'description': "Description",
                                    'max_length': "Max Length",
                                    'mask': "Format"
                                })

# An array of dictionary items that define sources for Data Dictionary information.
ENTITIES_SOURCES = [
    dict(source_file_name=SOURCE_FOLDER / 'AllSalesOrdersEntityAttributes.xlsx',
         source_worksheet_name='SalesOrderTest',
         entity_name="SALES_ORDER",
         subject_area="Transaction: Order Management",
         description="Small data set of Sales Order for Testing",
         environment="Data Generation",
         attribute_column_mapping=dict(name="Field Name",
                                       data_type="Field Type",
                                       required="Required",
                                       description="Description",
                                       keys="Keys",
                                       parent_entity="Parent Entity",
                                       parent_attribute="Parent Attribute",
                                       parent_return_attribute="Parent Return Attribute",
                                       join_criteria="Join Criteria",
                                       parent_filter_criteria="Parent Filter Criteria",
                                       max_length="Max Length",
                                       mask="Format")
         )
    ,
    dict(source_file_name=SOURCE_FOLDER / 'AllSalesOrdersEntityAttributes.xlsx',
         source_worksheet_name='Enterprise',
         entity_name="ENTERPRISE",
         subject_area="Enterprise entity",
         description="The highest level in the Enterprise/Organization/Site Hierarchy",
         environment="Data Generation",
         attribute_column_mapping=dict(name="Field Name",
                                       data_type="Field Type",
                                       required="Required",
                                       description="Description",
                                       keys="Keys",
                                       parent_entity="Parent Entity",
                                       parent_attribute="Parent Attribute",
                                       parent_return_attribute="Parent Return Attribute",
                                       join_criteria="Join Criteria",
                                       parent_filter_criteria="Parent Filter Criteria",
                                       max_length="Max Length",
                                       mask="Format"
                                       )
         ),
    dict(source_file_name=SOURCE_FOLDER / 'AllSalesOrdersEntityAttributes.xlsx',
         source_worksheet_name='Organization',
         entity_name="ORGANIZATION",
         subject_area="Organization entity",
         description="Level 2 in the Enterprise/Organization/Site Hierarchy",
         environment="Data Generation",
         attribute_column_mapping=dict(name="Field Name",
                                       data_type="Field Type",
                                       required="Required",
                                       description="Description",
                                       keys="Keys",
                                       parent_entity="Parent Entity",
                                       parent_attribute="Parent Attribute",
                                       parent_return_attribute="Parent Return Attribute",
                                       join_criteria="Join Criteria",
                                       parent_filter_criteria="Parent Filter Criteria",
                                       max_length="Max Length",
                                       mask="Format"
                                       )
         ),
    dict(source_file_name=SOURCE_FOLDER / 'AllSalesOrdersEntityAttributes.xlsx',
         source_worksheet_name='Site',
         entity_name="SITE",
         subject_area="Site entity",
         description="Level 3 in the Enterprise/Organization/Site Hierarchy",
         environment="Data Generation",
         attribute_column_mapping=dict(name="Field Name",
                                       data_type="Field Type",
                                       required="Required",
                                       description="Description",
                                       keys="Keys",
                                       parent_entity="Parent Entity",
                                       parent_attribute="Parent Attribute",
                                       parent_return_attribute="Parent Return Attribute",
                                       join_criteria="Join Criteria",
                                       parent_filter_criteria="Parent Filter Criteria",
                                       max_length="Max Length",
                                       mask="Format"
                                       )
         )
]

# Add or update information about a Trade Item
# Required Interfaces	SCC.Item_IB – Adds or updates information for a Trade Item
# SCC.ItemMapping_IB – Adds or updates how Trade Items are mapped to the SCCT Product Catalog Generic Item
# SCC.ItemSubstitution_IB – Adds or updates information regarding valid item substitutions that are related to the Trade Item
# SCC.AttribSet_IB – Adds or updates mapping information for custom attributes related to the Trade Item (if applicable)
# SCC.Bill of Material  – Adds or updates information about Trade Items that have Bill of Material or Kit components (if applicable)
# Filenames	scc/item_ib_[timestamp].csv
# scc/itemmapping_ib_[timestamp].csv
# scc/itemsubstitution_ib_[timestamp].csv
# scc/attribset_ib_[timestamp].csv
# scc/billofmaterials_ib_[timestamp].csv
# Dependencies	The SCCT Generic Item. If you believe your Trade Item should be associated with an SCCT Generic Item that is not listed, please contact the SCCT Project Team.
#

ENTITY_RELATIONSHIP_MAPPINGS = [
    dict(parent_entity='ENTERPRISE',
         parent_attribute='ENTERPRISE_ID',
         child_entity="SALES_ORDER",
         child_attribute="Creation Org Enterprise Name",
         relationship_type="FK-PK",
         description="All Sales orders have a Creation Organization that is an Existing Enterprise")
    ,
    dict(parent_entity='ENTERPRISE',
         parent_attribute='ENTERPRISE_NAME',
         child_entity="OMS_SALES_ORDER",
         child_attribute="Owning Org Enterprise Name",
         relationship_type="FK-PK",
         description="All Sales orders have a Owning Organization that is an Existing Enterprise")
]

DATA_INTERFACE_MAPPINGS = [
    dict(interface_name='',
         data_provider='ENTERPRISE_NAME',
         format="CSV, Excel, etc.",
         output_name="salesorder_ib_[mmddyyyy].csv",
         description="All Sales orders have a Creation Organization that is an Existing Enterprise")
    ,
    dict(parent_entity='ENTERPRISE',
         parent_attribute='ENTERPRISE_NAME',
         child_entity="OMS_SALES_ORDER",
         child_attribute="Owning Org Enterprise Name",
         relationship_type="FK-PK",
         description="All Sales orders have a Owning Organization that is an Existing Enterprise")
]

INTERFACE_PROCESSING = [
    dict(interface_name='item_ib_YYYYMMDD.CSV',
         interface_entity='ITEM',
         interface_description="Trade Item",
         interface_format="CSV", delimiter=",",
         fields=[],
         processing_order=1,
         )
    ,
    dict(interface_name='salesorder_ib_YYYYMMDD.CSV',
         interface_entity='OMS_SALES_ORDER',
         interface_description="OMS_SALES_ORDER",
         interface_format="CSV",
         delimiter=",",
         fields=[],
         processing_order=9
         )
]

# oms/salesorder_ib_[timestamp].csv
# Depdendencies: The SCCT Vendor for your supplier (if applicable ).
# The SCCT Customer for your customer.
# The SCCT Site for your ship-from source (Vendor).
# The SCCT Site for your ship-to destination (Customer or Partner).
# The applicable Trade Items have been created in the SCCT.
# oms/salesorder_ib_[timestamp].csv

TEST_DATA_GENERATION_MAPPINGS = [
    dict(parent_entity='ENTERPRISE',
         parent_attribute='ENTERPRISE_NAME',
         child_entity="OMS_SALES_ORDER",
         child_attribute="Creation Org Enterprise Name",
         relationship_type="FK-PK",
         description="All Sales orders have a Creation Organization that is an Existing Enterprise")
    ,
    dict(parent_entity='ENTERPRISE',
         parent_attribute='ENTERPRISE_NAME',
         child_entity="OMS_SALES_ORDER",
         child_attribute="Owning Org Enterprise Name",
         relationship_type="FK-PK",
         description="All Sales orders have a Owning Organization that is an Existing Enterprise")
]

#     dict(SOURCE_FILES=
# [
#     dict(FILE_NAME=SOURCE_FOLDER / 'AllUSAIDInterfaces-Release Date -11-15-2024.xlsx',
#          SHEET_NAME='HCPT.SalesOrder_IBv1.0'),
#     dict(FILE_NAME=SOURCE_FOLDER / 'AllUSAIDInterfaces-Release Date -11-15-2024.xlsx',
#          SHEET_NAME='OMS.SalesOrder_IBv4.0')
# ]
# ))

# HCPT.SalesOrder_IBv1.0
# OMS.SalesOrder_IBv4.0
# TODO: Include DW Schema spreadsheet
SOURCE_SPREADSHEETS = [SOURCE_FOLDER / 'AllUSAIDInterfaces-Release Date -11-15-2024.xlsx',
                       SOURCE_FOLDER / 'SCCT Enterprise Mapping Document 20240813.xlsx',
                       SOURCE_FOLDER / 'USAID NextGen SCCT GHSC-PSM Implementing Partner Specifications v1.2.xlsx']

SOURCE_COLUMNS = ['Field Type',
                  'UI Audit',
                  'Model level',
                  'Required',
                  'USAID Required',
                  'Requisition Order(Regular SO)',
                  'Distribution Order',
                  'Replenishment Order',
                  'Format',
                  'Max Length',
                  'Description',
                  'USAID Model'
                  ]
