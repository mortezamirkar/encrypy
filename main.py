import functtions as f
try:
 question=int(input("1-encrypt\n2-decrypt\nEnter 1 or 2: "))
except :
    print("invalid input!")
    exit()
if question==1:
 filename=input("please enter the path of your file: ")
 f.createKeyFike()
 try:
     f.encrypt(filename,"key.key")
 except FileNotFoundError as err:
     print(err)
else:
    filename=input("please enter the path of your file: ")
    userkey=input("please enter the path of you key file: ")
    try:
     f.decrypt(filename,userkey)
    except FileNotFoundError as err:
        print(err)
