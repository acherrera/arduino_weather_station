
import tkinter as tk
from tkinter import filedialog

def menu_maker(in_list):
    """
    in_list is of the form [(prompt1, output1),
                            (prompt2, output2),
                            ...]
    """
    exit = False
    while not exit:
        print("\n\n")
        n = 1
        for item in in_list:
            print("{}. \t {}".format(n, item[0]))
            n += 1
        user_selection = input("Please enter a number: ")
        try:
            user_selection = int(user_selection) - 1
            if user_selection in range(len(in_list)):
                user_output = in_list[user_selection][1]
                exit = True
            else:
                print("Please enter a valid number")
        except:
            print("Please enter a valid number")
    return user_output

def GUI_file_selector():
    # File location from user using pretty GUI
    # returns full file path
    root = tk.Tk()                      # make it
    root.withdraw()                     # how to
    raw_path = filedialog.askopenfile() # what to
    root.destroy()                      # get rid of

    # This is needed to make the file path work correctly
    file_path = raw_path.name

    return file_path

