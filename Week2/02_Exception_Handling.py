def Exception_Handling():
 try:
    print(x)
 except:
    print("An exception occurred")


 try:
    print(x)
 except NameError:
    print("Variable x is not defined")
 except:
    print("Something else went wrong")  
    
    
 try:
    print(x)
 except:
    print("Something went wrong")
 finally:                                 
    print("The 'try except' is finished")  

 k = -1
 if k < 0:
   raise Exception("Sorry, no numbers below zero")


 #You can define what kind of error to raise, and the text to print to the user
 x = "hello"
 if not type(x) is int:
  raise TypeError("Only integers are allowed")

Exception_Handling()