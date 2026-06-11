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
    y=int(float("1.123")) #float to integer
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
    
    
    
    
    #1.join
    myTuple = ("John", "Peter", "Vicky")
    x = "A".join(myTuple)
    print(x) #prints JohnAPeterAVicky
    
    
    
    
    #join() using directory
    myDict = {"name": "John", "country": "Norway"}
    mySeparator = "TEST"
    xl = mySeparator.join(myDict)
    print(xl)   #prints nameTESTcountry
    
    
    
    
    #2.find()
    txt = "Hello, welcome to my world."
    xr = txt.find("welcome")
    print(xr)  #Prints -> 7
    
    
    
    
      #3.string.find(value, start, end)
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
    print(c)  #prints Bob Alice
    
    
    
    
    print("-----------------------------------------------------------------")
    print("Formatting Strings")
    print("-----------------------------------------------------------------")
    
    
    
    
    #Format Strings
    d=8
    j=f"sorry to say but my gpa is {d}"
    print(j) #f-string (it helps to print an integer in a string output )
    t=f"sorry to say but my gpa is {d:.3f}"
    print(t) #f-string with 3 decimal places (print sorry to say but my gpa is 8.000)
    
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
    
    
    
    
    print("------------------------------------------------------------------")
    print("Arithmetic Operator")
    print("------------------------------------------------------------------")
    
    
    
    
   #Arithmetic Operators
      #we know the basic ones so i liked below are extras
      
    #1.division
    a = 12
    b = 3
    print(a / b) #print 4
    
    #2.Modulus
    c = 5
    d = 2
    print(c % d) #print 1
    
    #3.Floor Division
    e = 15
    f = 2
    print(e // f) #print 7
    #the floor division // rounds the result down to the nearest whole number
    
    #4.Exponential
    v = 2
    m = 5
    print(v ** m) #same as 2*2*2*2*2
    
    
    
    
    print("------------------------------------------------------------------")
    print("Ternary Operator")
    print("------------------------------------------------------------------")
    
    
    
    
    #Ternary Operators( i.e. if else)
    # 1.
    numb = 6
    xp = "WEEKEND!" if numb > 5 else "Workday"
    print(xp)  #prints WEEKEND!
    
    # 2.
    num = 6
    x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
    print(x)  #prints Sat
    
    
    
    
    print("------------------------------------------------------------------")
    print("Comparison Operator")
    print("------------------------------------------------------------------")
    
    
    
    
    #Comparison Operator
    #1.
    xc = 5
    yk = 3

    print(xc == yk)  #prints false
    print(xc!= yk)  #prints true
    print(xc> yk)   #prints true
    print(xc< yk)   #prints false
    print(xc>= yk)  #prints true
    print(xc<= yk)  #prints false
    
    #2. connecting
    x = 5

    print(1 < x < 10)  #true
    print(1 < x and x < 10)  #true
    
    
    
    
    print("------------------------------------------------------------------")
    print("Logical Operator")
    print("------------------------------------------------------------------")
    
    
    
    
    #Logical Operator
    
    #1.and -->(Returns True if both statements are true)
    xw = 5
    print(xw > 0 and xw < 10)  #prints true
    
    #2.or --> (Returns True if one of the statements is true)
    xe = 5
    print(xe < 5 or xe > 10) #prints false
    
    #3.not --> (Reverse the result, returns False if the result is true)
    xg = 5
    print(not(xg > 3 and xg < 10)) # prints false
    
    
    
    
    print("------------------------------------------------------------------")
    print("Identity Operator")
    print("------------------------------------------------------------------")
    
    
    
    
    #Identity Operator
    
    #1.is -->(Returns True if both variables are the same object)
    xx = ["apple", "banana"]
    yy = ["apple", "banana"]
    zz = xx

    print(xx is zz)  #prints true
    print(xx is yy)  #prints false
    print(xx == yy)  #prints false
    
    #2.is not -->Returns True if both variables are not the same object
    bb = ["apple", "banana"]
    vv = ["apple", "banana"]

    print(bb is not vv) #prints true
    
    
    # 3.Point To Be Noted ( Difference Between is and == ):-
      # is - Checks if both variables point to the same object in memory
      # == - Checks if the values of both variables are equal
    ee = [1, 2, 3]
    rr = [1, 2, 3]

    print(ee == rr) #true
    print(ee is rr)  #false
    
    
    
    
    print("------------------------------------------------------------------")
    print("Membership Operator")
    print("------------------------------------------------------------------")
    
    
    
    
    #Membership Operator
    
    #1.in--> (Returns True if a sequence with the specified value is present in the object)
    fru = ["apple", "banana", "cherry"]
    print("banana" in fru)  #true
    
    #2.not in -->(Returns True if a sequence with the specified value is not present in the object)
    fr = ["apple", "banana", "cherry"]
    print("pineapple" not in fr)  #true


Details()