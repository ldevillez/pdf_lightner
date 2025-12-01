"""
Manage the CLI and ligthen the pdf
"""

import click
import pymupdf # imports the pymupdf library


__version__ = "0.2.0"
__author__ = "Devillez Louis"
__maintainer__ = "Devillez Louis"
__email__ = "louis.devillez@gmail.com"

@click.command()
@click.help_option("-h", "--help")
@click.argument("input_file",type=click.Path(exists=True))
def lighten(input_file: str) -> None:
    """
    Take an input pdf and ligthen some of the annotations
    """
    doc = pymupdf.open(input_file) # open a document

    number = 0
    number_modified = 0
    for page in doc: # iterate the document pages
        annots = page.annot_names()
        number += len(annots)
        for annot in annots:
            obj_annot = page.load_annot(annot)
            if obj_annot.type[1] in ["Caret", "Highlight"] :
                number_modified += 1
                cols = obj_annot.colors
                stroke = cols["stroke"]
                sum_stroke = stroke[0] + stroke[1] + stroke[2]

                if sum_stroke > 1.5:
                    continue

                diff = 1.5 - sum_stroke
                for i in range(3):
                    cols["stroke"][i] += diff
                    if cols["stroke"][i] > 1:
                        cols["stroke"][i] = 1
                obj_annot.set_colors(cols)
                obj_annot.update()

    percent_modified = 100 * number_modified / number
    print(f"Number of annotation modified: {number_modified}/{number} ({percent_modified:.2f}%)")

    output_file = input_file.replace(".pdf", "_lighten.pdf")
    doc.save(output_file)

@click.group()
@click.version_option(__version__, "-v", "--version")
@click.help_option("-h", "--help")
def cli() -> None:
    """
    To make annotation in pdf more readable
    """

cli.add_command(lighten)


if __name__ == "__main__":
    cli()
