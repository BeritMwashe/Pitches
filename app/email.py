import email
from email import message
import os


from flask import Flask,render_template,request


from flask_mail import Mail,Message
from . import mail

def send_email(to,subject,template,**kwargs):
    
    if request.method=='POST':
        e_mail=to
        subject=subject
        
        
        message=Message(subject,sender='mwasheberit@gmail.com',recipients=[to])
        message.body=render_template(template+'.txt',**kwargs)
        message.html=render_template(template+'.html',**kwargs)

        mail.send(message)
        success="Message sent"
        
        # return render_template('auindex.html',success=success)