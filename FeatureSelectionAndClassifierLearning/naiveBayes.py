# Implementing Naive Bayes Classifer by using NLTK

###################################################################################################
# import the required libraries

import sys, subprocess, os # For getting directories information for calculating the probability.

import re # import re (regular expression) for checking strings 
          # to see if they match certain patterns

import operator

from documentsProcessing import removeUnnecessaryCharacters,storeToResultDict,tokenizeAndGetFrequency,sortAndCutWordsInTestSet,tokenizeAndGetFreq4SingleDocument

# Get the number of most frequent words to be processed
numberOfTopMostFrequentWordTrain = int(sys.argv[1])
numberOfTopMostFrequentWordTest = int(sys.argv[2])

###################################################################################################

# 1. Get statistics.

pathList = []
directoryInfo = {}

pathList.append('train/course')
pathList.append('train/faculty')
pathList.append('train/student')
pathList.append('test/course')
pathList.append('test/faculty')
pathList.append('test/student')

# Count the number of files in this directory.
for filePath in pathList:
    p1 = subprocess.Popen(('ls',filePath), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(('wc','-l'), stdin=p1.stdout, stdout=subprocess.PIPE)
    directoryInfo[filePath] = int(filter(str.isdigit, str(p2.communicate())))

total4Test = directoryInfo.get("test/student") + directoryInfo.get("test/course") + directoryInfo.get("test/faculty")
total4Train = directoryInfo.get("train/student") + directoryInfo.get("train/course") + directoryInfo.get("train/faculty")

# Get the prior probabilities for each label/class
prob4TrainStudent = float(directoryInfo.get("train/student"))/float(total4Train)
prob4TrainCourse = float(directoryInfo.get("train/course"))/float(total4Train)
prob4TrainFaculty = float(directoryInfo.get("train/faculty"))/float(total4Train)

# Get the probabilities for labels in test set (To test accuracy)
prob4TestStudent = float(directoryInfo.get("test/student"))/float(total4Test)
prob4TestCourse = float(directoryInfo.get("test/course"))/float(total4Test)
prob4TestFaculty = float(directoryInfo.get("test/faculty"))/float(total4Test)

###################################################################################################

# 2. Preprocess documents in train sets. Tokenize words and get the words' frequency. 
#    Then getting the probability for each word 
#    i.e. number of words occuring in this set / total number of all words occuring in this set.
#    Only keep the top most frequent words (user input indicates the number).

wordWithFrequency4TrainStudent = tokenizeAndGetFrequency("/train/student")
wordWithFrequency4TrainCourse = tokenizeAndGetFrequency("/train/course")
wordWithFrequency4TrainFaculty = tokenizeAndGetFrequency("/train/faculty")

def getProbability(toBeProcessed):
    wordWithProb = {}
    resultList= sorted(toBeProcessed.iteritems(), key=lambda frequency:frequency[1], reverse = True) # sort the dict based on the value (frequency)
    totalNumberOfWordsAppear = 0
    resultList = resultList[:numberOfTopMostFrequentWordTrain] # Pick the top most frequent number  
    for eachTuple in resultList:
        totalNumberOfWordsAppear = totalNumberOfWordsAppear + eachTuple[1]
    for eachTuple in resultList:
        wordWithProb[eachTuple[0]] = float(eachTuple[1]) / float(totalNumberOfWordsAppear)
    return wordWithProb

wordWithProb4TrainStudent = getProbability(wordWithFrequency4TrainStudent)
wordWithProb4TrainCourse = getProbability(wordWithFrequency4TrainCourse)
wordWithProb4TrainFaculty = getProbability(wordWithFrequency4TrainFaculty)

###################################################################################################

# 3. Calculating probability and classify documents.

holder4Student = []
holder4Course = []
holder4Faculty = []

def calculateAndClassify(toBeProcessed,filename):
    resultDic = {}
    # Prior probabilities
    resultDic["student"] = prob4TrainStudent
    resultDic["course"] = prob4TrainCourse
    resultDic["faculty"] = prob4TrainFaculty
    for eachTuple in toBeProcessed:
        if eachTuple[0] in wordWithProb4TrainCourse:
            resultDic["course"] = resultDic.get("course") * wordWithProb4TrainCourse.get(eachTuple[0])/prob4TrainCourse
        else:
            resultDic["course"] = resultDic.get("course") * 0.01
    for eachTuple in toBeProcessed:  
        if eachTuple[0] in wordWithProb4TrainStudent:
            resultDic["student"] = resultDic.get("student") * wordWithProb4TrainStudent.get(eachTuple[0])/prob4TrainCourse
        else:
            resultDic["student"] = resultDic.get("student") * 0.01          
    for eachTuple in toBeProcessed:
        if eachTuple[0] in wordWithProb4TrainFaculty:     
            resultDic["faculty"] = resultDic.get("faculty") * wordWithProb4TrainFaculty.get(eachTuple[0])/prob4TrainCourse
        else:
            resultDic["faculty"] = resultDic.get("faculty") * 0.01
    #for key,value in resultDic.iteritems():
    #    print key,value
    theResult =  max(resultDic.iteritems(), key=operator.itemgetter(1))[0]
    if theResult == "student":
        holder4Student.append(filename)
    elif theResult == "course":
        holder4Course.append(filename)
    else:
        holder4Faculty.append(filename)

###################################################################################################

# 4. Loop the directories and process files. Add result to an dictionary and test.

def loopAndProcessDocuments(path):  
    for filename in os.listdir(os.getcwd()+path): 
        calculateAndClassify(sortAndCutWordsInTestSet(tokenizeAndGetFreq4SingleDocument(os.getcwd()+path+'/'+filename),numberOfTopMostFrequentWordTest),filename)

loopAndProcessDocuments('/test/course')
loopAndProcessDocuments('/test/faculty')
loopAndProcessDocuments('/test/student')

###################################################################################################

# 5. Format and displaythe result
def formatAndDisplayResult():
    # Predicted statistics
    predTotal = len(holder4Student) + len(holder4Course) + len(holder4Faculty)
    predProb4Student = float(len(holder4Student)) / float(predTotal)
    predProb4Course = float(len(holder4Course)) / float(predTotal)
    predProb4Faculty = float(len(holder4Faculty)) / float(predTotal)

    print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
    print "There are " +  str(len(holder4Student)) + " documents be classified as Student. In fact, there are " + str(directoryInfo.get("test/student")) + " student documents."  
    print "There are " +  str(len(holder4Course)) + " documents be classified as Course. In fact, there are " + str(directoryInfo.get("test/course")) + " course documents."  
    print "There are " +  str(len(holder4Faculty)) + " documents be classified as Faculty. In fact, there are " + str(directoryInfo.get("test/faculty")) + " faculty documents."  
    print "The classifed percentages of test sets for student, course and faculty are " + str(predProb4Student)+ " , " + str(predProb4Course) + " , " + str(predProb4Faculty) + " respectively."
    print "The actuall percentages of test sets for student, course and faculty are " + str(prob4TestStudent)+ " , " + str(prob4TestCourse) + " , " + str(prob4TestFaculty) + " respectively."
    print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"

#formatAndDisplayResult()

###################################################################################################

# 6. Test accuracy and display accuracy score.
def testAccuracy(testSetPath,listToBeTested):
    nameHolder = set()
    for filename in os.listdir(os.getcwd()+testSetPath):
        nameHolder.add(filename)
    holder4Test = set(listToBeTested)
    # Formula : accuracy = number of correct classifed documents / total # of documents
    return float(len(holder4Test&nameHolder)) / float(len(nameHolder))

def displayAccuray(studentScore,courseScore,facultyScore):
    print "************************************************************************************************"
    print "Given the top most " + str(numberOfTopMostFrequentWordTrain) + " , " + str(numberOfTopMostFrequentWordTest) + " frequent words in train and test sets"
    print "The accuracy for classified student documents is " + str(studentScore)
    print "The accuracy for classified course documents is " + str(courseScore)
    print "The accuracy for classified faculty documents is " + str(facultyScore)
    print "The average accuracy is " + str(float(sum([studentScore,courseScore,facultyScore])/3))
    print "************************************************************************************************"

displayAccuray(testAccuracy('/test/student',holder4Student),testAccuracy('/test/course',holder4Course),testAccuracy('/test/faculty',holder4Faculty))
