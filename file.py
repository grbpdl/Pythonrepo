file=open('abc.txt','r')#read the  file contents
#data=file.read() #reads whole file
#print(data)
#file.close()
a=file.readline() #reads a line
#b=file.read(4) #read first 4 character
print (a)
file.close()
file=open('abc.txt','w')
file.write("overwriting")
file.close()
file=open('abc.txt','a')
file.write(". adding at last")
file.close()
with open('abc.txt','r') as f:#no need to close if opened using with
    f.read()
