"""
Real Python Book 1 Chapter 11 - Interact with PDF Files.
"""
import os
from pypdf import PdfReader


def read_pdf(file_path):
    # Enter a function here
    input_file_name = os.path.join(file_path, "Pride and Prejudice.pdf")
    input_file = PdfReader(open(input_file_name, "rb"))

    output_file_name = os.path.join(file_path, "Pride and Prejudice.txt")
    output_file = open(output_file_name, "w")

    total_pages = len(input_file.pages)
    print("Number of pages: ", total_pages)
    print("Metadata:", input_file.metadata)
    title = input_file.metadata["/Title"]
    print("Title:", title)

    output_file.write(title + "\n")
    output_file.write("Number of pages: {}\n\n".format(total_pages))

    for page_num in range(total_pages):
        text = input_file.get_page(page_num).extract_text()
        output_file.write(text)

    output_file.close()


def main():
    # Enter main function here
    my_path = ("C:/Users/Q/Dropbox/Recurrent Commitments/Growth and "
               "Learning/Python/RealPython/book1-exercises-master/chp11/practice_files")
    read_pdf(my_path)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{round(time.time() - start_time, 2)}---")
