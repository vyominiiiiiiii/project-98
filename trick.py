def swapData():
    name=input("ENTER YOUR FILE NAME: ")

    x=open("file1.txt","r")
    print(x.read())
    y=open("file1.txt","w")
    y.write("Bbbbbrother yu have been PPPPranked!")
    print(y)

    a=open("file2.txt","r")
    print(a.read())
    b=open("file2.txt","w")
    b.write("Title: The Importance of Health: A Gateway to Happiness and Success")
    print(b)
    ## print(y)
   # x.close()
   # y=open("file2.txt","r")
   # open(file1.tx,"w")

swapData()
    
