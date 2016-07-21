# Project stage 2 report and presentation requirements:

Implement a learning algorithm to classify test documents with the
vocabulary selected in stage 1. Your report and presentation (20 minutes) should include
learning programs developed and classification performance. You should use all possible
techniques learnt in this course to achieve the best performance you can. 

## 1. Report should be formally organized, formatted, and written without spelling errors.

Report should clearly describe the problem you address, and particularly how you
address the problem step by step with details (e.g. how you finalize the vocabulary,
what model you use to implement the classifier, what is the performance, what you
have done to improve the performance).

## 2. You should implement your own code without using any open sources.

## 3. Provide references at the end of report for any work you refer to.

## 4. Report and presentation should address the following:
### 1) Feature selection

o The vocabulary you actually use in the implementation of the classifier:
the size and all words

o How you reduce the vocabulary from stage 1 to this size, and why you
are confident these words are good in discrimination

o Review the key parts of your code

### 2) Classifier learning

o What classifier model you have chosen and implemented

o What is the performance

o What you have done to improve the performance

o Review the key parts of your code

### 3) Any lessons you have learned and deemed valuable. Note: Discussion on
lessons and problems won't impact your marks negatively but positively.

### 4) The presentation slides should be readable to audiences with proper <font></font>s.

## 5. Report and presentation should be printed out and submitted to me before the due day class. 

### Performance:
* If the selected top most frequent words for a train set and a single documents in test set are 300 and 50, the accuracy is 0.686984737077
* If the selected top most frequent words for a train set and a single documents in test set are 300 and 20, the accuracy is 0.710603275401
* If the selected top most frequent words for a train set and a single documents in test set are 300 and 10, the accuracy is 0.726604278075
* If the selected top most frequent words for a train set and a single documents in test set are 200 and 50, the accuracy is 0.750153186275
* If the selected top most frequent words for a train set and a single documents in test set are 200 and 20, the accuracy is 0.74370543672
* If the selected top most frequent words for a train set and a single documents in test set are 200 and 10, the accuracy is 0.786179812834
* If the selected top most frequent words for a train set and a single documents in test set are 100 and 50, the accuracy is 0.772977941176
* If the selected top most frequent words for a train set and a single documents in test set are 100 and 20, the accuracy is 0.7656807041
* If the selected top most frequent words for a train set and a single documents in test set are 100 and 10, the accuracy is 0.791388146168 (THE HIGHEST ACCURACY)
* If the selected top most frequent words for a train set and a single documents in test set are 50 and 50, the accuracy is 0.727565173797
* If the selected top most frequent words for a train set and a single documents in test set are 50 and 20, the accuracy is 0.72026793672
* If the selected top most frequent words for a train set and a single documents in test set are 50 and 10, the accuracy is 0.765346479501
* If the selected top most frequent words for a train set and a single documents in test set are 20 and 20, the accuracy is 0.622855392157
* If the selected top most frequent words for a train set and a single documents in test set are 20 and 10, the accuracy is 0.645819407308
* If the selected top most frequent words for a train set and a single documents in test set are 10 and 10, the accuracy is 0.627172459893

### Valuable lesson and experience learnt
* How to deal with dirty data/words.
* Data pre-processing/tokenizing.
* Data structures. List/Dictionary/Set for storing data and operations on those data.
* Python features, syntax.
* Supervised learning.
* Naive Bayes model and classifier.
* Shell scripting.
* Python system processing.



### How to use:

Download and install the required python programs.
Open your terminal, navigate to this folder.
In your command line, type "python naiveBayes.py 100 10". 
The last two number are the number of top most frequent words (for train and test, respectively) you wanna use to classify documents.
Or, you can "sh nbshell.py" to test with different top most frequent numbers.

## Tools Used:
### Language: Python.
#### Why I use Python rather than Java?
* Easy syntax and readibility.
* Python programs are generally expected to run slower than Java programs, but they also take much less time to develop. 
* Python programs are typically 3-5 times shorter than equivalent Java programs. This difference can be attributed to Python's built-in high-level data types and its dynamic typing. 
* Python is ideal for text classification, because of it's strong string class with powerful methods. Furthermore the regular expression module re of Python provides the user with tools, which are way beyond other programming languages. 

### Built on Spyder.
* Spyder is an interactive Python development environment providing MATLAB-like features in a simple and light-weighted software. It also provides ready-to-use pure-Python widgets to your PyQt4 or PySide application: source code editor with syntax highlighting and code introspection/analysis features, NumPy array editor, dictionary editor, Python console, etc.

## Libraries and APIs used:

### os
* os (Miscellaneous operating system interfaces) imported to read, create and write files 
* check os website (https://docs.python.org/2/library/os.html)

### re
* re (Regular expression operations) imported to check strings see if they match certain patterns
* check re website (https://docs.python.org/2/library/re.html)

### sys,subprocess
* import those packages to act as command line tools (e.g., cd, ls, wc -l)
* enable python to take arguments
* to get the number of documents in each directoy
* (https://docs.python.org/2/library/sys.html) (https://docs.python.org/2/library/subprocess.html)

### from documentsProcessing import some methods
* documentsProcessing.py is used for tokenzing, pre-processing documents.
* part of its code was developed at stage 1.
* import methods for tokenizing and processing documents
* good for code reliability and maintenance

### nltk

#### NLTK is a leading platform for building Python programs to work with human language data. (http://www.nltk.org/)

#### from nltk.corpus import stopwords; imported and downloaded from nltk.corpus for checking and removing stopwords
*  Stop words are basically a set of commonly used words in any language, not just English. The reason why stop words are critical to many applications is that, if we remove the words that are very commonly used in a given language, we can focus on the important words instead.

#### from nltk import PorterStemmer; imported PorterStemmer for stemming a single word
* Stemming is the process for reducing inflected (or sometimes derived) words to their stem, base or root form—generally a written word form. 

## References:

Naive Bayesian Classification: 
(http://www.cnblogs.com/leoo2sk/archive/2010/09/17/naive-bayesian-classifier.html)
(http://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification)
(http://www.nltk.org/book/ch06.html)
(http://www.analyticsvidhya.com/blog/2015/09/naive-bayes-explained)


Python Advantages
(https://www.python.org/doc/essays/comparisons/)
(https://en.wikiversity.org/wiki/Python/Why_learn_Python)

More about Spyder
(https://pythonhosted.org/spyder/overview.html)

Stopwords
(http://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html)

Python stopwords removing 
(http://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python)

Stemming
(http://stackoverflow.com/questions/10369393/need-a-python-module-for-stemming-of-text-documents)
(http://www.nltk.org/api/nltk.stem.html)
(http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization)

os
(https://docs.python.org/2/library/os.html)

re
(https://docs.python.org/2/library/re.html)

dictionary sorting
(http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python)

add new stopwords
(http://stackoverflow.com/questions/19130512/stopword-removal-with-nltk)

sys
(https://docs.python.org/2/library/sys.html) 

subprocess
(https://docs.python.org/2/library/subprocess.html)

data structures (dictionary, list, set)
(https://docs.python.org/3/tutorial/datastructures.html)