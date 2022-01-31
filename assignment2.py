

import socket
import string

class Assignment2:
    string_isnumeric = string.isnumeric()
    def __init__(self,age):
        self.age = age
    def sayWelcome(self,name):
        print("Welcome to the assignment, " + name +" haven't seen you for " + str(self.age)+" years!")
    def doubleList(self,arr):
        for i,val in enumerate(arr):
            arr[i] =  val*2
        arr1 = []
        arr2 = []
        #meaning of add and even interchanges due to
        #List being 0 indexed in Python 
        for i,val in enumerate(arr):
            if(i%2==0):
                arr1.append(val)
            else:
                arr2.append(val)

        arr1.extend(arr2)
        return arr1
    def modifyString(self, str):
        ans = ""
        for i,val in enumerate(str):
            if((i+1)%3==0):
                ans += val.upper()
            elif((i+1)%4==0):
                ans += val.lower()
            elif((i+1)%5==0):
                ans += " "
            else:
                ans +=val

        return ans
    def isGoodPassword(self, str):
        if(len(str)<9):
            return False
        smalls = 0
        bigs = 0
        spl = 0
        num = 0
        for val in str[0:-1:1]:
            
            if(val.isnumeric()):
                num +=1
            elif(val.isupper()):
                bigs+=1
            elif(val.islower()):
                smalls+=1
            elif(val==',' or val == '.' or val == '#'):
                spl += 1
        if(smalls >= 2 or bigs >= 3):
            if(spl >= 2 or num >= 1):
                return True
        return False

    def connectTcp(self,host,port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))            
            print("Connection established correctly")
        except:
            print("Some error")
obj = Assignment2(12)

obj.sayWelcome("John")

list2 = obj.doubleList(["foo", " bar", "cho", "sar"])
# print(list2)

new_str = obj.modifyString("mikeTestingHello!")
# print(new_str)

pass_word_check = obj.isGoodPassword("12E*,a$$$$$$$aaa")
# print(pass_word_check)

obj.connectTcp('www.google.com',80)
