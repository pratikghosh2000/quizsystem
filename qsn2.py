import hashlib
import sys
from tkinter import *

top=Tk()
password="095f26e6c7c467c5ecce3205a0dc90f6dc4868e8ddfe7a21829e91d47e386676"  #pratik
class question:
    def __init__(self,x):
        self.x=x
    def getqs(self):
        file1 = open("qsn.txt",'a')
        c = input("enter the questions to be added\n");
        file1.write(c)
        marks =input("enter marks...")
        file1.write(" ")
        file1.write(marks)
        file1.write("\n")
        file1.close()
    def dispqs(self):
        print("contents of question file");
        file1 = open("qsn.txt", 'r')
        line1 = file1.readline()
        while (line1 != ""):
            print(line1)
            line1 = file1.readline()
        file1.close()
def code():
    list1=[]
    qsn=question(1)
    number1=int(input("enter the number of questions to be added"));
    count=1
    while(count<=number1):
        con=input("press any key to continue or press -1 to stop");
        if con=="-1":
            print("contents of question file");
            file1 = open("qsn.txt", 'r')
            line1 = file1.readline()
            while (line1 != ""):
                print(line1)
                line1 = file1.readline()
            file1.close()
            exit()
        else:
            list1.append(qsn.getqs())
            count=count+1
    qsn.dispqs()
    exit()

#def passcheck(text):
    # if hashlib.sha256(text.encode('utf-8')).hexdigest() == password:
    #     print("You are authorized and allowed to add questions")
    #     code()
    #
    # else:
    #     print("Error in password. You are not authorized")
    #     exit()

def check():

    name=input("Enter password: ")
    #name.encode('utf-8')

    if hashlib.sha256(name.encode('utf-8')).hexdigest() == password:
        print("You are authorized and allowed to add questions")
        code()

    else:
        print("Error in password. You are not authorized")
        exit()



top.geometry("500x100")
var = StringVar()
label = Message(top, textvariable=var, relief=RAISED)
var.set("WELCOME TO QUIZ SYSTEM\n TO CONTINUE PRESS NEXT")
B = Button(top, text="NEXT",command=check)
B.place(x=100, y=100)

# canvas1 = Canvas(top, width=400, height=300)
# canvas1.pack()
# entry1 = Entry(top)
# canvas1.create_window(200, 140, window=entry1)
# x1 = entry1.get()
# a=print(x1)
# button1 = Button(text='enter password',command=check(a))
# canvas1.create_window(200, 180, window=button1)
B.pack()
label.pack()
top.mainloop()