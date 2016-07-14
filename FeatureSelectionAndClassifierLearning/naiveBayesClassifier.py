###########################################################################################
# Thought For Naive Bayes Classifer

# Prior probability has been calculated in getStat.py

# Steps:

# 1. For Training, get frequent words's frequency in each training set.

# 2. Tokenize the test sets documents. Get their most frequent words. Relate those words frequency in training set.

# 3. Use the formula to classify them.

# 4. Test accuracy.

###########################################################################################
# IMPLEMENTATION:
# 0. Get files statistics

# 1. Rewrite v1.py. Get the frequency of the top 100 most frequent words in each train sets.

# 2. Tokenize the test sets documents. Get their most frequent words. Relate those words frequency in training set.

# 3. Loop the directories and execute files. Add result to an dictionary and test.

###########################################################################################
import sys

numberOfTopMostFrequentWordTrain = int(sys.argv[1])
numberOfTopMostFrequentWordTest = int(sys.argv[2])

#print numberOfTopMostFrequentWordTrain,numberOfTopMostFrequentWordTest
# 0. Get files statistics
import subprocess 

pathList = []
directoryInfo = {}
probInfo = {}

pathList.append('train/course')
pathList.append('train/faculty')
pathList.append('train/student')

pathList.append('test/course')
pathList.append('test/faculty')
pathList.append('test/student')

for filePath in pathList:
    p1 = subprocess.Popen(('ls',filePath), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(('wc','-l'), stdin=p1.stdout, stdout=subprocess.PIPE)
    directoryInfo[filePath] = int(filter(str.isdigit, str(p2.communicate())))

#for key, value in directoryInfo.iteritems():
#    print key, value

total4Test = directoryInfo.get("test/student") + directoryInfo.get("test/course") + directoryInfo.get("test/faculty")
total4Train = directoryInfo.get("train/student") + directoryInfo.get("train/course") + directoryInfo.get("train/faculty")

prob4TrainStudent = float(directoryInfo.get("train/student"))/float(total4Train)
prob4TrainCourse = float(directoryInfo.get("train/course"))/float(total4Train)
prob4TrainFaculty = float(directoryInfo.get("train/faculty"))/float(total4Train)

probInfo["student"] = prob4TrainStudent
probInfo["course"] = prob4TrainCourse
probInfo["faculty"] = prob4TrainFaculty

#for key, value in probInfo.iteritems():
    #print key, value
print "************************************************"
prob4TestStudent = float(directoryInfo.get("test/student"))/float(total4Test)
prob4TestCourse = float(directoryInfo.get("test/course"))/float(total4Test)
prob4TestFaculty = float(directoryInfo.get("test/faculty"))/float(total4Test)

probInfo["studentTest"] = prob4TestStudent
probInfo["courseTest"] = prob4TestCourse
probInfo["facultyTest"] = prob4TestFaculty
###########################################################################################

# Part 1. Rewrite v1.py. Get the frequency of the top most frequent words in each train sets.

import os # import os for reading source files
import re # import re (regular expression) for checking strings 
          # to see if they match certain patterns
from nltk.corpus import stopwords # import and download from nltk.corpus for checking and removeing stopwords
from nltk import PorterStemmer # import PorterStemmer for stemming a single word

trainPathForCourse = '/train/course'
trainPathForFaculty = '/train/faculty'
trainPathForStudent = '/train/student'

# dictionary for storing result
wordWithFrequency4TrainStudent = {}
wordWithFrequency4TrainCourse = {}
wordWithFrequency4TrainFaculty = {}

# Final result for part 1
wordWithProb4TrainStudent = {}
wordWithProb4TrainCourse = {}
wordWithProb4TrainFaculty = {}

def openAndProcessingFiles(path,resultDict):  # Main Function
    for filename in os.listdir(os.getcwd()+path):
        thisFile = open(os.getcwd()+path+'/'+filename,'r') #open the file and process each file
        currentTextString = " ".join(thisFile.read().split())#store the file as a string for removing HTML tags
        textAfterHtmlRemovingString = re.sub('<[^>]*>', '', currentTextString) # remove HTML tags (String)    
        textAfterHtmlRemovingList = textAfterHtmlRemovingString.split() # convert String to List for the text contains only characters
        textRemoveingUnnecessaryCharactersList = [removeUnnecessaryCharacters(word) for word in textAfterHtmlRemovingList ] 
        textRemoveingUnnecessaryCharactersList = [word for word in textRemoveingUnnecessaryCharactersList if word is not None]       
        stop_words = set(stopwords.words('english'))     
        stop_words.update(['texthtml', 'html', 'server', "email", 'date', 'gmt', 'www']) # By analying the previous result set, continully adding new stopwords   
        textAfterStopwordsRemovingList = [word for word in textRemoveingUnnecessaryCharactersList if word not in stop_words] #remove stopwords
        stemmer = PorterStemmer() #stemming        
        for eachWord in textAfterStopwordsRemovingList:
            eachWord = stemmer.stem(eachWord)
            storeToResultDict(eachWord,resultDict)

# Note: Bad for code usability and maintainence

def storeToResultDict(word,resultDict):
    if resultDict.has_key(word): #this word exists, update the value =+ 1
        resultDict[word] = resultDict.get(word)+1
    else: # this word doesnt exist, add this word as a key and value = 1
        resultDict[word] = 1

def removeUnnecessaryCharacters(word):
    if '@' in word or 'www' in word: # eliminate email addresses and website addresses
        return None
    newWord = "".join(re.findall("[a-zA-Z]+", word)).lower() # contain only characters
    if len(newWord) > 2 and len(newWord) < 15:            
        return newWord
    else:
        return None

def processDictionary(resultDict,processedDic,wordsToRemove):
#def processDictionary(resultDict,processedDic):
    for word in wordsToRemove:
        resultDict.pop(word)  
    resultList= sorted(resultDict.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)
    totalNumberOfWordsAppear = 0
    resultList = resultList[:numberOfTopMostFrequentWordTrain] # the top 100 most frequent words    
    for eachTuple in resultList:
        totalNumberOfWordsAppear = totalNumberOfWordsAppear + eachTuple[1]
    for eachTuple in resultList:
        processedDic[eachTuple[0]] = float(eachTuple[1]) / float(totalNumberOfWordsAppear) * 10
  #  for key,value in processedDic.iteritems():
  #      print key,value
  #  print sorted(processedDic.values())

def getWordsAppearAllSets(d1,d2,d3): # Becuse words appera in all sets  are less indicative (useless)
    s1 = set(d1.keys())             # So we remove them
    s2 = set(d2.keys())
    s3 = set(d3.keys())
    placeHolderList = list()
    for word in s1&s2&s3:
        placeHolderList.append(word)
    return placeHolderList

openAndProcessingFiles(trainPathForCourse,wordWithFrequency4TrainCourse)
openAndProcessingFiles(trainPathForFaculty,wordWithFrequency4TrainFaculty)
openAndProcessingFiles(trainPathForStudent,wordWithFrequency4TrainStudent)

commonWordsList = getWordsAppearAllSets(wordWithFrequency4TrainStudent,wordWithFrequency4TrainCourse,wordWithFrequency4TrainFaculty)

processDictionary(wordWithFrequency4TrainStudent,wordWithProb4TrainStudent,commonWordsList)
processDictionary(wordWithFrequency4TrainCourse,wordWithProb4TrainCourse,commonWordsList)
processDictionary(wordWithFrequency4TrainFaculty,wordWithProb4TrainFaculty,commonWordsList)

#processDictionary(wordWithFrequency4TrainStudent,wordWithProb4TrainStudent)
#processDictionary(wordWithFrequency4TrainCourse,wordWithProb4TrainCourse)
#processDictionary(wordWithFrequency4TrainFaculty,wordWithProb4TrainFaculty)

###########################################################################################
# 2. Tokenize the test sets documents. Get their most frequent words. Relate those words frequency in training set.

import operator

testPathForCourse = '/test/course'
testPathForFaculty = '/test/faculty'
testPathForStudent = '/test/student'

numOfDocumentsInCourse = 0
numOfDocumentsInFaculty = 0
numOfDocumentsInStudent = 0

courseList = []
facultyList = []
studentList = []

def tokenizeAndGetMostFrequentyWords(fileToProcess): # top 20 frequent words. Same procedure as processing the train set
    wordDictionary = {}
    thisFile = open(fileToProcess,'r') #open the file and process each file
    currentTextString = " ".join(thisFile.read().split())#store the file as a string for removing HTML tags
    textAfterHtmlRemovingString = re.sub('<[^>]*>', '', currentTextString) # remove HTML tags (String)    
    textAfterHtmlRemovingList = textAfterHtmlRemovingString.split() # convert String to List for the text contains only characters
    textRemoveingUnnecessaryCharactersList = [removeUnnecessaryCharacters(word) for word in textAfterHtmlRemovingList ] 
    textRemoveingUnnecessaryCharactersList = [word for word in textRemoveingUnnecessaryCharactersList if word is not None]       
    stop_words = set(stopwords.words('english'))     
    stop_words.update(['texthtml', 'html', 'server', "email", 'date', 'gmt', 'www']) # By analying the previous result set, continully adding new stopwords   
    textAfterStopwordsRemovingList = [word for word in textRemoveingUnnecessaryCharactersList if word not in stop_words] #remove stopwords
    stemmer = PorterStemmer() #stemming        
    for eachWord in textAfterStopwordsRemovingList:
        eachWord = stemmer.stem(eachWord)
        storeToResultDict(eachWord,wordDictionary)
    # Remove common words
    for word in commonWordsList:
        wordDictionary.pop(word,None)
    #print len(wordDictionary)  
    wordList= sorted(wordDictionary.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)
    wordList = wordList[0:numberOfTopMostFrequentWordTest] # the top 10 most frequent words
    #for eachTuple in wordList:
    #    print eachTuple[0],eachTuple[1]   
    return [wordList,fileToProcess]

def calculateProbabilities(resultList):
    wordList = resultList[0]
    resultDic = {}
    prob4Student = probInfo.get("student")
    prob4Course = probInfo.get("course")
    prob4Faculty = probInfo.get("faculty")
    resultDic["student"] = round(prob4Student, 5)
    resultDic["course"] = round(prob4Course, 5)
    resultDic["faculty"] = round(prob4Faculty, 5)
    #print len(wordList)
    for eachTuple in wordList:
        #print eachTuple[0] + ";;;;;;;;;;;;;"
        if eachTuple[0] in wordWithProb4TrainCourse:
            #print eachTuple[0] + "  Course"
            #print resultDic.get("course")
            #print (round(wordWithProb4TrainCourse.get(eachTuple[0]),5))
            resultDic["course"] = resultDic.get("course") * round(wordWithProb4TrainCourse.get(eachTuple[0])/probInfo.get("course"),5)
        else:
            resultDic["course"] = resultDic.get("course") * (0.01)
    for eachTuple in wordList:  
        if eachTuple[0] in wordWithProb4TrainStudent:
            #print eachTuple[0] + "  Student"
            #print resultDic.get("student")
            #print (round(wordWithProb4TrainStudent.get(eachTuple[0]),5))
            resultDic["student"] = resultDic.get("student") * round(wordWithProb4TrainStudent.get(eachTuple[0])/probInfo.get("student"),5)
        else:
            resultDic["student"] = resultDic.get("student") * 0.01          
    for eachTuple in wordList:
        if eachTuple[0] in wordWithProb4TrainFaculty:  
            #print eachTuple[0] + "  Faculty"  
            #print resultDic.get("faculty")   
            #print (round(wordWithProb4TrainFaculty.get(eachTuple[0]),5))    
            resultDic["faculty"] = resultDic.get("faculty") * round(wordWithProb4TrainFaculty.get(eachTuple[0])/probInfo.get("faculty"),5)
        else:
            resultDic["faculty"] = resultDic.get("faculty") * 0.01
    theResult =  max(resultDic.iteritems(), key=operator.itemgetter(1))[0]
    if theResult == "student":
        holder4StudentResult.append(resultList[1])
    elif theResult == "course":
        holder4CouseResult.append(resultList[1])
    else:
        holder4FacultyResult.append(resultList[1])
    #for key,value in resultDic.iteritems():
    #    print key,round(value, 5)    
#calculateProbabilities(tokenizeAndGetMostFrequentyWords("train/student/http:^^www.cs.washington.edu^homes^speed^"))
#calculateProbabilities(tokenizeAndGetMostFrequentyWords("train/course/http:^^www.cs.utexas.edu^users^joshi^cs380d-main.html"))
'''
for key,value in wordWithProb4TrainStudent.iteritems():
    print key,value
print "**************************************************************"
for each in tokenizeAndGetMostFrequentyWords("train/course/http:^^www.cs.washington.edu^education^courses^451^CurrentQuarter^"):
    if each[0] in wordWithProb4TrainCourse:
        print each[0] + "CCCCCC"
    if each[0] in wordWithProb4TrainStudent:
        print each[0] + "SSSSS"
'''
###########################################################################################

# 3. Loop the directories and execute files. Add result to an dictionary and test.
from collections import defaultdict
statResultDic = {}
statResultDic["student"] = []
statResultDic["faculty"] = []
statResultDic["course"] = []
holder4CouseResult = []
holder4StudentResult = []
holder4FacultyResult = []

def loopAndClassifyDocuments(path,statResultDic):  # Main Function
    for filename in os.listdir(os.getcwd()+path):
        calculateProbabilities(tokenizeAndGetMostFrequentyWords(os.getcwd()+path+'/'+filename))

loopAndClassifyDocuments('/test/course',statResultDic)
loopAndClassifyDocuments('/test/faculty',statResultDic)
loopAndClassifyDocuments('/test/student',statResultDic)

def getStatisticsAndTestAccuraty(resultToBeTested):
    predTotal = len(holder4StudentResult) + len(holder4CouseResult) + len(holder4FacultyResult)
    predProb4Student = float(len(holder4StudentResult)) / float(predTotal)
    predProb4Course = float(len(holder4CouseResult)) / float(predTotal)
    predProb4Faculty = float(len(holder4FacultyResult)) / float(predTotal)
    print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
    print "There are " +  str(len(holder4StudentResult)) + " documents be classified as Student. In fact, there are " + str(directoryInfo.get("test/student")) + " student documents."  
    print "There are " +  str(len(holder4CouseResult)) + " documents be classified as Course. In fact, there are " + str(directoryInfo.get("test/course")) + " course documents."  
    print "There are " +  str(len(holder4FacultyResult)) + " documents be classified as Faculty. In fact, there are " + str(directoryInfo.get("test/faculty")) + " faculty documents."  
    print "The classifed percentages of test sets for student, course and faculty are " + str(predProb4Student)+ " , " + str(predProb4Course) + " , " + str(predProb4Faculty) + " respectively."
    print "The actuall percentages of test sets for student, course and faculty are " + str(probInfo.get("studentTest"))+ " , " + str(probInfo.get("courseTest")) + " , " + str(probInfo.get("facultyTest")) + " respectively."
    # print "Correctness for student, course and faculty respectively: " + float(len(holder4StudentResult)) / float(directoryInfo.get("test/student")) + " , "+ + " , " + +
    print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

getStatisticsAndTestAccuraty(statResultDic)

###########################################################################################





###################################################################################
########





###########################################################################################