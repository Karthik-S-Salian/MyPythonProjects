file = input("Enter file name: ")
handle = None
try:
    handle = open(file)
except:
    print("File couldn't recognise")
    quit()

word = input("Enter the required word: ")
l_found = list()
l_count = 0

for line in handle:
    li = line.rstrip()
    l_count = l_count + 1
    if word in li.split():
        l_found.append(l_count)

print(l_found)
