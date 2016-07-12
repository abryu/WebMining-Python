
import os # import os for reading source files
import re # import re (regular expression) for checking strings 
          # to see if they match certain patterns
from nltk.corpus import stopwords # import and download from nltk.corpus for checking and removeing stopwords
from nltk import PorterStemmer # import PorterStemmer for stemming a single word

trainingPathForCourse = '/train/course'
trainingPathForFaculty = '/train/faculty'
trainingPathForStudent = '/train/student'

# dictionaries for storing result
storingTrainingSetForCourse = {}
storingTrainingSetForFaculty = {}
storingTrainingSetForStudent = {}

intersectionWords = []
def calculateWordsAppearInAll(r1,r2,r3,fileName):
    
    file4Intersection = open(fileName,'w')
    file4Intersection.write('<!DOCTYPE html><html><body><table>\
    <tr><th>Word</th></tr>')
    s1 = set([(eachTuple[0]) for eachTuple in r1])
    s2 = set([(eachTuple[0]) for eachTuple in r2])
    s3 = set([(eachTuple[0]) for eachTuple in r3])
   # return len(s1&s2),len(s1-s2)
    for word in s1&s2&s3:
        file4Intersection.write("<tr><td>"+word+"</td></tr>")
        intersectionWords.append(word)
    file4Intersection.write('</table></body></html>')
    file4Intersection.close()
    return intersectionWords

def uniquelyAppear(l1,l2): 
    s1 = set([(eachTuple[0]) for eachTuple in l1])
    s2 = set([(eachTuple[0]) for eachTuple in l2])
    return s1-s2
    
def writeUnique(filename,uList):
    fileN = open(filename,'w')
    fileN.write('<!DOCTYPE html><html><body><table>\
    <tr><th>Word</th></tr>')
    for word in uList:
        fileN.write("<tr><td>"+word+"</td></tr>")
    fileN.write('</table></body></html>')
    fileN.close()
    return uList
    
    
def writeResultToFile(resultDict, destFile, intersectionSet):
    interWords = intersectionSet
    resultDict.pop("comput", None)
    resultDict.pop("scienc", None)
    
    print (len(interWords))
    
    for wordKey in resultDict.keys():
        if resultDict.get(wordKey) <= 3:
            resultDict.pop(wordKey,None)
            
    if len(interWords) != 0:
        for word in interWords:
            print (word)
            resultDict.pop(word,None)
            
        resultList= sorted(resultDict.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)
    
        count = 1    
        for eachTuple in resultList:
            destFile.write('<tr><td>'+eachTuple[0]+'</td><td>'+str(eachTuple[1])+'</td></tr>')
        
            if count == 200:
                destFile.write('<tr><td>Above is the top 200 most frequent words</td></tr>')
            count = count + 1
        
        destFile.write('<tr><td>There are totally '+str(count)+' words be identified</td></tr>')
    else:          
        resultList= sorted(resultDict.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)

    return resultList
    

def removeUnnecessaryCharacters(word):
    if '@' in word or 'www' in word: # eliminate email addresses and website addresses
        return None
    newWord = "".join(re.findall("[a-zA-Z]+", word)).lower() # contain only characters
    if len(newWord) > 2 and len(newWord) < 15:            
        return newWord
    else:
        return None

def storeToResultDict(word,resultDict):
    if resultDict.has_key(word): #this word exists, update the value =+ 1
        resultDict[word] = resultDict.get(word)+1
    else: # this word doesnt exist, add this word as a key and value = 1
        resultDict[word] = 1
    
def formatAndPrintResultDict(resultDict,destFile,rFile):
    resultList= sorted(resultDict.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)
    count = 1    
    for eachTuple in resultList:
        destFile.write('<tr><td>'+eachTuple[0]+'</td><td>'+str(eachTuple[1])+'</td></tr>')
        if count <= 200:
            rFile.write(eachTuple[0]+'    ('+str(eachTuple[1])+'),\n')
        if count == 200:
            destFile.write('<tr><td>Above is the top 200 most frequent words</td></tr>')
            rFile.write('Above is the top 200 most frequent words\n')
        count = count + 1
        
    destFile.write('<tr><td>There are totally '+str(count)+' words be identified</td></tr>')
    rFile.write('There are totally '+str(count)+' words be identified.\n')
    return resultList

def openAndProcessingFiles(path,resultDict):  # Main Function

    for filename in os.listdir(os.getcwd()+path):

        thisFile = open(os.getcwd()+path+'/'+filename,'r') #open the file and process each file
        
        currentTextString = " ".join(thisFile.read().split())#store the file as a string for removing HTML tags
        
        textAfterHtmlRemovingString = re.sub('<[^>]*>', '', currentTextString) # remove HTML tags (String)
        
        textAfterHtmlRemovingList = textAfterHtmlRemovingString.split() # convert String to List for the text contains only characters
        
        textRemoveingUnnecessaryCharactersList = [removeUnnecessaryCharacters(word) for word in textAfterHtmlRemovingList ] 

        textRemoveingUnnecessaryCharactersList = [word for word in textRemoveingUnnecessaryCharactersList if word is not None]
        
        stop_words = set(stopwords.words('english'))
        
        stop_words.update(['texthtml', 'html', 'server', "email", 'date', 'gmt', 'www', 'page', 'comput']) # By analying the previous result set, continully adding new stopwords
                                                                                    # *********************
        textAfterStopwordsRemovingList = [word for word in textRemoveingUnnecessaryCharactersList if word not in stop_words] #remove stopwords

        stemmer = PorterStemmer() #stemming
        
        for eachWord in textAfterStopwordsRemovingList:
            eachWord = stemmer.stem(eachWord)
            storeToResultDict(eachWord,resultDict)
    
        thisFile.close()
        
f4Course = open('courseResult.html','w') #create and write to a file for storing Training set results
f4Falculty = open('falcultyResult.html','w') #create and write to a file for storing Test set results
f4Student = open('studentResult.html','w')

f4Course.write('<!DOCTYPE html><html><body><table>\
    <tr><th>Word List</th><th>Frequency</th></tr>') #write the header to the destination file
f4Falculty.write('<!DOCTYPE html><html><body><table>\
    <tr><th>Word List</th><th>Frequency</th></tr>') #write the header to the destination file
f4Student.write('<!DOCTYPE html><html><body><table>\
    <tr><th>Word List</th><th>Frequency</th></tr>') #write the header to the destination file

openAndProcessingFiles(trainingPathForCourse,storingTrainingSetForCourse)
openAndProcessingFiles(trainingPathForFaculty,storingTrainingSetForFaculty)
openAndProcessingFiles(trainingPathForStudent,storingTrainingSetForStudent)

calculateWordsAppearInAll(writeResultToFile(storingTrainingSetForCourse,f4Course,[]),writeResultToFile(storingTrainingSetForFaculty,f4Falculty,[]),writeResultToFile(storingTrainingSetForStudent,f4Student,[]),"intersection.html")

dC = writeResultToFile(storingTrainingSetForCourse,f4Course,intersectionWords)
dF = writeResultToFile(storingTrainingSetForFaculty,f4Falculty,intersectionWords)
dS = writeResultToFile(storingTrainingSetForStudent,f4Student,intersectionWords)

uC = uniquelyAppear(dC,dF) & uniquelyAppear(dC,dS)
uF = uniquelyAppear(dF,dC) & uniquelyAppear(dF,dS)
uS = uniquelyAppear(dS,dC) & uniquelyAppear(dS,dF)

writeUnique("uC.html",uC)
writeUnique("uF.html",uF)
writeUnique("uS.html",uS)

f4Course.write('</table></body></html>') # End of the file, write the close tags
f4Course.close()
f4Falculty.write('</table></body></html>') # End of the file, write the close tags
f4Falculty.close()
f4Student.write('</table></body></html>') # End of the file, write the close tags
f4Student.close()


print ("END PROCESSING")