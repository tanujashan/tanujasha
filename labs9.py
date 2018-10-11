# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com',) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("tanujashan30@gmail.com", "        ") 
  
# message to be sent 
message = "hello"
  
# sending the mail 
s.sendmail("tanujashan30@gmail.com", "shylasathya2000@gmail.com", message) 
  
# terminating the session 
s.quit() 