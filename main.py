__author__ = 'hamedtorky'


from mailDetectFromWebpage import mailDetect
from classSendmail import sendMail


sendMail('mailconfg.txt','html.txt').sendMailList()

mailDetect('url.txt').searchMail('my.txt')