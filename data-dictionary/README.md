# USAID SCCT - Data Dictionary

This page contains details regarding how data dictionaries are created and maintained. 

[TOC levels=2]: # "### Table of contents"

## Data Dictionary Files

Format and layout of files that are used to manage data dictionary information.  

* Logical Data Model
* Physical Data Model
* Entity/Attribute and Table/Column Details
* Data Lineage
* Data State Diagrams - Describes how data changes based on defined processes (e.g. Shippping/Order milestones)

## Creating Data Dictionary Confluence/Documentation Pages

Using Python Markdown utilities libraries, markdown pages can be automatically created.  The source of the information used to create the pages are source-to-target mappings.

The following information will be provided and used to create the documentation.

* Entity/Table - Entity/Table names along with description/purpose of entity/table
* Entity/Table and Attribute/Column - Table describing attributes/columns for tables along with data type, example and key information.
* Dependencies - Details regarding other attributes that are dependent on each column.  
* Traceability/Lineage - Provides complete data lineage and traceability for each attribute (forwards and backwards) 
* Data Model - A data model for each subject area will be included 

A main markdown page will be created that includes the list of all entities/tables included in child pages.

Starting/Main page
- List of Entities along with descriptions in a table that include links to child pages that provide attribute details.   

Create data dictionary using Pandas data frame.

```python
import pandas as pd

def create_data_dictionary(df):
    """
    Creates a data dictionary for a given Pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.

    Returns:
        pd.DataFrame: A DataFrame containing the data dictionary.
    """

    data_dict = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Non-Null Count': df.count(),
        'Unique Values': df.nunique(),
        'Sample Values': [df[col].unique()[:3] for col in df.columns]
    })

    return data_dict

# Example usage:
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

data_dictionary = create_data_dictionary(df)
print(data_dictionary)
```