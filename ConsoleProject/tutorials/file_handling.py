import os


text="""computer is an electronic device
motherboard is a main circuit board
intel amd different types of processors
hello world
"""

# opening file

def read_file():
    """ 
        MODES
    "r" read error if doesnot exits    // default 
    'a' append enters at last create if file doesnot exits
    'w'  write erase everything and rewrites create if file doesnot exits
    'x' create create new file error if exist
    
    # additional
    't' text mode    // default
    'b' binary (eg images)
    
    eg 'wt' -> write file in text mode
    """
    file = open("resources/test.txt", "r")
    print("file read = ",file.read(1))   # parameter no of char to read if not mentioned read whole file



#   VI //  READLINE FUNCTION READS NEXT FROM WHERE IT READ BEFORE

    print("\n file.readline()   ->  ", file.readline())   # reda first line
    print("\n file.readline(3)   ->  ",file.readline(5))  # reads of entered number of char from a line
    print("\n file.readlines()   ->   ",file.readlines())   # read lines separately
    file.close()

    file = open("resources/test.txt", "r")
    # READING ALL LINES
    for lines in file:
        print(lines)
    file.close()


def write_file():
    file = open("resources/test.txt", "w")
    file.write(text)
    file.close()

def create_file():
    if not os.path.exists("resources/test.txt"):  # check file exist or not
        open("resources/test.txt","x")

def delete_file():
    if os.path.exists("resources/test.txt"):   # check file exist or not
        os.remove("resources/test.txt")
    else:
        print("ERROR")

if __name__=="__main__":
    create_file()
    write_file()
    read_file()
    delete_file()
