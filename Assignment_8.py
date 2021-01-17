#Write a program to read through the words.txt
#and figure out who has the sent the greatest number of mail messages.

name = input("Enter file:")
if len(name) < 1 : name = "words.txt"
handle = open(name)
x = 0
counts = dict()
for line in handle :
    if line.find ('From ') : continue
    x = x + 1
    line = line.split()
    mails = line[1]
    counts[mails] = counts.get(mails, 0) + 1
    print("mails", mails)


mostmails = None
prolificomitter = None
for sender,amount in counts.items():
    if mostmails is None or amount > mostmails:
        print("sender, amount", sender, amount)
        mostmails = amount
        prolificomitter = sender
print(prolificomitter, mostmails)