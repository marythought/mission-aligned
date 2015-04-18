# Tweet it!

with open('workfile.txt', "r") as f:
    lines = f.readlines()

for x in range(101):
    if len(lines[x]) > 140:
        print "too long"
    else:
        print "all good"
