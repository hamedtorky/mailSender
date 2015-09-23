__author__ = 'hamedorky'

from urllib import urlopen
import urllib
from re import findall



url = open('mailDetectConfig.txt','r')

link = url.readlines(2)
url.close()
print link[1]
content = urlopen(link[1]).read()


doc = urllib.unquote(content).decode('utf8')

# list =  findall('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', doc)
list =  findall('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', content)

file = open("newfile.txt", "w")

file.write("mail list of "+link[1]+"\n \n")
print "start\n"
for i in xrange(len(list)):
    if i == 0:
        file.write((list[i]+'\n'))
        printList = list[i]
        print printList
    elif(list[i-1] != list[i]):
        file.write(list[i]+'\n')
        printList = list[i]
        print printList

file.close()


