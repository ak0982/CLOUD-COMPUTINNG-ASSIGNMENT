
import operator

def readFile(filename):
    temp=[]

    for i in filename:
        
        for j in i.split():


            temp.append(j)
            #print(j)

    return temp


def wordCount(words):

    counts = dict()
    

    for word1 in words:

        if word1 in counts:
            counts[word1] += 1

        else:

            counts[word1] = 1

    return counts

def topTenWords(wordCountDict):
    sort = sorted(wordCountDict.items(), key=operator.itemgetter(1),reverse=True)

    #ict1 = OrderedDict(sorted(wordCountDict.())) 
    temp=0
    for i in sort:
        if temp <10:

            print(i)
            temp +=1
    return sort
'''

def ignorestopwords(temp):

    for i in temp:
        if i[0]!='hi':
            print(i)


'''


filename= open('sample.txt', 'r')
contents= readFile(filename)
#print(contents)
wordCountDict= wordCount(contents)
#print(wordCountDict)
temp=topTenWords(wordCountDict)

#ignorestopwords(temp)


