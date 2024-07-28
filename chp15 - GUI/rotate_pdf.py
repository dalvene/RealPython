"""
Real Python Book 1 Chapter 15 - Graphical User Interface
Rotate PDF exercise
"""

from easygui import *
from pypdf import PdfReader, PdfWriter


def choose_input():
    # Let the user choose an input file
    input_file_name = fileopenbox("", "Select a PDF to rotate...", "*.pdf")
    if input_file_name is None:  # exit on "Cancel"
        exit()
    return input_file_name


def choose_rotation():
    # Let the user choose an amount of rotation
    rotate_choices = [90, 180, 270]
    message = "Rotate the PDF clockwise by how many degrees?"
    degrees = buttonbox(message, "Choose rotation...", rotate_choices)
    return degrees


def choose_output(input_file_name):
    # Let the user choose an output file
    output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")
    while input_file_name == output_file_name:  # Cannot use same file as input
        msgbox("Cannot overwrite original file!", "Please choose another file...")
        output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")
    if output_file_name is None:
        exit() # exit on "Cancel"
    return output_file_name


def rotate_pdf(input_file_name, degrees, output_file_name):
    # read in file, perform rotation, save out new file
    input_file = PdfReader(open(input_file_name, "rb"))
    output_PDF = PdfWriter()

    for page_num in range(input_file.get_num_pages()):
        page = input_file.get_page(page_num)
        page = page.rotate(int(degrees))
        output_PDF.add_page(page)

    output_file = open(output_file_name, "wb")
    output_PDF.write(output_file)
    output_file.close()


def main():
    # Enter main function here
    input_file_name = choose_input()
    degrees = choose_rotation()
    output_file_name = choose_output(input_file_name)
    rotate_pdf(input_file_name, degrees, output_file_name)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{(time.time() - start_time):.2f}---")