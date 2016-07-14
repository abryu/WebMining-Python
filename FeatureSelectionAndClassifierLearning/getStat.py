import subprocess 

pathList = []
directoryInfo = {}

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

for key, value in directoryInfo.iteritems():
    print key, value

# For Naive Bayes
total4Test = directoryInfo.get("test/student") + directoryInfo.get("test/course") + directoryInfo.get("test/faculty")
total4Train = directoryInfo.get("train/student") + directoryInfo.get("train/course") + directoryInfo.get("train/faculty")



prob4TrainStudent = float(directoryInfo.get("train/student"))/float(total4Train)
prob4TrainCourse = float(directoryInfo.get("train/course"))/float(total4Train)
prob4TrainFaculty = float(directoryInfo.get("train/faculty"))/float(total4Train)

prob4TestStudent = float(directoryInfo.get("test/student"))/float(total4Test)
prob4TestCourse = float(directoryInfo.get("test/course"))/float(total4Test)
prob4TestFaculty = float(directoryInfo.get("test/faculty"))/float(total4Test)

print (total4Test)
print (total4Train)
print (prob4TrainStudent)
print (prob4TrainCourse) 
print (prob4TrainFaculty)