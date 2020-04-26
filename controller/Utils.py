import os
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def get_pull():
    p_return=0
    with open("controller/logs.txt", 'wb') as logfile:
        p_return=subprocess.call(['git','pull'] ,stdout=logfile, stderr=subprocess.STDOUT)
    if(p_return!=0):
        email_it("Git Pull")
        return 
    return buildUp()
    
    
def buildUp():
    with open("controller/logs.txt", 'wb') as logfile:
        p_return=subprocess.call(['docker-compose','build'] ,stdout=logfile, stderr=subprocess.STDOUT)
    if(p_return!=0):
        email_it("Build")
        return RollBack()
     
    with open("controller/logs.txt", 'wb') as logfile:
        p_return=subprocess.call(['docker-compose','up','-d'] ,stdout=logfile, stderr=subprocess.STDOUT)
    if(p_return!=0):
        email_it("Runtime")
        return RollBack()
    print("Done ALL")
    return 
    
def RollBack():
    p_return=0
    with open("controller/logs.txt", 'wb') as logfile:
        p_return=subprocess.call(['git','reset','--hard','HEAD@{1}'] ,stdout=logfile, stderr=subprocess.STDOUT)
    if(p_return!=0):
        email_it("RollBack")
        return
    buildUp()
   

def email_it(problem):
    print(problem+ " Error")
    message = MIMEMultipart()
    message['Subject'] = 'Automatic deployment failed.'
    message['From'] = 'sender@gmail.com'
    message['To'] = 'receiver@gmail.com'
    f=open("controller/logs.txt", "r")
    fail="""<h2> Flask Web Application - <b> {}</b> Failed.<br/></h2>
            <br/>
            Check console <a href="">output</a> to view full results.<br/>
            If you cannot connect to the build server, check the attached logs.<br/>
            <br/>
            --<br/>
            Following is the last lines of the log.<br/>
            <br/>
            --LOG-BEGIN--<br/>
            <pre style='line-height: 22px; display: block; color: #333; font-family: Monaco,Menlo,Consolas,"Courier New",monospace; padding: 10.5px; margin: 0 0 11px; font-size: 13px; word-break: break-all; word-wrap: break-word; white-space: pre-wrap; background-color: #f5f5f5; border: 1px solid #ccc; border: 1px solid rgba(0,0,0,.15); -webkit-border-radius: 4px; -moz-border-radius: 4px; border-radius: 4px;'>{}</pre>
            --LOG-END-- """.format(problem,f.read())
    message.attach(MIMEText(fail, 'html') )       
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sender@gmail.com", "password")             
    server.sendmail("sender@gmail.com", "receiver@gmail.com", message.as_string())
