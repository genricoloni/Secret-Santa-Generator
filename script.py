import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def fun():
    x = input("How much friends")
    x = int(x)

    #create a list, one for iterator and one for backup
    y  = list(range(x))
    back = list(range(x))
    #fill the list with your friend's names
    for i in range(x):
        y[i] = input()
        back[i] = y[i]

    z = list(range(x))

    # count is the number of friends yet to be paired
    count = x

    print("DONOR:     RECEIVER:")
    for i in range(x):
        # random index from 0 to count
        w = random.randrange(0,count)
        if z[i] == y[w]:
            #if these two are the same, there'll be a self gift and that would be bad
            count += 1
            #so we'll just skip this iteration
            continue
        #assign the value to the list
        z[i] = y[w]
        # print the donor and receiver
        print(back[i], "->",z[i])
        #remove friend from the list
        y.remove(y[w])
        # count is decremented
        count -= 1


fun()