    
    #Exception Handling
   -> The 'try' block lets you test a block of code for errors.
   -> The 'except' block lets you handle the error.
   -> The 'else' block lets you execute code when there is no error
   -> The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

   #Example:
   i)The try block will generate an exception, because x is not define
   try:
     print(x)
   except:
     print("An exception occurred")

   ii)Print one message if the try block raises a NameError and another for other errors:
   try:
     print(x)
   except NameError:
     print("Variable x is not defined")
   except:
     print("Something else went wrong")
    
    #Finally
   try:
     print(x)
   except:
     print("Something went wrong")
    finally:                                 #prints-> Something went wrong
                                               The 'try except' is finished
     print("The 'try except' is finished")


   i)Try to open and write to a file that is not writable:
    try:
      f = open("demofile.txt")
      try:
        f.write("Lorum Ipsum")                                 Here, the program can continue, without leaving the file object open.
      except:
        print("Something went wrong when writing to the file")  
      finally:
        f.close()
    except:
      print("Something went wrong when opening the file") 


    #Raising an exception
   ->As a Python developer you can choose to throw an exception if a condition occurs
   ->To throw (or raise) an exception, use the raise keyword


