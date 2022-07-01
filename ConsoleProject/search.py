import os

file = input("Enter file name: ")

if os.path.exists(file):
    with open(file) as f_handle:
        word = input("Enter the required word: ")
        line_found=list()
        l_count = 0

        for line in f_handle:
            li = line.rstrip()
            l_count = l_count + 1
            if word in li.split():
                line_found.append(l_count)
        print(l_count)
else:
    print("file doesnot exist")




