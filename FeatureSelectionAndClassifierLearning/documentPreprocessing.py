import os # import os for reading source files
import re # import re (regular expression) for checking strings 
          # to see if they match certain patterns
from nltk.corpus import stopwords # import and download from nltk.corpus for checking and removeing stopwords
from nltk import PorterStemmer # import PorterStemmer for stemming a single word
       
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

def tokenizeAndGetFrequency(path): 
    resultDict = {}
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
    return resultDict