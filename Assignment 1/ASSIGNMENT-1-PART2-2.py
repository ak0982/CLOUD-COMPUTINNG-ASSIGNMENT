
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
    print('top ten word ')
    temp=0
    for i in sort:
        if temp <10:

            print(i)
            temp +=1
    return sort


def ignorestopwords(temp):
    
    #print(temp)
    count=0
    al=[]
    sw=[]
    print(type(temp))
    for i in temp:

        if i[0] =='hi' or i[0]=='the' or i[0]=='an' or i[0]=='to' or i[0]=='and' or i[0]=='of' or i[0]=='be' or i[0]=='as' or i[0]=='is' or i[0]=='or' or i[0]=='data':

            sw.append(i[0])

        else:
            if count < 10:

                al.append(i[0])
                count +=1

    return sw,al



        





filename= open('sample.txt', 'r')
contents= readFile(filename)
#print(contents)
wordCountDict= wordCount(contents)
#print(wordCountDict)
temp=topTenWords(wordCountDict)
print('top ren word without repeating word')
sw,al=ignorestopwords(temp)
print(al)

print('stop word')
print(sw)


