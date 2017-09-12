wordstring = 'This is python class. This is easy'
# wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

v = list(zip(wordlist,wordfreq))
print(v)

print("String: " + wordstring + "\n")
print("List: " + str(wordlist) + "\n")
print("Frequencies: " + str(wordfreq) + "\n")
print("Pairs: " + list(zip(wordlist, wordfreq)))
