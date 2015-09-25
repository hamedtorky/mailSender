__author__ = 'hamedorky'
class sendMail():
    def __init__(self,mail_Config_File,html_File):

        mailconfig = open(mail_Config_File,'r')
        self.listName = mailconfig.readline().strip()
        self.from_address = mailconfig.readline().strip()
        self.username = self.from_address
        self.password = mailconfig.readline().strip()
        self.to_address = mailconfig.readline().strip()
        self.ccMail = self.to_address
        self.bccMail = self.to_address
        self.smtpAddress = mailconfig.readline().strip()
        self.subject = mailconfig.readline().strip()
        mailconfig.close()
        self.sleepTime = 2#second
        self.counter = 0
        fileHtml = open(html_File,'r')
        self.html = fileHtml.read()
        fileHtml.close()
        print (mail_Config_File+html_File)

    def sendMailList(self):
        import time
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        from email.MIMEImage import MIMEImage

        mailBuffer = []
        mailList = open(self.listName,"r")
        endSendMail = 0
        print 'Start send mail in list "' + self.listName+'"'
        print '---------------------------------------------------'
        while endSendMail == 0:

            for i in xrange(20):
                mailBuffer.append(mailList.readline().strip())
                self.ccMail = self.ccMail + ',' + mailBuffer[i]
                self.bccMail = self.bccMail + ',' + mailBuffer[i]

            for i in xrange(20):

                print mailBuffer[i]
                if mailBuffer[i] == "end":
                    endSendMail = 1
                    print "wait close program "
                    break
                self.counter = self.counter + 1
                self.to_address = mailBuffer[i]

                msg = MIMEMultipart()

                msg['From'] = self.from_address
                msg['To'] = self.to_address
                msg['Subject'] = self.subject
                msg['Bcc'] = self.bccMail
                msg['Cc'] = self.ccMail

                # msg.attach(MIMEText(text,'plain'))
                msg.attach(MIMEText(self.html,'html'))
                msg.attach(MIMEImage(file("img/image1.png").read()))

                # if counterAttach > 0:
                #     for attachNum in xrange(counterAttach):
                #         msg.attach(MIMEImage(file(attachFile[attachNum]).read()))

                server = smtplib.SMTP(self.smtpAddress)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.username, self.password)
                server.sendmail(self.from_address, self.to_address, msg.as_string())
                server.quit()

                print 'send email for ',self.to_address
                print 'Done.'
                print '---------------------------------------------------'
            ccMail = self.to_address
            bccMail = self.to_address
            time.sleep(self.sleepTime)
        mailList.close()
        print "Program Ended :p"
