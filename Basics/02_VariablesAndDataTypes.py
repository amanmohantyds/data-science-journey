def Details():
 
    
    
    age = 18 #integer
    height = 150.9 #float
    name = "Aman" #string
    is_student = True #boolean
    
    print("My name is", name, "My age is", age, "and my height is", height)
    

     
    x=str(0.123) 
    y=int(float("1.123")) 
    z=float(5) 
    l=str("king") 
    print(x,y,z,l) 
    print(int(35.8)) 
    
  
     
    xs="Aman","Ram","Sham"
    print(xs[0]) 
    print(xs[0:5]) 
    print(xs[1:3]) 
    print(xs[-1]) 
    
    
    
    n=" Aman Mohanty "
    s=" Hi,hello,how,are,you "
    print(n.upper()) 
    print(n.lower()) 
    print(n.replace("Aman", "Ram")) 
    print(n.strip()) 
    print(s.split(","))
    
    
    myTuple = ("John", "Peter", "Vicky")
    x = "A".join(myTuple)
    print(x) 
    
    myDict = {"name": "John", "country": "Norway"}
    mySeparator = "TEST"
    xl = mySeparator.join(myDict)
    print(xl)   #prints nameTESTcountry

    txt = "Hello, welcome to my world."
    xr = txt.find("welcome")
    print(xr)  #Prints -> 7      
 
    tx = "Hello, welcome to my world."
    qx = tx.find("e", 5, 10)
    print(qx)  
    
    
    
    a="Bob"
    b="Alice"
    c=a+" "+b
    print(c)  #prints Bob Alice
    
    
 
  
    d=8
    j=f"sorry to say but my gpa is {d}"
    print(j) 
    t=f"sorry to say but my gpa is {d:.3f}"
    print(t) 
    
    a=19
    an=f"hi my age is {a}"
    print(an)
    
    t=56
    ak=f"hi my age is {a} and my gpa is {d} and i have {t:.1f} friends"
    print(ak)
    bn=f"price of new headphone is {45*8} rupees"
    print(bn)
    
    

    
    
    print("they were so called\"Vikings\"") 
    print("they were so called\\ Vikings \\") 
    print("they were so called\nVikings") 
    print("they were so called\tVikings") 
    
    
    


    a = 200
    b = 33
    if b > a:
      print("b is greater than a")
    else:
      print("b is not greater than a")
    
 
    xv = "Hello"
    yr = 15
    print(bool(xr))
    print(bool(yr))
    
    



    a = 12
    b = 3
    print(a / b) #print 4
    
  
    c = 5
    d = 2
    print(c % d) #print 1
    
   
    e = 15
    f = 2
    print(e // f) #print 7
   
    
  
    v = 2
    m = 5
    print(v ** m) #same as 2*2*2*2*2
    
    
 

    numb = 6
    xp = "WEEKEND!" if numb > 5 else "Workday"
    print(xp)  #prints WEEKEND!
    
  
    num = 6
    x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
    print(x)  #prints Sat
    
    

    
    xc = 5
    yk = 3

    print(xc == yk)  
    print(xc!= yk)  
    print(xc> yk)   
    print(xc< yk)   
    print(xc>= yk) 
    print(xc<= yk)  
   
    x = 5

    print(1 < x < 10)  #true
    print(1 < x and x < 10)  #true
    
 
    
   
   
    xw = 5
    print(xw > 0 and xw < 10)  #prints true
    
   
    xe = 5
    print(xe < 5 or xe > 10) #prints false
    
    
    xg = 5
    print(not(xg > 3 and xg < 10)) # prints false
    
    
   
 
    xx = ["apple", "banana"]
    yy = ["apple", "banana"]
    zz = xx

    print(xx is zz)  #prints true
    print(xx is yy)  #prints false
    print(xx == yy)  #prints false
    
    bb = ["apple", "banana"]
    vv = ["apple", "banana"]

    print(bb is not vv) #prints true
    
    
  
    ee = [1, 2, 3]
    rr = [1, 2, 3]

    print(ee == rr) 
    print(ee is rr)  
    

    
   
    fru = ["apple", "banana", "cherry"]
    print("banana" in fru)  #true
    

    fr = ["apple", "banana", "cherry"]
    print("pineapple" not in fr)  #true

    print("end")
Details()