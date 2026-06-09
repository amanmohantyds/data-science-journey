def Details():
    print("----------------------------------------------------------------")
    print("types of data")
    print("---------------------------------------------------------------")
    #types of data
    age = 18 #integer
    height = 150.9 #float
    name = "Aman" #string
    is_student = True #boolean
    
    print("My name is", name, "My age is", age, "and my height is", height)
    
    print("----------------------------------------------------------------")
    print("type casting")
    print("---------------------------------------------------------------")
    
    #type casting 
    x=str(0.123) #float to string
    y=int("1.123") #float to integer
    z=float(5) #integer to float
    l=str("king") #string to string
    print(x,y,z,l) 
    print(int(35.8)) #float to integer
    
    print("-----------------------------------------------------------------")
    print("String")
    print("-----------------------------------------------------------------")
    
    #String 
    xs="Aman","Ram","Sham"
    print(xs[0]) #indexing
    print(xs[0:5]) #slicing from index 0 to 5 and excluding 5
    print(xs[1:3]) #slicing from index 1 to 3 and excluding 3
    print(xs[-1]) #negative indexing
    
    print("-----------------------------------------------------------------")
    print("Modifying String")
    print("-----------------------------------------------------------------")
    
    #Modifying string
    n=" Aman Mohanty "
    s=" Hi,hello,how,are,you "
    print(n.upper()) #upper case
    print(n.lower()) #lower case
    print(n.replace("Aman", "Ram")) #replace
    print(n.strip()) #remove whitespace
    print(s.split(",")) #split string into list
    
    print("---------------------------------------------------------------")
    #String methods
    print("---------------------------------------------------------------")
    
    #1join
    myTuple = ("John", "Peter", "Vicky")
    x = "A".join(myTuple)
    print(x) #prints JohnAPeterAVicky
    
    #join() using directory
    myDict = {"name": "John", "country": "Norway"}
    mySeparator = "TEST"
    xl = mySeparator.join(myDict)
    print(xl)   #prints nameTESTcountry
    
    #find()
    txt = "Hello, welcome to my world."
    xr = txt.find("welcome")
    print(xr)  #Prints -> 7
    
      #string.find(value, start, end)
    tx = "Hello, welcome to my world."
    qx = tx.find("e", 5, 10)
    print(qx)  
      #if not found returns -1 but if in index() if not found returns an exception
      
    print("---------------------------------------------------------------")
    print("String concatenation")
    print("----------------------------------------------------------------")
    
    #String concatenation
    a="Bob"
    b="Alice"
    c=a+" "+b
    print(c)
    
    print("-----------------------------------------------------------------")
    print("Formatting Strings")
    print("-----------------------------------------------------------------")
    
    #Format Strings
    d=8
    print(f"sorry to say but my gpa is {d}") #f-string
    print(f"sorry to say but my gpa is {d:.3f}") #f-string with 3 decimal places
    
    a=19
    an=f"hi my age is {a}"
    print(an)
    
    t=56
    ak=f"hi my age is {a} and my gpa is {d} and i have {t:.1f} friends"
    print(ak)
    bn=f"price of new headphone is {45*8} rupees"
    print(bn)
    
    print("------------------------------------------------------------------")
    print("Escape characters")
    print("------------------------------------------------------------------")
    
    #Escape characters
    print("they were so called\"Vikings\"") #escape double quote
    print("they were so called\\ Vikings \\") #escape backslash
    print("they were so called\nVikings") #escape newline
    print("they were so called\tVikings") #escape tab
    
    
    print("------------------------------------------------------------------")
    print("True or False")
    print("------------------------------------------------------------------")
    
    #True of False
    a = 200
    b = 33
    if b > a:
      print("b is greater than a")
    else:
      print("b is not greater than a")
    
    #The bool() function allows you to evaluate any value, and give you True or False in return
    xv = "Hello"
    yr = 15
    print(bool(xr))
    print(bool(yr))
    
   #Arithmetic Operators
      #we know the basic ones so i liked below are extras
      
    #division
    a = 12
    b = 3
    print(a / b) #print 4
    
    #Modulus
    c = 5
    d = 2
    print(c % d) #print 1
    
    #Floor Division
    e = 15
    f = 2
    print(e // f) #print 7
    #the floor division // rounds the result down to the nearest whole number
    
    #Exponential
    v = 2
    m = 5
    print(v ** m) #same as 2*2*2*2*2
    
    
Details()