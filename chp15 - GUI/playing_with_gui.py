"""
Real Python Book 1 Chapter 15 - Graphical User Interface
Add GUI elements with EasyGUI
"""

from easygui import *


def boxes():
    # Enter a function here
    # msgbox("Hello, EasyGUI!", "This is a message box", "Hi there")
    choices = ["Blue", "Yellow", "Auuugh!"]
    title = "Choose wisely..."
    result = buttonbox("What is your favourite colour?", title, choices)
    print("Result: ", result)
    result = indexbox("What is your favourite colour?", title, choices)
    print("Result: ", result)
    result = choicebox("What is your favourite colour?", title, choices)
    print("Result: ", result)
    result = multchoicebox("What are your favourite colours?", title, choices)
    print("Result: ", result)
    result = enterbox("What is your favourite colour?", title)
    print("Result: ", result)
    result = passwordbox("What is your favourite colour? (I won't tell.)", title)
    print("Result: ", result)
    result = textbox("Please describe your favourite colour?")
    print("Result: ", result)


def main():
    # Enter main function here
    result = fileopenbox("message", "title", "*.txt")
    print("Result: ", result)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print(f"Runtime: ---{(time.time() - start_time):.2f}---")