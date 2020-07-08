import hashlib
import sys
password="095f26e6c7c467c5ecce3205a0dc90f6dc4868e8ddfe7a21829e91d47e386676"  #pratik
class question:
    def __init__(self,x):
        self.x=x
    def getqs(self):
        file1 = open("qsn.txt",'a')
        c = input("enter the questions to be added\n");
        file1.write("\n")
        file1.write(c)
        file1.close()
    def dispqs(self):
        print("contents of question file");
        file1 = open("qsn.txt", 'r')
        line1 = file1.readline()
        while (line1 != ""):
            print(line1)
            line1 = file1.readline()
        file1.close()
def main():
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
            qsn.getqs()
            count=count+1
    qsn.dispqs()

while True:
    name=input("Enter password: ")
    #name.encode('utf-8')
    if hashlib.sha256(name.encode('utf-8')).hexdigest()==password:
        print("You are authorized and allowed to add questions")
        main()
    else:
        print("Error in password. You are not authorized")