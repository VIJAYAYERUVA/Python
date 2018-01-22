import itertools

filepath = '/home/bigdata/PycharmProjects/LDA/PyLDA/pubmed_bioontology/data/PreLresults.txt'


# convert the data into list
def read_words(words_file):
    with open(words_file, 'r') as f:
        return list(itertools.chain.from_iterable(line.split("\n") for line in f))


mylist = read_words(filepath)

# covert all list of elements to lower case
lowercaselist = []
for x in mylist:
    y = x.lower()
    lowercaselist.append(y)

# get only unique values from above list
uniqueoutput = []
for x in lowercaselist:
    if x not in uniqueoutput:
        uniqueoutput.append(x)

# sort the unique output

# convert the sorted output to string
output = '\n'.join(uniqueoutput)

# write the output to file
f = open("data/unique.txt", "a+")
f.write("%s" % output)
f.close()
