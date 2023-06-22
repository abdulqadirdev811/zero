wordsList  = ["duel", "dule", "speed", "spede", "deul", "cars"]

def creteNgramVector(word):
    emptyList = [ 0 for i in range(0,22)]    
    ngramVectorsList = []
    for alphabet in word:
        index = ord(alphabet) - 97
        emptyList[index] += 1
         
    ngramVector = tuple(emptyList)
    return ngramVector


def classifyTheWords(wordsList):
    classDict = {}
    for i,word in enumerate(wordsList):
        ngramVector = creteNgramVector(word)

        if ngramVector not in classDict:
            classDict[ngramVector] = [word]
        else:
            classDict[ngramVector].append(word)  
    return(classDict)


#ngramVectorsList = creteNgramVectorsList(wordsList)
WordClassificationDict = classifyTheWords(wordsList)
query = "dule"
relevenCategory = WordClassificationDict[creteNgramVector(query)]
print(relevenCategory)