def File_Handling():
    f=open('myfile.txt','r')
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
     
     
     #Also
    fi=open('myfile.txt','r')
    i=0 
    while True:
        i=i+1
        line=fi.readline()
        if not line:
            break
        m1=int(line.split(",")[0])
        m2=int(line.split(",")[1])
        print(f"mark of student {i} in math is {m1}")
        print(f"mark of student {i} in math is {m2}")
        print(line)
    
    #writelines()    
    f=open("myfile.txt","w")
    lines=["line 1\n","line \2", "line \3"]      #This will write the string in the "lines" list to the file "myfile.txt"
    f.writelines(lines)                            #and \n add new line characters to the end of string
    f.close() 
    
    #Add a new line
    fl=open("myfile.txt","w")
    lines=["line 1","line 2 ", "line 3"]
    for line in lines:
     fl.write(line + '\n')
    fl.close()
    
    
         
File_Handling()

         