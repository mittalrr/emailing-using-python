import smtplib
from email.mime.text import MIMEText
import config
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

EMAIL=config.EMAIL  # email stored in config.py file
PASSWORD=config.PASSWORD  #password stored in config.py file
server.login(EMAIL,PASSWORD)

# message=MIMEText("Sent from py")
message=MIMEText(input("Enter the mail MESSAGE: "))
message["From"]=EMAIL
message["To"]=EMAIL
# message["Subject"]="Hellow WOrld"
message["Subject"]=input("Enter the mail SUBJECT: ")
print("Please wait...\nSending mail...")

server.sendmail(EMAIL,EMAIL,message.as_string())

print("Mail is successfully sent")
