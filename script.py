import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass



def fun():
    x = input("How much friends? ")
    x = int(x)

    #create a list, one for iterator and one for backup
    y  = list(range(x))
    print("Insert your friends' names")
    #fill the list with your friend's names
    for i in range(x):
        y[i] = input()
        
    back = y.copy()
    z = list(range(x))

    # count is the number of friends yet to be paired
    count = x

    sender = input("Enter your email address without 'gmail.com': ")
    password = getpass.getpass("Enter your 16-digit-app-password: ")
    
    i = 0
    while i < x:
        # random index from 0 to count
        w = random.randrange(0,count)
        if back[i] == y[w]:
            #if these two are the same, there'll be a self gift and that would be bad
            #so we'll just skip this iteration
            continue
        #assign the value to the list
        z[i] = y[w]
        #print the donor and receiver: DELETE NEXT LINE IF YOU DON'T WANT TO SEE THE PAIRS
        print(back[i], "->",z[i])
        #DELETE THE NEXT LINE IF YOU DON'T WANT TO SEND THE EMAILS
        email(sender, back[i], z[i], password)
        #remove choosen friend from the list
        y.remove(y[w])
        # count and index are decremented
        count -= 1
        i += 1

#send an email to the donor from unique email address
#now it works only with gmail
def email(sender, donor, receiver, password):

    #get the email address of the donor
    donor_e = input("Enter the email address of " + donor + ": ")
    #get the message
    message = "Hi "+ donor + "! You'll have to give a gift to" + receiver + "!"

    #create a new email
    msg = MIMEMultipart()
    #add the sender's email address
    msg['From'] = str(sender)
    #add the receiver's email address
    msg['To'] = str(donor_e)
    #add the subject
    msg['Subject'] = "Secret Santa"

    #add the message
    msg.attach(MIMEText(message, 'plain'))

    #create a new server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #start the server
    server.starttls()
    #login to the server
    server.login(sender, password)
    #send the email
    server.sendmail(sender, donor_e, msg.as_string())
    #close the server
    server.quit()
    
fun()