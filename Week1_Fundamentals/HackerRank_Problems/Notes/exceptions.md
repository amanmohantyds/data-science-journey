    #Core exceptions to know (use these 90% of the time)
ValueError – invalid value for a function
TypeError – wrong data type
KeyError – dictionary key doesn't exist
IndexError – list index out of range
AttributeError – object has no attribute
NameError – variable not defined
ZeroDivisionError – division by zero
FileNotFoundError – file doesn't exist
ImportError – module not found
RuntimeError – general runtime problem



NOTE:- 

for regex
  use re.compile
  
if you write 
  except:          # you tell it to catch ANY exception
   error condition        # do nothing with this line
  print(false)


  so write like this 
  except (error condition):   #it runs this block only id the specific error condition is there
   print(False)