#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case.


fname = input("Enter file name: ")
fh = open(fname)
print("fh___", fh)
book = fh.read()
print("book___", book)
bookCAPITAL = book.upper()
bookCAPITALrstrip = bookCAPITAL.rstrip()
print(bookCAPITALrstrip)