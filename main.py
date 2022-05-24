import functtions as f
question=int(input("1-encrypt\n2-decrypt\nEnter 1 or 2: "))
if question==1:
 filename=input("please enter your file name with its format: ")
 f.createKeyFike()
 f.encrypt(filename,"key.key")
else:
    filename=input("please enter your file name: ")
    userkey=input("please enter you key file name: ")
    f.decrypt(filename,userkey)
