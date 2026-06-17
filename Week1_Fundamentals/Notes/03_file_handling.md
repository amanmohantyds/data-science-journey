    
    #File Handling
-> The key function for working with files in Python is the open() function.
-> The open() function takes two parameters; filename, and mode.
-> There are four different methods (modes) for opening a file:
       i) "r" - Read - Default value. Opens a file for reading, error if the file does not exist
       ii) "a" - Append - Opens a file for appending, creates the file if it does not exist
       iii) "w" - Write - Opens a file for writing, creates the file if it does not exist
       iv) "x" - Create - Creates the specified file, returns an error if the file exists

-> In addition you can specify if the file should be handled as binary or text mode  
       i) "t" - Text - Default value. Text mode
       ii) "b" - Binary - Binary mode

    -> Syntax:- f = open("demofile.txt", "rt")

        Example:-
         f = open("demofile.txt")
                  print(f.read())
                  f.close()

    #Using the 'with' statement  
->When you do not have to worry about closing your files, the with statement takes care of that.

   Example:- 
    with open("demofile.txt") as f:
    print(f.read())

-> By default the read() method returns the whole text, but you can also specify how many characters you want to return:

   Example:-
    with open("demofile.txt") as f:
    print(f.read(5))

    # Read Lines Method:
   ->You can return one line by using the readline() method and by calling it two times,  you can read first two lines

-> By looping through the lines of the file, you can read the whole file, line by line:

   Example:-
   with open("demofile.txt") as f:
   for x in f:
   print(x)

   

    #To Read lines One by One from a file 
   f = open("file.txt","r")
   while True:
      line = f.readline()
      if not line:
        break
      print(line)  


    # writelines() method
   ->It is a method in python that  write a sequence of string to a file. Sequence can be iterable object, such as list, or a tuple
     Example:-
     f=open{"myfile.txt","w"}
     lines=["line 1\n","line \2", "line \3"]      #This will write the string in the "lines" list to the file "myfile.txt"
     f.writelines(lines)                            and \n add new line characters to the end of string
     f.close()       

   -> "writelines() method" does not add newline characters between the string in the sequence.
       You have to do it by your self like this:
       Example:
       f=open("myfile.txt","w")
       lines=["line 1","line 2 ", "line 3"]
       for line in lines:
         f.write(line + '\n')
       f.close()  

    # Write to an Existing File
   Example:-
   with open("demofile.txt", "a") as f:         (append at the end of content)
   f.write("Now the file has more content!")
   
   0r
   with open("demofile.txt", "w") as f:         (Overwrite the content)
   f.write("Woops! I have deleted the content!")

    # Delete a file
   To delete a file, you must import the OS module, and run its os.remove() function:

   Example:-
   import os
   os.remove("demofile.txt")

   ->Check if file exist:

   Example:-
   import os
   if os.path.exists("demofile.txt"):
     os.remove("demofile.txt")
   else:
     print("The file does not exist")

-> To delete the folder:
    use the "os.rmdir()" method:

   Example:-
    import os
    os.rmdir("myfolder")
   


     



