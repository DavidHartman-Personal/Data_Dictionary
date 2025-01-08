"""This script is used to create various types of output files based on data in the Data Dictionary\

This script contains functions that are used to create markdown files.  It has methods that can be used to create the
various types of Markdown content as needed.

This file can also be imported as a module and contains the following functions:

    * create_markdown_file - Creates a markdown file
    * main - the main function of the script
"""

from mdutils.mdutils import MdUtils
from mdutils import Html
from pathlib import Path
import logging
import coloredlogs

coloredlogs.install(level=logging.DEBUG,
                    fmt="%(asctime)s %(hostname)s %(name)s %(filename)s line-%(lineno)d %(levelname)s - %(message)s",
                    datefmt='%H:%M:%S')

PYCHARM_ROOT_DIR = Path(__file__).parents[2].resolve()
"""This is the make directory containing all Python projects"""

PROJECT_ROOT_DIR = Path(__file__).parents[1].resolve()
"""The make Project root directory
NOTE: This assumes that this file is contained within a directory within the Project
"""

MARKDOWN_FILE_DIR = PROJECT_ROOT_DIR / "output_files"
"""Output directory where generated markdown files are stored"""


def add_code_section(md_file: MdUtils, code: str, language: str = "python") -> None:
    """Add a code section to a markdown file

    Args:
        md_file (MdUtils): MdUtils object
        code (str): Code string to add to markdown section
        language (str): Language to add to markdown section

    """
    md_file.insert_code(code, language=language)
    # "import Mdutils\n"
    #                        "\n"
    #                        "\n"
    #                        "md_file = MdUtils(file_name=\'Example_Markdown\',title=\'Markdown File Example\')\n"
    #                        "md_file.create_md_file()"


def add_paragraph(md_file: MdUtils, paragraph_text: str) -> None:
    """Add a code section to a markdown file

    Args:
        md_file (MdUtils): MdUtils object
        paragraph_text (str): The paragraph text to add.

    """
    return_string = ""
    md_file.new_paragraph("``create_md_file()`` is the last command that has to be called.")
    # Adding a paragraph with some formatting added (e.g. bold, purple)
    md_file.new_paragraph("This is an example of text in which has been added color, bold and italics text.",
                          bold_italics_code='bi', color='purple')


def add_using_write_method(md_file: MdUtils, paragraph_text: str) -> None:
    """Add a code section to a markdown file

    Args:
        md_file (MdUtils): MdUtils object
        paragraph_text (str): The paragraph text to add.

    """
    md_file.write('  \n')
    md_file.write('bold_italics_code', bold_italics_code='bic')
    md_file.write('  \n')
    md_file.write('Text color', color='green')
    md_file.write('  \n')
    md_file.write('Align Text to center', align='center')


def add_toc(md_file: MdUtils) -> None:
    """Add a code section to a markdown file

    Args:
        md_file (MdUtils): MdUtils object

    """
    # This adds a TOC to a level of 2.  This can be called just before the call to create the file)
    md_file.new_table_of_contents(table_title='Contents', depth=2)


def create_table(md_file: MdUtils, table_data: []) -> None:
    """Add a code section to a markdown file

    Args:
        table_data: A 2D array (array of arrays) that contains the row data.
        md_file (MdUtils): MdUtils object

    NOTE:
         Example of creating the array data:
         list_of_strings = ["Items", "Descriptions", "Data"]
         for x in range(5):
            list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
         md_file.new_line()
         md_file.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')
    """
    # This adds a TOC to a level of 2.  This can be called just before the call to create the file)
    list_of_strings = ["Items", "Descriptions", "Data"]
    for x in range(5):
        list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
    md_file.new_line()
    md_file.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')
    md_file.new_table_of_contents(table_title='Contents', depth=2)


def create_table_data(md_file: MdUtils, table_data: []) -> []:
    """Creates an array of arrays that can be passed to new_table to create a Markdown table.

    This method contains code that creates an example data set for a table that will have 3 columns
    and 6 rows.

    Args:
        table_data ([]): The array to create
        md_file (MdUtils): MdUtils object

    Returns:
        Array: The 2D array that contains table data.

    """
    list_of_strings = ["Items", "Descriptions", "Data"]
    for x in range(5):
        list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
    return list_of_strings


def create_link(md_file: MdUtils) -> None:
    """Creating links in Markdown files.

    ``new_inline_link`` method allows you to create a link of the style: ``[mdutils](https://github.com/didix21/mdutils)``.
    Reference link adds a reference at the bottom of the Markdown file and then uses the reference link format.
    md_file.write('\n  - Reference link: ' + md_file.new_reference_link(link='https://github.com/didix21/mdutils', text='mdutils', reference_tag='1')


    Args:
        md_file (MdUtils): MdUtils object

    """
    # This adds a TOC to a level of 2.  This can be called just before the call to create the file)
    md_file.new_table_of_contents(table_title='Contents', depth=2)


def create_list(md_file: MdUtils) -> None:
    """Creating various types of lists in a Markdown file.

    Unordered list that contains multiple levels
    This function takes an array of items to be added to the list.
    If the list has level, the "header" for the parent level is added followed by an array of items that would be
    included in the indented level.
    items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', ['Item 4.1', 'Item 4.2', ['Item 4.2.1', 'Item 4.2.2'], 'Item 4.3', ['Item 4.3.1']], 'Item 5']
    md_file.new_list(items)
    The resulting output would look as follows:
    - Item 1
    - Item 2
    - Item 3
    - Item 4
        - Item 4.1
        - Item 4.2
            - Item 4.2.1
            - Item 4.2.2
        - Item 4.3
        - Item 4.3.1
        - Item 5


    Args:
        md_file (MdUtils): MdUtils object

    """
    # This adds a TOC to a level of 2.  This can be called just before the call to create the file)
    md_file.new_table_of_contents(table_title='Contents', depth=2)


def add_image(md_file: MdUtils, image_text: str, image_link: str) -> None:
    """Creating links in Markdown files.

    md_file.new_line(md_file.new_inline_image(text='snow trees', path='./doc/source/images/photo-of-snow-covered-trees.jpg'))
    Image created using a reference link.
    md_file.new_line(md_file.new_reference_image(text='snow trees', path='./doc/source/images/photo-of-snow-covered-trees.jpg', reference_tag='im'))

    Args:
        image_link: URL/File location for link
        image_text: Text to show for the link in the markdown file.
        md_file (MdUtils): MdUtils object

    """
    # This adds a TOC to a level of 2.  This can be called just before the call to create the file)
    md_file.new_line(
        md_file.new_inline_image(text=image_text, path=image_link))


def create_markdown_file(file_path: Path = MARKDOWN_FILE_DIR / "full_example.md", force_overwrite=False):
    """Gets and prints the spreadsheet's header columns

    Longer function header comment describing details/purpose of the function.
    This file uses numpy style docstrings

    Parameters:
      force_overwrite (bool): (default=False) This forces to overwrite of a file if it already exists
      file_path (Path): The full file path of the file to be created.

    Returns
      None

    Raises
      FileExistsError: Will not create file if it already exists
    """

    if Path(file_path).exists() and not force_overwrite:
        logging.error("File already exists and force_overwrite set to False: [%s]", file_path)
        raise FileExistsError
    else:
        md_file = MdUtils(file_name=str(file_path), title='Markdown File Example')
        """Creates a md object used to create a markdown file.  The file_name can be a Path object
        The title becomes the Level 1/header (#) of the page.
        """

    md_file.new_header(level=1, title='Overview')  # style is set 'atx' format by default.

    md_file.new_header(level=2, title="Create Markdown files")
    add_paragraph(md_file, "Adding text")
    md_file.new_table_of_contents(table_title='Contents', depth=2)
    md_file.create_md_file()


def main():
    logging.info("PYCHARM_ROOT_DIR: [%s]", PYCHARM_ROOT_DIR)
    logging.info("PROJECT_ROOT_DIR: [%s]", PROJECT_ROOT_DIR)
    logging.info("MARKDOWN_FILE_DIR: [%s]", MARKDOWN_FILE_DIR)
    logging.info("Creating markdown file: [%s]", MARKDOWN_FILE_DIR / "example.md")
    create_markdown_file(MARKDOWN_FILE_DIR / "example.md", force_overwrite=True)


if __name__ == "__main__":
    main()
