__author__ = 'hamedorky'

class mailDetect():

    def __init__(self,file_Name):
        from urllib import urlopen
        import urllib

        url = open(file_Name,'r')
        self.link = url.readlines(2)
        url.close()
        self.content = urlopen(self.link[1]).read()
        self.doc = urllib.unquote(self.content).decode('utf8')

    def searchMail(self,FileName):
        from re import findall

        list =  findall('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', self.content)
        file = open(FileName, "w")
        file.write("mail list of "+self.link[1]+"\n \n")

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
