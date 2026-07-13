#Write User Name to File
name=input("enter your name:")
file=open("user.txt","w")
file.write(name)
file.close()
