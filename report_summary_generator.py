import glob
from argparse import ArgumentParser, Namespace
from typing import List

from docx import Document

"""
    How to run:
        
"""

DOCX_EXTENSION: str = ".docx"


def main() -> None:
    args = prepare_args()
    path: str = args.path
    file_paths: List[str] = glob.glob(f"{path}*{DOCX_EXTENSION}")

    for filepath in file_paths:
        print(filepath)

    document: Document = Document(file_paths[0])
    print([x.text for x in document.paragraphs if x.text == "Data:"])
    for paragraph in document.paragraphs:
        print(paragraph.text)


def prepare_args() -> Namespace:
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-p", "--path", type=str, required=True,
        help="Path do directory where reports are placed"
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
