def List_Tuples_Set_Conditionals():
  
    
    #TOPIC-1(lIST)
   
    x=["car","bike","scooter"]
    print(x)    #prints--> ["car","bike","scooter"]
    
    y=[5, 6, 23]
    print(y)    #prints --> [5, 6, 23] 
    
    
    
    #Access List Items
  
    a = ["apple", "banana", "cherry"]
    print(a[1])  #prints --> banana
    

    b=["apple", "banana", "cherry"]
    print(b[-1]) #prints --> cherry
    
   
         
    L = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(L[2:5]) 
 
    c = ["apple", "banana", "cherry"]
    c[1] = "blackcurrant"
    print(c)          
    
    
    
  
    d = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    d[1:3] = ["blackcurrant", "watermelon"]
    print(d)            #prints -->['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
    
    
    
   
    
    st = ["apple", "banana", "cherry"]
    st.append("orange")
    print(st)            #prints-> ['apple', 'banana', 'cherry', 'orange']
    
    
    
   
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)      #print-> ['apple', 'orange', 'banana', 'cherry']
    
    
    
 
    print()
    th = ["apple", "banana", "cherry"]
    tr = ["mango", "pineapple", "papaya"]
    th.extend(tr)
    print(th)            #print-> ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
    
    
    
   
    tlist = ["apple", "banana", "cherry"]
    tuple = ("kiwi", "orange")
    tlist.extend(tuple)
    print(thislist)     #print ->['apple', 'banana', 'cherry', 'kiwi', 'orange']
    
  
    #Remove
   
    y=["Hi,","Welcome","to","candy","town"]
    y.remove("Hi,")
    print(y)  #print ->["Welcome","to","candy","town"]
    
    
    
   
    y = ["Ho", "Welcome", "to", "urban", "town"]
    y.pop(0)           # removes "Ho"
   
    print(y)           # ['Welcome', 'to', 'urban', 'town']                 
    
    
    
    
    k = ["apple", "banana", "cherry"]
    del k[0]
    print(k)
    
    
  
    r = ["apple", "banana", "cherry"]
    del r
    # print(r)         
    
    
    
    
    dl = ["apple", "banana", "cherry"]
    dl.clear()
    print(dl)
    

                
    #TOPIC-2(TUPLES)

    tuple= ("apple", "banana", "cherry", "apple", "cherry")
    print(tuple) # prints -> ("apple", 'banana', 'cherry', 'apple', 'cherry')
    
    
    le = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(le[-4:-1])  #prints-> ('orange', 'kiwi', 'melon')     #(new)
    print(le[1:4])    

                
    #Unpack Tuples
    ta = ("apple", "banana", "cherry")
    (green, yellow, red) = ta
    print(green)
    print(yellow)
    print(red)      
    
    
   
    tz = ("apple","banana","cherry","strawberry","raspberry")
    (g,y,*r) =  tz
    print(g)
    print(y)
    print(r)  #prints -> #apple
                         #banana
                         #['cherry', 'strawberry', 'raspberry']
                  
                  
                  
  
    s = ("apple", "mango", "papaya", "pineapple", "cherry")
    (gr, *tr, re) = s
    print(gr)
    print(tr)
    print(re)       #prints -> #apple
                               #['mango', 'papaya', 'pineapple']
                               #cherry
                               
    
    
    
   
    #TOPIC-3(SETS)                  
  
    set = {"apple", "banana", "cherry"}
    print(set)      #prints -> {"apple", "banana", "cherry"} OR {"cherry", "banana", "apple"} OR Any Patterns as Unordered
    
    
    
    ti = {"apple", "banana", "cherry", "apple"}
    print(ti)       #prints -> {'banana', 'cherry', 'apple'}
    
    

    tet = {"apple", "banana", "cherry", True, 1, 2}
    print(tet)      #prints -> {True, 2, 'banana', 'cherry', 'apple'}
    
    
   
    tel = {"apple", "banana", "cherry", False, True, 0}
    print(tel)      #prints -> {False, True, 'cherry', 'apple', 'banana'}
    
    
   
    ee = {"apple", "banana", "cherry"}
    print(len(ee))  #prints ->3
    
    
    
    
   
    ms = {"apple", "banana", "cherry"}
    print(type(ms))   #prints -> <class 'set'>
    
    vr={45,63,17}
    vc={12,53,11}
    vr.add(23)  
    vr.update(vc) 
    
   
    ta = {"apple", "banana", "cherry"}
    mq = ["kiwi", "orange"]
    ta.update(mq)
    print(ta)    #prints -> {'banana', 'cherry', 'apple', 'orange', 'kiwi'}
    
  
    #REMOVE-
   
 
    f={"green","yellow","teal"}
    f.remove("teal")              #prints -> {"green","yellow"}
    print(f)
    
    fx={"green","yellow","teal"}   
    fx.discard("orange")          


    u = {"apple", "banana", "cherry"}
    p = u.pop()     
    print(p)     
    print(u)     
    
    
    tw = {"apple", "banana", "cherry"}
    tw.clear()
    print(tw)  #prints -> set()


   
    #TOPIC-4(DIRECTORIES)
 
    print("basic example")
    dl = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(dl["brand"])  #prints -> Ford
                        #You can also use get() function like x=art.get("breed") -> print(x)
    
    
    #Duplicates not allowed:
    print("Duplicates not allowed:")
    sd ={
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964,
          "year": 2020
        }
    print(sd)   #prints -> {
                           # "brand": "Ford",
                           # "model": "Mustang",
                           # "year": 1964,
                           # "year": 2020
                           #}

    car = {"brand": "Ford", "model": "Mustang"}
    xb = car.keys()        
    car["color"] = "white"
    print(xb)              # prints ->dict_keys(['brand', 'model', 'color'])
    
    
    xe = car.values()     
    car["year"] = 2020
    print(xe)              # prints ->dict_values(['Ford', 'Mustang', 2020])
    
    
    xi = car.items()       
    car["color"] = "red"
    print(xi)              # ('color','red')
    
    
   
    if "model" in car:
     print("Yes")
     
     
   
    car["year"] = 2018
    print(car)
    
    
    
    car.update({"year": 2020})   # changes year
    car.update({"color": "red"}) # adds if new
    
 
    x = ('key1', 'key2', 'key3')
    y = 0
    asd = dict.fromkeys(x, y)
    print(asd)   #prints -> {'key1': 0, 'key2': 0, 'key3': 0}
    
    ak= dict.fromkeys(x)
    print(ak)    #prints -> {'key1': None, 'key2': None, 'key3': None}
    
 
    #TOPIC-4(CONDITIONALS)     
   
    print("Basic Example")
    a = 33
    b = 200
    if b > a:
     print("b is greater than a")  #prints-> b is greater than a
     
    #v)Boolean variables can be used directly in if statements without comparison operators:
    is_logged_in = True
    if is_logged_in:
     print("Welcome back!")
 
 
 
  #)It is similar to "elseIf statement" but here we write "elif" statement:
    jul = 33
    bul = 33
    if bul > jul:
     print("bul is greater than jul")
    elif jul == bul:
     print("jul and bul are equal")
     
     score = 75
    if score >= 90:
     print("Grade: A")
    elif score >= 80:
     print("Grade: B")
    elif score >= 70:
     print("Grade: C")
    elif score >= 60:
     print("Grade: D")   #print-> Grade: C
     
  
    #Else Statement
    a = 200
    b = 33
    if b > a:
     print("b is greater than a")
    elif a == b:
     print("a and b are equal")
    else:
     print("a is greater than b")  #prints->a is greater than b
     
     
 
    #Short Hand if
    mia=15
    lia=19
    if mia>lia: print("mia is a teenager")
    
    abel=14
    tom=19
    print("tom is a teenager") if(abel<tom) else print("abel is a teenager")
    
    
    
    
    #Assign a value with If .. Else
   
    a = 10
    b = 20
    bigger = a if a > b else b
    print("Bigger is", bigger)   #prints-> Bigger is 20

    #Multiple Conditions on One Line

    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")  #prints-> =
 
    # Combined Conditions with and/or
   
    score = 50
    submitted_project = True

    if score >= 90 and submitted_project:
      print("A+")
    elif score >= 90:
      print("A")
    elif score >= 80:
      print("B")
    elif score >= 70:
      print("C")
    elif score >= 60 or submitted_project:
      print("D")
    else:
      print("F")
    
    
    # Traditional If-Elif Version

    country = "USA"

    if country == "United States":
      print("US")
    elif country == "India":
      print("IN")
    elif country == "Egypt":
      print("EG")
    elif country == "Germany":
      print("DE")
    else:
      print("Unknown Country")
      
    # match-case Version
    # Cleaner and more readable for many conditions.
    
    country = "USA"

    match country:

       case "United States" | "USA":
         print("US")

       case "India":
         print("IN")

       case "Egypt":
         print("EG")

       case "Germany":
         print("DE")

       case _:
         print("Unknown Country")
    
    
    
    # Example 2: HTTP Status Handler
    # Handle response codes from an API.

    status_code = 404

    match status_code:

      case 200:
          print("Request successful")

      case 400:
          print("Bad request")

      case 401:
          print("Unauthorized access")

      case 404:
          print("Resource not found")

      case 500:
          print("Internal server error")

      case _:
          print("Unhandled status code")
    
 
 
    # Independent Conditions
    score = 50
    submitted_project = True

    if score >= 90:
      print("High Score")
    else:
      print("Low Score")

    if submitted_project:
      print("Project is submitted")
    else:
      print("Project is not submitted") 
 
 
 
    
    # Cleaning Data Inside a Loops
    # Cleaning file names before processing them.

    files = [' Report.csv ', 'DATA.csv ', ' final.TXT']

    for file in files:
       file = file.strip().lower().replace('.txt', '.csv')
       print(f"Processing {file}")
    
    
    # Real-World Example (Security Check)
    # Stop processing if a suspicious input appears.
    emails = [
       'data@gmail.com',
       'baraa@outlook.de',
       'DROP TABLE USERS;',
       'maria@gmail.com'
    ]

    for email in emails:
        if ';' in email:
            print('SQL Injection: Hacker Attack')
            break
        print(f'Processing Email: {email}')
 
 
   # Nested Loop (2 Levels)
    for xi in range(3):  # outer loop
      for yi in range(2):  # inner loop
        print(f"({xi}, {yi})")
    
   # Nested Loop (3 Levels)
    for a in range(3):  # outer loop
      for b in range(2):  # inner loop
        for c in range(2):
            print(f"({a}, {b}, {c})")   
            
    
    
           
        
        
        
    # Real-World Example (File Generation)
    # Generating file names dynamically using years, months, and days.
    years = [2026, 2027]
    months = ['Jan', 'Feb']
    days = range(1, 29)

    for yr in years:
      for mn in months:
        for dy in days:
            print(f'report_{yr}_{mn}_{dy}.csv')
            
            
            
    # Real-World Example (SQL Generation)
    # Automatically generating SQL queries for multiple tables and columns.
    tables = ['customers', 'orders', 'products', 'prices']
    columns = ['id', 'create_date']

    for t in tables:
      for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')        
    
        
List_Tuples_Set_Conditionals()    