import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


message = MIMEMultipart()
message['Subject'] = 'Automatic deployment failed.'
message['From'] = 'imailgurpreet@gmail.com'
message['To'] = 'gurpreets8117@else.com'
fail="""Flask Web App - Build # 12345 - Fail.<br/>
<br/>
Check console <a href="">output</a> to view full results.<br/>
If you cannot connect to the build server, check the attached logs.<br/>
<br/>
--<br/>
Following is the last 100 lines of the log.<br/>
<br/>
--LOG-BEGIN--<br/>
<pre style='line-height: 22px; display: block; color: #333; font-family: Monaco,Menlo,Consolas,"Courier New",monospace; padding: 10.5px; margin: 0 0 11px; font-size: 13px; word-break: break-all; word-wrap: break-word; white-space: pre-wrap; background-color: #f5f5f5; border: 1px solid #ccc; border: 1px solid rgba(0,0,0,.15); -webkit-border-radius: 4px; -moz-border-radius: 4px; border-radius: 4px;'>
2020-04-24T19:42:35.692995+00:00 heroku[router]: at=info method=POST path="/payload" host=webtunneler.herokuapp.com request_id=6f8661a8-19d5-4b4b-b8e2-26a6bd165252 fwd="192.30.252.97" dyno=web.1 connect=0ms service=2584ms status=200 bytes=171 protocol=https
2020-04-24T19:42:35.691573+00:00 app[web.1]: 10.155.88.71 - - [24/Apr/2020:19:42:35 +0000] "POST /payload HTTP/1.1" 200 19 "-" "GitHub-Hookshot/8b3e8c7"
2020-04-24T19:44:57.942321+00:00 app[web.1]: 10.45.161.126 - - [24/Apr/2020:19:44:57 +0000] "POST /payload HTTP/1.1" 200 19 "-" "GitHub-Hookshot/8b3e8c7"
2020-04-24T19:44:57.944303+00:00 heroku[router]: at=info method=POST path="/payload" host=webtunneler.herokuapp.com request_id=e2167da9-cb65-49a4-b7ea-259c0400187c fwd="140.82.115.250" dyno=web.1 connect=1ms service=2987ms status=200 bytes=171 protocol=https
</pre>
--LOG-END-- """
message.attach(MIMEText(fail, 'html') )       
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("imailgurpreet@gmail.com", "Wahe123@")             
# server.sendmail(“sender@gmail.com”, “receiver@gmail.com”, “YourMessage”)
server.sendmail("imailgurpreet@gmail.com", "gurpreets8117@gmail.com", message.as_string())

server.quit()