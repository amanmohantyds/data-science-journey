1)     #Input Method
     # x = input("Enter the name or thing")
    
    #For removing extra space in input
     # x = int(input().strip())
    
    #For Single integer input
     # x=int(input())
    
    #For multiple input
     # x,y=input().split()
    
    #For multiple integer input
     # x, y = map(int, input().split())
    
    #for multiple input
     # n = int(input().strip())

2)     #type casting 
    x=str(0.123) #float to string

    y=int(float("1.123"))    #float to integer
    z=float(5)               #integer to float
    l=str("king")            #string to string
    
    print(x,y,z,l) 
    print(int(35.8)) #float to integer     

3)     #String 
    xs="Aman","Ram","Sham"
    print(xs[0]) #indexing
    print(xs[0:5]) #slicing from index 0 to 5 and excluding 5
    print(xs[1:3]) #slicing from index 1 to 3 and excluding 3
    print(xs[-1]) #negative indexing   

    i)    #Modifying string

    n=" Aman Mohanty "
    s=" Hi,hello,how,are,you "

    print(n.upper())                  #upper case
    print(n.lower())                  #lower case
    print(n.replace("Aman", "Ram"))   #replace
    print(n.strip())                  #remove whitespace
    print(s.split(","))               #split string into list     

2)     #String Methods

    #i).join
        myTuple = ("John", "Peter", "Vicky")
        x = "A".join(myTuple)
        print(x) #prints JohnAPeterAVicky     #Note:- Can be used to insert something within every item of list/tuple etc
    
    
    
    
    #join() using directory
        myDict = {"name": "John", "country": "Norway"}
        mySeparator = "TEST"
        xl = mySeparator.join(myDict)
        print(xl)   #prints nameTESTcountry
    
    
    
    
    #ii).find()
        txt = "Hello, welcome to my world."
        xr = txt.find("welcome")
        print(xr)  #Prints -> 7          #Note:- Can be used for Finding at which index is a Item Present
    
    
    
    
      #iii).string.find(value, start, end)

       tx = "Hello, welcome to my world."
       qx = tx.find("e", 5, 10)
       print(qx)  
        #if not found returns -1 but if in index() if not found returns an exception


3)     #String concatenation
    a="Bob"
    b="Alice"
    c=a+" "+b
    print(c)  #prints Bob Alice 



4)     #Format Strings
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


5)     #Escape characters
    print("they were so called\"Vikings\"")      #escape double quote
    print("they were so called\\ Vikings \\")    #escape backslash
    print("they were so called\nVikings")        #escape ne        


6)     #Arithmetic Operators

    / → normal division
    % → modulus (remainder)
    // → floor division (rounds down to nearest whole number)
    ** → exponentiation (e.g., 2**5 = 2×2×2×2×2)    

7)     #Ternary / Conditional Expressions

    result = "A" if condition else "B"
    Chained: "X" if cond1 else "Y" if cond2 else "Z"


8)     #Comparison Operators

    ==, !=, >, <, >=, <=
    Chained condition: 1 < x < 10 is equivalent to 1 < x and x < 10


9)     #Logical Operators

   and → True if both conditions true
   or → True if at least one condition true
   not → reverses the result


10)     #Identity Operators (is vs ==) — Important distinction

   is → checks if two variables point to the same object in memory
   == → checks if the values are equal
   Example: two separate lists with identical contents → == is True, but is is False (different objects in memory)
   is not → True if variables are NOT the same object    

11)     #Membership Operators

   in → True if value exists in the sequence
   not in → True if value does NOT exist in the sequence      
