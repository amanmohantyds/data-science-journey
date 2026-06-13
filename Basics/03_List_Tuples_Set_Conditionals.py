def List_Tuples_Set_Conditionals():
    
    #Input Method
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
     
    print("----------------------------------------------------------------")
    print("LIST")
    print("---------------------------------------------------------------")
    
    
    
    
    #TOPIC-1(lIST)
    #written with sq. brackets -> []
    #It is used to store multiple items in a single variable
    #List items are ordered, changeable, and allow duplicate values.
    #List items are indexed, the first item has index [0], the second item has index [1] etc.
    #It is Indexed




    print("----------------------------------------------------------------")
    print("types of data")
    print("---------------------------------------------------------------")
    
    
    
    
    
    #Basic Examples of List
    x=["car","bike","scooter"]
    print(x)    #prints--> ["car","bike","scooter"]
    
    y=[5, 6, 23]
    print(y)    #prints --> [5, 6, 23] 
    
    z= [True, False, False]
    print(z)    #prints --> [True, False, False]
    
    
    
    
    print("----------------------------------------------------------------")
    print("Access List")
    print("---------------------------------------------------------------")
    
    
    
    
    #Access List Items
    #1.first item with []
    a = ["apple", "banana", "cherry"]
    print(a[1])  #prints --> banana
    
    #2.last item [-ve]
    b=["apple", "banana", "cherry"]
    print(b[-1]) #prints --> cherry
    
                #list can be indexed ,which starts from zero and list allow duplicates
                # x[0] -> print first item,x[-1] -> print last item,and x[-2] -> print second last item
                #There is a method called "len()" which can be used to determine how many items a list has
                #They can be of any data type i.e. string,int,boolean
                #Use of list() -> It is also possible to use the list() constructor when creating a new list.
                
    #3.range [x:y]           
    L = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(L[2:5])  #prints ->['cherry', 'orange', 'kiwi']
                   #This will return the items from position 2 to 5.
                   #Remember that the first item is position 0,
                   #and note that the item in position 5 is NOT included





    print("----------------------------------------------------------------")
    print("Changing List items")
    print("---------------------------------------------------------------")
    
    
    
    
    #Change List Items
    
    #1. x[n]= " .."
    c = ["apple", "banana", "cherry"]
    c[1] = "blackcurrant"
    print(c)            #prints -->['apple', 'blackcurrant', 'cherry']
    
    
    
    #2.Change a Range of Item Values with [x:y]
    d = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    d[1:3] = ["blackcurrant", "watermelon"]
    print(d)            #prints -->['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
    
    
    
    #3.If you insert more items than you replace, the new items will be inserted where you specified, and 
        #the remaining items will move accordingly   
        
        
    
    #4.append() :add items at last
    st = ["apple", "banana", "cherry"]
    st.append("orange")
    print(st)            #prints-> ['apple', 'banana', 'cherry', 'orange']
    
    
    
    #5.insert() :add items at specific index using [index,item]
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)      #print-> ['apple', 'orange', 'banana', 'cherry']
    
    
    
    #6.extend() :add elements from another list to the current list
    print()
    th = ["apple", "banana", "cherry"]
    tr = ["mango", "pineapple", "papaya"]
    th.extend(tr)
    print(th)            #print-> ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
    
    
    
    #7.The extend() is not same as append()
       # In extend() you can add any iterable object (tuples, sets, dictionaries etc)
    tlist = ["apple", "banana", "cherry"]
    tuple = ("kiwi", "orange")
    tlist.extend(tuple)
    print(thislist)     #print ->['apple', 'banana', 'cherry', 'kiwi', 'orange']
    
    
    
    
    print("----------------------------------------------------------------")
    print("Remove")
    print("---------------------------------------------------------------")
    
    
    
    
    #Remove
    
    #1.remove()
    y=["Hi,","Welcome","to","candy","town"]
    y.remove("Hi,")
    print(y)  #print ->["Welcome","to","candy","town"]
    
    
    
    #2.pop() method: removes the specified index, example x.pop(1) remove second item and if nothing mentioned x.pop() 
                     #remove last item
    # use integer index or empty for last item
    y = ["Ho", "Welcome", "to", "urban", "town"]
    y.pop(0)           # removes "Ho"
    # or y.remove("Ho")
    print(y)           # ['Welcome', 'to', 'urban', 'town']                 
    
    
    
    #3.del keyword: also removes the specified index and it uses "[] symbol to specify index"
    k = ["apple", "banana", "cherry"]
    del k[0]
    print(k)
    
    
    
    #4.del keyword: also delete the list completely
    r = ["apple", "banana", "cherry"]
    del r
    # print(r)         
    
    
    
    #5.clear() method empties the list
    dl = ["apple", "banana", "cherry"]
    dl.clear()
    print(dl)
    
  #---------------------------------------------------------------------------------------
    
    
    
    
    #Rest Of Methods
    #1.copy() ->Returns a copy of the list
    #2.count() ->Returns the number of elements with the specified value
    #3.reverse() ->Reverses the order of the list
    #4.sort() ->Sorts the list
                 
    #To Check if a number is in a range of number:
    # num in range(x,y) 
    #Here "x" is included and "y" is excluded      
    # OR 
    # num1 <= x <= num2
    
    
    #To Check Odd Number
    # n % 2 != 0   OR  n % 2 == 1     
       
    #Range
     # range(stop)
     # range(start, stop)
    #Range that moves by 2 
     # range(start, stop, step)
    #Range in reverse 
     # range(start, 0, -1)  #here start is last number
     
     
     #Python do not use " = " symbol in for loop
                 
                 
    #---------------------------------------------------------------------------------------     
    
           
    print("----------------------------------------------------------------")
    print("TUPLES")
    print("---------------------------------------------------------------")
    
    
    
                
    #TOPIC-2(TUPLES)
    #written with round brackets -> ()
    #Tuples are used to store multiple items in a single variable.
    #It is a collection which is ordered and unchangeable ie cannot be added or removed
    #It is Indexed
    
    #Basic example
    tuple= ("apple", "banana", "cherry", "apple", "cherry")
    print(tuple) # prints -> ("apple", 'banana', 'cherry', 'apple', 'cherry')
    
    
    #Concept of indexing,negetive indexing,range of positive index are same as lists
    
    
    #example of negetive indexing and positive indexing
    le = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(le[-4:-1])  #prints-> ('orange', 'kiwi', 'melon')     #(new)
    print(le[1:4])    #prints-> ("banana", "cherry", "orange")

                   #Negative indexing means starting from the end of the tuple.
                   #This example returns the items from index -4 (included) to index -1 (excluded)
                   #Remember that the last item has the index -1
                   
    
    
    
    #Unpack Tuples
    #In Python, we are also allowed to extract the values back into variables. This is called "unpacking"
    ta = ("apple", "banana", "cherry")
    (green, yellow, red) = ta
    print(green)
    print(yellow)
    print(red)            
    
    
    #Note: The number of variables must match the number of values in the tuple, if not, you must use an 
           # asterisk to collect the remaining values as a list.    
    
    
    #Using an Asterisk
    tz = ("apple","banana","cherry","strawberry","raspberry")
    (g,y,*r) =  tz
    print(g)
    print(y)
    print(r)  #prints -> #apple
                         #banana
                         #['cherry', 'strawberry', 'raspberry']
                  
                  
                  
    #Special Case:-If the asterisk is added to another variable name than the last, Python will assign values to 
        #the variable until the number of values left matches the number of variables left.
        
    #Example is below-
    s = ("apple", "mango", "papaya", "pineapple", "cherry")
    (gr, *tr, re) = s
    print(gr)
    print(tr)
    print(re)       #prints -> #apple
                               #['mango', 'papaya', 'pineapple']
                               #cherry
                               
    
    
    
    print("----------------------------------------------------------------")
    print("SETS")
    print("---------------------------------------------------------------")
    
    
    
    
    #TOPIC-3(SETS)                  
    #Sets are written with curly brackets --> {}
    #Sets are used to store multiple items in a single variable.
    #A set is a collection which is unordered, unchangeable, unindexed and do not allow duplicate values.
    #Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    #Set items are unchangeable, but you can remove items and add new items   
    #Set items can be of any data type i.e. string,int,boolean
    #A single set can contain multiple data types  
    #Note: the set list is unordered, meaning: the items will appear in a random order.
    
    #Basic example 
    set = {"apple", "banana", "cherry"}
    print(set)      #prints -> {"apple", "banana", "cherry"} OR {"cherry", "banana", "apple"} OR Any Patterns as Unordered
    
    
    #Duplicates not allowed:
    ti = {"apple", "banana", "cherry", "apple"}
    print(ti)       #prints -> {'banana', 'cherry', 'apple'}
    
    #1.The values "True" and '1' are considered the same value in sets, and are treated as duplicates:
    tet = {"apple", "banana", "cherry", True, 1, 2}
    print(tet)      #prints -> {True, 2, 'banana', 'cherry', 'apple'}
    
    #2.The values "False" and '0' are considered the same value in sets, and are treated as duplicates:
    tel = {"apple", "banana", "cherry", False, True, 0}
    print(tel)      #prints -> {False, True, 'cherry', 'apple', 'banana'}
    
    #3.len() function is used to determine how many items a set has:
    ee = {"apple", "banana", "cherry"}
    print(len(ee))  #prints ->3
    
    
    #From Python's perspective, sets are defined as objects with the data type 'set'
    #Example is below
    ms = {"apple", "banana", "cherry"}
    print(type(ms))   #prints -> <class 'set'>
    
    #Add items in sets -> add() method
    #To Add items from another set use update() method ,example:
    vr={45,63,17}
    vc={12,53,11}
    vr.add(23)    #prints -> {45,63,17}
    vr.update(vc) #prints -> {11,45,63,12,53,17}
    
    #Objects in the update() method does not have to be a set,it can be any iterable object(tuples,lists,dictionaries etc)
    #Example Below:-
    ta = {"apple", "banana", "cherry"}
    mq = ["kiwi", "orange"]
    ta.update(mq)
    print(ta)    #prints -> {'banana', 'cherry', 'apple', 'orange', 'kiwi'}
    
    
    
    
    print("----------------------------------------------------------------")
    print("Remove")
    print("---------------------------------------------------------------")
    
    
    
    
    #REMOVE-
    
    
    #To remove an item in a set, use the "remove()", or the "discard()" method.
    # Example like 
    f={"green","yellow","teal"}
    f.remove("teal")              #prints -> {"green","yellow"}
    print(f)
    
    # If the item to remove does not exist, remove() "will" raise an error
     #prints -> error
    
    fx={"green","yellow","teal"}   # If the item to remove does not exist discard() "will NOT" raise an error
    fx.discard("orange")           #prints -> {"green","yellow","teal"} ,no errors
    print(fx)
    
    
    
    #You can also use the pop() method to remove an item, but this method will remove a random item,
      # so you cannot be sure what item that gets removed.
    #The return value of the pop() method is the removed item.
    #Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
    
    u = {"apple", "banana", "cherry"}
    p = u.pop()     
    print(p)        #removed item i.e. -> prints ->cherry
    print(u)        #prints the set after removal i.e. ->{'apple', 'banana'}
    
    #The clear() method empties the set:
    tw = {"apple", "banana", "cherry"}
    tw.clear()
    print(tw)  #prints -> set()
    
    #The del keyword will delete the set completely:
    #example:-
    #az={2,4,6,12}
    #del az 
    #print(az)  #prints -> error

    
    
    
    print("----------------------------------------------------------------")
    print("Directories")
    print("---------------------------------------------------------------")
    
    
    
    
    #TOPIC-4(DIRECTORIES)
    #Dictionaries are used to store data values in key:value pairs.
    #Dictionaries are written with curly brackets, and have keys and values ->{"breed": "cats"}
    #A dictionary is a collection which is ordered*,changeable and do not allow duplicate (my version is Python 3.14.5)
    #As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    
    #Basic Example-
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
                           
                           
    #OTHER Points                      
    #1.len() used to find length of directory   like print(length(art))
    #2.The values in dictionary items can be of any data type:
    #3.Use type() function to find data type
    #4.Use dict() method to convert to directory
    
    
    #5.The keys() method will return a list of all the keys in the dictionary:
    car = {"brand": "Ford", "model": "Mustang"}
    xb = car.keys()        # prints ->dict_keys(['brand', 'model'])
    car["color"] = "white"
    print(xb)              # prints ->dict_keys(['brand', 'model', 'color'])
    
    
    #6.Get all values: values() returns an updating view:
    xe = car.values()      # print ->dict_values(['Ford', 'Mustang'])
    car["year"] = 2020
    print(xe)              # prints ->dict_values(['Ford', 'Mustang', 2020])
    
    
    #7.Get all items: items() returns key-value pairs as tuples in a view:
    xi = car.items()       # dict_items([('brand','Ford'), ('model','Mustang')])
    car["color"] = "red"
    print(xi)              # ('color','red')
    
    
    #8.Check if key exists: Use in keyword:
    if "model" in car:
     print("Yes")
     
     
    #9.Change value: Assign new value to key:
    car["year"] = 2018
    print(car)
    
    
    #10.Update dictionary: update() with dict or iterable:
    car.update({"year": 2020})   # changes year
    car.update({"color": "red"}) # adds if new
    
    
    
    
    print("----------------------------------------------------------------")
    print("Methods")
    print("---------------------------------------------------------------")
    
    
    
    
    #1) .pop(key) removes specific key.
    #2) .popitem() removes last inserted 
    #3) del car[key] removes key.
    #4) del car deletes entire dict.
    #5) .clear() empties dict.
    
    #EXAMPLES:-
      #[ #1. car.pop("model")
         #2. car.popitem()
         #3. del car["year"]
         #4. car.clear()
      #]
    
    
    #5)fromkeys(seq, value) -> Creates a new dict with keys from seq and the same optional value.
    #key --> Required. An iterable specifying the keys of the new dictionary
    #value --> Optional. The value for all keys. Default value is None
    
    x = ('key1', 'key2', 'key3')
    y = 0
    asd = dict.fromkeys(x, y)
    print(asd)   #prints -> {'key1': 0, 'key2': 0, 'key3': 0}
    
    ak= dict.fromkeys(x)
    print(ak)    #prints -> {'key1': None, 'key2': None, 'key3': None}
    
    #6)setdefault() method returns the value of the item with the specified key.
      #keyname -> 	Required. The keyname of the item you want to return the value from
      #value   ->   Optional.If the key exist, this parameter has no effect.
                            # If the key does not exist, this value becomes the key's value
                            #Default value None
                            
    #7)values() method -> Returns a view of all values.   
    
    
    
    
    print("----------------------------------------------------------------")
    print("Conditionals")
    print("---------------------------------------------------------------")
    
    
    
    
    #TOPIC-4(CONDITIONALS)     
    
    #Python If:-
    #i)All other logical conditions are same like a == b,a != b,a < b,a <= b,a > b,a >= b,true,false
    #ii)But here we take "if condition: " symbol instead of "if(condition)"
    #iii)Here indentation is important ie give space before writing print line
    #iv)We can have multiple statement (i.e. multiple print statement) in if block
    
    print("Basic Example")
    a = 33
    b = 200
    if b > a:
     print("b is greater than a")  #prints-> b is greater than a
     
    #v)Boolean variables can be used directly in if statements without comparison operators:
    is_logged_in = True
    if is_logged_in:
     print("Welcome back!")
     
    
    
    
    print("----------------------------------------------------------------")
    print("Python Elif")
    print("---------------------------------------------------------------")
    
    
    
    
    #Python Elif 
    #i)It is similar to "elseIf statement" but here we write "elif" statement:
    jul = 33
    bul = 33
    if bul > jul:
     print("bul is greater than jul")
    elif jul == bul:
     print("jul and bul are equal")
     
     
    #ii)You can have as many elif statements as you need. Python will check each condition in order 
       # and execute the first one that is true:
    score = 75
    if score >= 90:
     print("Grade: A")
    elif score >= 80:
     print("Grade: B")
    elif score >= 70:
     print("Grade: C")
    elif score >= 60:
     print("Grade: D")   #print-> Grade: C
     
     
     
     
    print("----------------------------------------------------------------")
    print("Else Statement")
    print("---------------------------------------------------------------")
    
    
    
    
    #Else Statement
    #i)The else statement is executed when the if condition (and any elif conditions) evaluate to False:
    a = 200
    b = 33
    if b > a:
     print("b is greater than a")
    elif a == b:
     print("a and b are equal")
    else:
     print("a is greater than b")  #prints->a is greater than b
     
     
     
     
    print("----------------------------------------------------------------")
    print("Short Hand if")
    print("---------------------------------------------------------------")
    
    
    
    
    #Short Hand if
    mia=15
    lia=19
    if mia>lia: print("mia is a teenager")
    
    #i)If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
    abel=14
    tom=19
    print("tom is a teenager") if(abel<tom) else print("abel is a teenager")
    
    
    
    
    print("----------------------------------------------------------------")
    print("Assign a value with If .. Else")
    print("---------------------------------------------------------------")
    #Assign a Value With If ... Else
      #Syntax for the following pattern-->  variable = value_if_true if condition else value_if_false
    #Example:    
    a = 10
    b = 20
    bigger = a if a > b else b
    print("Bigger is", bigger)   #prints-> Bigger is 20
    
    
    
    
    print("----------------------------------------------------------------")
    print("Multiple Conditions on One Line")
    print("---------------------------------------------------------------")
    
    
    
    
    #Multiple Conditions on One Line:-
     #You can chain conditional expressions, but keep it short so it stays readable:
    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")  #prints-> =
     
     
     
     
     
    print("----------------------------------------------------------------")
    print("Practice")
    print("---------------------------------------------------------------")
    
    
    
    
     #Practice
      #loops
       #The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n, print i square.
       #Constraints:1<=n<=20
       
     
    
List_Tuples_Set_Conditionals()    