#set_options.py will print and handle options based on filesystem type
import os

def read_params():
    filesystem_type = open("/usr/tmp/iKnowdeDiscovery/ext_type", "r")
    ext_option = filesystem_type.readline()
    filesystem_path = open("/usr/tmp/iKnowdeDiscovery/user_path", "r")
    filesystempath = filesystem_path.readline()
    filesystem_path.close()


    if ext_option == "EXT2":
        ext_2()
    elif ext_option == "EXT3":
        ext_3()
    elif ext_option == "EXT4":
        ext_4()
    else:
        print("[ERROR]  NO OPTIONS AVAILABLE")
        print("--- P R O G R A M --- T E R M I N A T I N G ---")
        os.system("./print_line.sh")
    filesystem_type.close()

def ext_2_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def ext_3_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def ext_4_print():
    print("(1) Hardlink Visualizer")
    print("(2) xxx")
    print("(3) xxx")
    print("(4) xxx")
    print("(5) xxx")

def ext_2():
    ext_2_print()
    userInput = input("[PROMPT] Enter an option: ")
    print("You entered: " + userInput)
    userInput2 = input("Is that correct? [Y(y)/N(n)]")
    if (userInput2 == "Y" or userInput2 == "y"):
        os.system("./enumeration.sh "+filesystempath)
    else:
        os.system("./print_line.sh")
        ext_2()
def ext_3():
    print(" OPTIONS for EXT 3 will go here")

   # os.system("./option_ext3.sh")
def ext_4():
    userInput = input("[PROMPT] Enter an option: ")
    print("You entered: " + str(userInput))
    userInput2 = input("Is that correct? [Y(y)/N(n)]")
    if (userInput2 == "Y" or userInput2 == "y"):
        os.system("./enumeration.sh " + str(filesystempath))
    else:
        os.system("./print_line.sh")
        ext_4()

   # os.system("./option_ext4.sh")
   # os.system("./option_ext4.sh")

read_params()