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

