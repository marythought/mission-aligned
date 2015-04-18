# Tweet it!

with open('workfile.txt', "r") as f:
    lines = f.readlines()

# Test to see how many lines are too long to tweet

for x in range(101):
    if len(lines[x]) > 140:
        print "too long"
    else:
        print "all good"

# Import code from previous python bot that uses tweepy to
# read and tweet random line. Add a "try" line to test for tweet-length?
