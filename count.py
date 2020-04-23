import os
# Get the full path of current folder
getFolder = os.path.dirname(os.path.abspath(__file__))
# use join to get full path of txt file
mainFile = os.path.join(getFolder, 'sample.txt')

# open txt file
file = open(mainFile)
# with read we can read our txt file
# if it is necesarry use replace()
line = file.read()
file.close()

# use blank(" ") as a reference and split words 
splitWords = line.split()
allWords={}
for word in splitWords:
    if word not in allWords:
        allWords[word] = 1
    else:
        allWords[word] += 1

#*.keys() returns the all keys of list 
for key in allWords.keys():
   print ("Word: %s =>%s " %(key , allWords[key]))
