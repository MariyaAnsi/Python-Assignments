
#Write a programa to open the file words.txt and read data from file where specific line to end.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "words.txt"
emptylist = list()
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        splitline = line.split()
        print(splitline[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
