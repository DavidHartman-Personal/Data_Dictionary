from mdutils.mdutils import MdUtils
from mdutils import Html
from pytablewriter import MarkdownTableWriter
import pytablewriter as ptw
import io


def create_md_table(markdownfile):
    """Adds Markdown table to markdown file

    Parameters
    ----------
    markdownfile : mdUtils Markdown file
        Object containing markdown file reference

    """

    writer = MarkdownTableWriter(
        table_name="example_table",
        headers=["int", "float", "str", "bool", "mix", "time"],
        value_matrix=[
            [0, 0.1, "dave", True, 0, "2017-01-01 03:04:05+0900"],
            [2, "-2.23", "foo", False, None, "2017-12-23 45:01:23+0900"],
            [3, 0, "bar", "true", "inf", "2017-03-03 33:44:55+0900"],
            [-10, -9.9, "", "FALSE", "nan", "2017-01-01 00:00:00+0900"],
        ],
    )
    writer.stream = io.StringIO()
    writer.write_table()
    markdownfile.new_paragraph(writer.stream.getvalue())

def main():
    mdFile = MdUtils(file_name='USAID-SCCT-Data-Dictionary', title='USAID SCCT Data Dictionary')

    mdFile.new_paragraph(
        "This page is the root/parent page for the Data Dictionary.  The table below contains the entities/tables "
        "that are described in these pages.  Each entity contains a link to a child page that provides details on the "
        "entities/tables include attributes/columns, data models, dependencies, etc. "
    )
    create_md_table(mdFile)
    # Create a table of contents
    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()


if __name__ == "__main__":
    main()