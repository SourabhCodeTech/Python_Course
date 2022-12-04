import smtplib as s
ob=s.SMTP('smtp.gmail.com', 587)
ob.starttls()
ob.login("vandanagautam540@gmail.com", "Eshugautam@123")
subject = "Jeene mera dil luteya"
body = "Ohooo, I am Sourabh Gautam!"
message = '''
{}
{}
'''.format(subject,body)

listOfAddress = ["vandanagautam503@gmail.com", "gplicbbk@gmail.com"]

ob.sendmail("vandanagautam540", listOfAddress, message)
print("Send SuccessFully!!")
ob.quit()
