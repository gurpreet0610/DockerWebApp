import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_it(problem):
    print(problem+ " Error")
    message = MIMEMultipart()
    message['Subject'] = 'Automatic deployment failed.'
    message['From'] = 'user@gmail.com'
    message['To'] = 'reciever@else.com'
    # f=open("controller/logs.txt", "r")
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
    server.login("user@gmail.com", "12345")             
    server.sendmail("user@gmail.com", "reciver@gmail.com", message.as_string())