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

## References:

Naive Bayesian Classification: 
http://www.cnblogs.com/leoo2sk/archive/2010/09/17/naive-bayesian-classifier.html
http://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification

### Steps:

#### 1. Review the result of first stage and keep refining it.

#### 2. Update v1.py. Display the words with frequency in each directory (course,falculty,student). Analyze the result files. Find the top common words. Remove those words (e.g. comput,page) in the result dictionary.

#### 3. Get the intersection of two or three result dictionaries. Analyze and remove words.

#### 4. Get the unique words that appear in each folder.

#### 5. Remove words that appear less than 3 times.

### Notes:
Python is ideal for text classification, because of it's strong string class with powerful methods. Furthermore the regular expression module re of Python provides the user with tools, which are way beyond other programming languages. 