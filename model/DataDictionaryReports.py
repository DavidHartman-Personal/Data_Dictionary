"""A Data Dictionary contains details regarding data withing a Business, Application, Process, etc.

A Data Dictionary object contains detailed information regarding data that is created and managed in support of any process (Business, Application, etc.)
The information captured for the data includes details regarding format, relationships to other data/information, lineage, lifecycle, etc.

    Attributes:
            workbook_filename (str): The full filename path to the Excel workbook
            worksheets (int):  A dictionary containing the Excel worksheets in the Excel workbook
            defined_names (str): An array of the defined names in the Excel workbook


    Methods
    -------

"""
from __future__ import annotations

__version__ = '2024.11'
__author__ = 'David Hartman'

import logging
import os
import sys
from openpyxl import load_workbook
import coloredlogs
from pprint import pp
from typing import List
import json
from datetime import datetime, date
from pathlib import Path

#: This effectively defines the root of this project and so adding ..\, etc is not needed in config files
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Add script directory to the path to allow searching for modules
sys.path.insert(0, PROJECT_ROOT_DIR)

#: Directory that contains configuration files
CONF_DIR = os.path.join(PROJECT_ROOT_DIR, 'conf')

tab_separator = "\t"
comma_separator = ", "

# import any functions inside or outside of this module.  If no helpers are needed it can be removed from here
# as well as remove the file from the excel_workbook module.
# from . import helpers

coloredlogs.install(level=logging.INFO,
                    fmt="%(asctime)s %(hostname)s %(name)s %(filename)s line-%(lineno)d %(levelname)s - %(message)s",
                    datefmt='%H:%M:%S')


def datetime_default(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


class Attribute:
    """An Attribute contains details about a data attribute/column including data type information.

    An Attribute contains details about a data attribute typically associated with entities.  The information generally includes details
    related to data type, masks and relationships to other data elements (e.g. parent-child, pk, fk, etc.).

    Args:
        name (str): A name for the data attribute.
        description (str): A description for the data attribute.
        subject_area (str): A subject area or type of data.  This includes master data, transactional data, configuration data, etc.
        environment (str): A environment for the data attribute.

    """

    def __init__(
            self,
            name: str,
            description: str,
            subject_area: str,
            environment: str,
            data_type: str,
            max_length: int = 0,
            key_types: list[str] = None,
            mask: str = "Y",
            required: str = "Y",
            parent_entity_attributes: list[(str, str)] = None
    ) -> None:
        if len(name) == 0:
            raise NameError("Attribute name is required")
        self.required = required
        self.key_types = key_types
        self.mask = mask
        self.max_length = max_length
        self.name = name
        self.description = description
        self.subject_area = subject_area
        self.environment = environment
        self.data_type = data_type
        self._attribute_id = str(name).upper()
        if len(parent_entity_attributes) != 0:
            logging.info("Attribute contains foreign keys.  Checking that Entity and Attribute exist")

    def to_dict(self):
        attribute_dict = dict(ATTRIBUTE_ID=self._attribute_id,
                              ATTRIBUTE_NAME=self.name,
                              DESCRIPTION=self.description,
                              SUBJECT_AREA=self.subject_area,
                              ENVIRONMENT=self.environment,
                              DATA_TYPE=self.data_type,
                              MAX_LENGTH=self.max_length,
                              REQUIRED=self.required)
        return attribute_dict

    @classmethod
    def attribute_from_dict(cls, attribute_dict: dict) -> Attribute:
        """Creates an instance of DataDictionary based on a dict containing an Attribute definition

        Creates an instance of Entity from a dict containing Attribute details, including attributes.
        TODO: Add check for keys in dictionary when creating an Attribute (i.e. confirm dict has ENTITY_NAME, etc.)

        Args:
             attribute_dict (dict): A dictionary containing an Attribute definition
        Returns:
             Attribute Class Object:
        """
        return cls(name=attribute_dict.get('ATTRIBUTE_NAME', "Required"),
                   description=attribute_dict.get('DESCRIPTION', "Description"),
                   subject_area=attribute_dict.get('SUBJECT_AREA', ""),
                   environment=attribute_dict.get('ENVIRONMENT', ""),
                   data_type=attribute_dict.get('DATA_TYPE', ""),
                   max_length=attribute_dict.get('MAX_LENGTH', 0),
                   key_types=attribute_dict.get('KEY_TYPES', []),
                   required=attribute_dict.get('REQUIRED', ""),
                   mask=attribute_dict.get('MASK', ""),
                   parent_entity_attributes=attribute_dict.get('PARENT_ENTITY_ATTRIBUTES', list()),
                   )


class Entity:
    """An Attribute contains details about a data attribute/column including data type information.

    An Attribute contains details about a data attribute typically associated with entities.  The information generally includes details
    related to data type, masks and relationships to other data elements (e.g. parent-child, pk, fk, etc.).

    Args:
        name (str): A name for the data attribute.
        description (str): A description for the data attribute.
        subject_area (str): A subject area for the data attribute.
        environment (str): A environment for the data attribute.
        attributes (List[Attribute]): A list of attributes.

    TODO: Change attributes to a dictionary and add check that attribute does not already exist for entity
    TODO: Add check for required elements and raise errors as needed.
    TODO: Add registry that includes all Entities created and their attributes

    """

    def __init__(
            self,
            name: str,
            description: str,
            subject_area: str,
            environment: str,
            attributes: list[Attribute] = None
    ) -> None:
        if len(name) == 0:
            raise NameError("Entity Name must be provided")
        self.name = name
        self.description = description
        self.subject_area = subject_area
        self.environment = environment
        self.attributes = attributes
        if attributes is None:
            self.attribute_count = 0
            self.attributes = list()
        else:
            self.attribute_count = len(attributes)
            self.attributes = list(attributes)
        # TODO: Add check that _entity_id is unique in the DataDictionary
        self._entity_id = str(name).upper()

    def __str__(self):
        return_str = ""
        try:
            return_str = "Entity {name} has {attribute_count} attributes".format(
                name=self.name,
                attribute_count=len(self.attributes)
            )
        except Exception as e:
            logging.error("Could not print string for object [%s]", str(e))
        return return_str

    def to_json(self) -> str:
        """Converts an Entity instance into a dictionary object containing Entity data elements

        Returns:
            Entity dict (str): JSON formatted string
        """
        entity_dict = dict(ENTITY_ID=self._entity_id,
                           ENTITY_NAME=self.name,
                           DESCRIPTION=self.description,
                           SUBJECT_AREA=self.subject_area,
                           ENVIRONMENT=self.environment)
        return json.dumps(entity_dict, separators=(',', ': '))

    def to_dict(self) -> dict:
        """Create a dictionary object containing Entity properties

        Returns:
            dict: A dictionary object containing Entity properties
        """
        attribute_list = list()
        for attribute in self.attributes:
            attribute_list.append(attribute.to_dict())
        entity_dict = dict(ENTITY_ID=self._entity_id,
                           ENTITY_NAME=self.name,
                           DESCRIPTION=self.description,
                           SUBJECT_AREA=self.subject_area,
                           ENVIRONMENT=self.environment,
                           ATTRIBUTES=attribute_list)
        return entity_dict

    @classmethod
    def entity_from_dict(cls, entity_dict: dict) -> Entity:
        """Creates an instance of DataDictionary based on a dict containing an Entity definition

        Creates an instance of Entity from a dict containing Entity details, including attributes.
        TODO: Add check for keys in dictionary when creating an Entity (i.e. confirm dict has ENTITY_NAME, etc.)

       Args:
             entity_dict (dict): A dictionary containing an Entity definition
       Returns:
             Entity Class Object:
        """
        attribute_list = list()
        for attribute in entity_dict['ATTRIBUTES']:
            # Create attribute object and add to Entity
            logging.info("Creating Attribute for Entity: [%s].[%s]",
                         str(entity_dict['ENTITY_NAME']),
                         str(attribute['ATTRIBUTE_NAME']))
            new_attribute = Attribute.attribute_from_dict(attribute_dict=attribute)
            attribute_list.append(new_attribute)
        return cls(name=entity_dict.get('ENTITY_NAME', "Required"),
                   description=entity_dict.get('DESCRIPTION', ""),
                   subject_area=entity_dict.get('SUBJECT_AREA', ""),
                   environment=entity_dict.get('ENVIRONMENT', ""),
                   attributes=attribute_list)

    @classmethod
    def entity_from_json(cls, entity_json_string: str) -> Entity:
        """Create an Entity instance from JSON formatted string

        Args:
            entity_json_string (str): JSON formatted string

        Returns:
            Entity: Creates an Entity instance
        """
        attribute_list = list()
        entity_dict = json.loads(entity_json_string)
        for attribute in entity_dict['ATTRIBUTES']:
            # Create attribute objects and add to Entity
            new_attribute = Attribute.attribute_from_dict(attribute)
            attribute_list.append(new_attribute)
        return cls(name=entity_dict['ENTITY_NAME'], description=entity_dict['ENTITY_DESCRIPTION'],
                   subject_area=entity_dict['SUBJECT_AREA'], environment=entity_dict['ENVIRONMENT'],
                   attributes=attribute_list)

    def add_attribute(self, attribute: Attribute) -> None:
        """Adds an entity to the list of entities.

        Args:
            attribute (Attribute): An attribute to add to the list of attributes.
        """
        logging.info("Adding Attribute [%s] to Entity [%s] to list of source files for the dictionary...",
                     str(attribute.name), str(self.name))
        self.attributes.append(attribute)

    def get_entity(self):
        logging.info("Getting Entity")
        return self.name

    def get_entity_id(self) -> str:
        logging.info("Getting Entity id for [%s]", self.name)
        return self._entity_id


class DataDictionary:
    """An Attribute contains details about a data attribute/column including data type information.

        An Attribute contains details about a data attribute typically associated with entities.  The information generally includes details
        related to data type, masks and relationships to other data elements (e.g. parent-child, pk, fk, etc.).

        Args:
            name (str): A name for the data attribute.
            description (str): A description for the data attribute.
            subject_area (str): A subject area for the data attribute.
            environment (str): A environment for the data attribute.
            entities (list[Entity]): A list of attributes.
            source_filename (str): The full path to the file used as the source for this data dictionary

        Methods:
            add_source_file: Adds a source file to the list of source files processed to create this data dictionary
            add_entity: Adds an Entity to the list of Entities included in this data dictionary.
            write_data_dictionary: Writes the data dictionary to a file using JSON.
            create_data_dictionary_from_json: Creates a DataDictionary instance based on a JSON input file.

        TODO: Change entities to a dictionary with the "entity_id" as the key.  Add checks for existing entity when adding entity.
        TODO: Add registry to manage what entities have been created and what Attributes are part of that Entity

        Notes:
            _data_dictionary_registry = dict(DICTIONARY_NAME="Data Dictionary",
            )

    """

    _data_dictionary_registry = {}

    def __init__(
            self,
            name: str,
            description: str,
            subject_area: str,
            environment: str,
            source_filename: Path = None,
            entities: list[Entity] = None
    ) -> None:
        """

        Args:
            name (str): A name for the data attribute.
            description (str): A description for the data attribute.
            subject_area (str): A subject area for the data attribute.
            environment (str): A environment for the data attribute.
            entities (list[Entity]): (Optional) A list of attributes.
            source_filename (Path): (Optional) The full path to the file used as the source for this data dictionary
        """
        if len(name) == 0:
            raise NameError("Dictionary name must be provided")
        self.source_files = None
        self.name = name
        self.description = description
        self.subject_area = subject_area
        self.environment = environment
        if source_filename is None:
            self.source_files = list()
        else:
            self.add_source_file(source_filename)
        if entities is None:
            self.entity_count = 0
            self.entities = list()
        else:
            self.entity_count = len(entities)
            self.entities = list(entities)

    @classmethod
    def create_data_dictionary_from_json(cls, data_dictionary_source_file: Path) -> DataDictionary:
        """Creates an instance of DataDictionary based on a JSON File

        Creates an instance of DataDictionary based on a JSON File.  This includes creating Entity and Attribute objects.

        Args:
            data_dictionary_source_file (Path): The file system path to the Data Dictionary JSON File

        Returns:
            DataDictionary Class Object:
        """
        logging.info("Creating data dictionary object from [%s] source file", str(data_dictionary_source_file))
        with open(data_dictionary_source_file, 'r') as file:
            json_data = json.load(file)
        entity_list = list()
        for entity in json_data['ENTITIES']:
            logging.info("Creating entity in Data Dictionary: [%s]", str(entity['ENTITY_NAME']))
            new_entity = Entity.entity_from_dict(entity)
            entity_list.append(new_entity)
        logging.info("Creating DataDictionary object based on input file.")
        return cls(name=json_data['DICTIONARY_NAME'], description=json_data['DESCRIPTION'],
                   subject_area=json_data['DICTIONARY_NAME'], environment=json_data['ENVIRONMENT'],
                   entities=entity_list)

    def add_source_file(self, source_file: Path) -> None:
        """Adds a source file to the list of source files for the data dictionary

        Args:
            source_file (Path): The full path of the source file name to write data dictionary to
        """
        logging.info("Adding source file [%s] to list of source files for the dictionary...", str(source_file))
        if self.source_files is None:
            self.source_files = list()
        if source_file.is_file():
            self.source_files.append(source_file)
        else:
            logging.error("Not a valid file.")

    def add_entity(self, entity: Entity) -> None:
        """Adds an Entity to the list of entities.

        Args:
            entity (Entity): The Entity to be added to the data dictionary
        """
        logging.info("Adding Entity to dictionary [%s] to list of source files for the dictionary...", str(entity))
        # _data_dictionary_registry = dict()
        self.entities.append(entity)

    def write_data_dictionary(self, out_filename: Path) -> None:
        """Writes contents of full data dictionary to an JSON formatted file

        This includes writing Entities and Attributes into a JSON formatted file.

        Args:
            out_filename (Path): The full path of the output file name to write data dictionary to

        """
        logging.info("[%s ]Writing data dictionary to JSON output file [%s]...", str(__name__), str(out_filename))
        # build list of source files
        dd_source_files = list()
        for source_file in self.source_files:
            dd_source_files.append(str(source_file))
        entities_list = list()
        for entity in self.entities:
            entities_list.append(entity.to_dict())
        out_dictionary = dict(DICTIONARY_NAME=self.name,
                              DESCRIPTION=self.description,
                              DATE_GENERATED=datetime.now(),
                              ENVIRONMENT=self.environment,
                              SOURCE_FILES=dd_source_files,
                              ENTITIES=entities_list)
        # json_formatted_str = json.dumps(out_dictionary, default=json_serial, indent=2, separators=(',', ': '))
        # print(str(json_formatted_str))
        with open(out_filename, 'w') as json_out_handle:
            json.dump(out_dictionary, json_out_handle, indent=2, default=json_serial, separators=(',', ': '))

    def get_entities(self) -> list[Entity]:
        logging.info("Getting entities")
        return self.entities

    def get_entity(self, entity_name: str) -> Entity | None:
        """

        Args:
            entity_name (str):

        Returns:
            Entity: If entity exists in entity object, otherwise None
        """
        logging.info("Checking if entity exist in list of entities [%s]", str(entity_name))
        for entity in self.entities:
            if entity.name == entity_name:
                logging.info("Found entity in list of entities [%s]", str(entity_name))
                return entity
        # if no entity found, for loop exits
        logging.warning("Entity not found in list of entities [%s]", str(entity_name))
        return None

    def __str__(self):
        return_str = ""
        entity_string_format = "Entity {name} includes: {description}, subject area {subject_area}"
        try:
            return_str = "Data Dictionary {name} has {entity_count} entities".format(
                name=self.name,
                entity_count=self.entity_count
            )
        except Exception as e:
            logging.error("Could not print string for object [%s]", str(e))
        return return_str


class DataDictionarySourceSpreadsheet:
    """An Attribute contains details about a data attribute/column including data type information.

        An Attribute contains details about a data attribute typically associated with entities.  The information generally includes details
        related to data type, masks and relationships to other data elements (e.g. parent-child, pk, fk, etc.).

        Args:
            name (str): A name for the data attribute.
            description (str): A description for the data attribute.
            subject_area (str): A subject area for the data attribute.
            environment (str): A environment for the data attribute.
            entities (List[Entity]): A list of attributes.

    """

    def __init__(
            self,
            name: str,
            description: str,
            subject_area: str,
            environment: str,
            entities: List[Entity] = None
    ) -> None:
        logging.info("function [%s]: Creating Data Dictionary Object [%s]...", str(__name__), str(name))
        self.name = name
        self.description = description
        self.subject_area = subject_area
        self.environment = environment
        if entities is None:
            self.entity_count = 0
        else:
            self.entity_count = len(entities)

    def write_data_dictionary(self, out_filename: str) -> None:
        """Writes contents of data dictionary to an output file

        todo: details about output format options.

        Args:
            out_filename: The full path of the output file name to write data dictionary to

        """
        logging.info("function [%s]: Writing data dictionary out [%s]...", str(__name__), str(self))
        # try:
        #     with open(out_filename, 'w') as json_out_handle:
        #         json.dump(self.to_json(self), json_out_handle, default=datetime_default)
        # except Exception as err:
        #     logging.error("Could not create file for data dictionary [%s]", str(out_filename))

    def __str__(self):
        return_str = ""
        try:
            return_str = "Data Dictionary {name} has {entity_count} entities".format(name=self.name,
                                                                                     entity_count=self.entity_count
                                                                                     )
        except Exception as e:
            logging.error("Could not print string for object [%s]", str(e))
        return return_str

# if len(str(source_filename)) > 0:
#     # If the list of source files already exists, add to it, otherwise create the list
#     if source_filename.is_file():
#         self.source_files = list[source_filename]
#     else:
#         logging.error("Source file is not a valid file reference: [%s]", str(source_filename))
#         raise NameError(source_filename)
# else:
#     logging.info("Source file not provided")