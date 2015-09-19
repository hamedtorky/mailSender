# __author__ = 'hamedtorky'
import time
import glob, os
import PyQt4
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

mailconfig = open("mailconfig.txt",'r')

listName = mailconfig.readline().strip()

from_address = mailconfig.readline().strip()
username = from_address
password = mailconfig.readline().strip()

to_address = mailconfig.readline().strip()
ccMail = to_address
bccMail = to_address

smtpAddress = mailconfig.readline().strip()
mailconfig.close()
print 'send mail by "'+from_address+'"'
print 'static mail is "'+to_address+'"'
print ''

sleepTime = 2#second

counter = 0

Subject = 'test message!'
text = 'send by HAMED.app'
fileHtml = open("html.txt",'r')
html = fileHtml.read()
fileHtml.close()

# -----------------------------------------------------------------
mailBuffer = []
mailList = open(listName,"r")

endSendMail = 0
print 'Start send mail in list "' + listName+'"'
print '---------------------------------------------------'

print 'Scan attach file :'
attachFile= []
counterAttach = 0
os.chdir("img")
for file in glob.glob("*.*"):
    print 'Name file : '+ file
    attachFile.append("img/"+file)
    counterAttach = counterAttach +1



while endSendMail == 0:

    for i in xrange(20):
        mailBuffer.append(mailList.readline().strip())
        ccMail = ccMail + ',' + mailBuffer[i]
        bccMail = bccMail + ',' + mailBuffer[i]

    for i in xrange(20):

        print mailBuffer[i]
        if mailBuffer[i] == "end":
            endSendMail = 1
            print "wait close program "
            break
        counter = counter + 1
        to_address = mailBuffer[i]

        msg = MIMEMultipart()

        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = Subject
        msg['Bcc'] = bccMail
        msg['Cc'] = ccMail

        msg.attach(MIMEText(text,'plain'))
        msg.attach(MIMEText(html,'html'))
        # msg.attach(MIMEImage(file("img/image1.png").read()))

        if counterAttach > 0:
            for attachNum in xrange(counterAttach):
                msg.attach(MIMEImage(file(attachFile[attachNum]).read()))

        server = smtplib.SMTP(smtpAddress)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()

        print 'send email for ',to_address
        print 'Done.'
        print '---------------------------------------------------'


    ccMail = to_address
    bccMail = to_address
    time.sleep(sleepTime)
mailList.close()
print "Program Ended :p"

