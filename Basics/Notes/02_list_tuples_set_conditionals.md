      #TOPIC-1(lIST)

   #written with sq. brackets -> []
   ->It is used to store multiple items in a single variable
   ->List items are ordered, changeable, and allow duplicate values.
   ->len() → number of items
   ->list() constructor can create a list from another iterable
   ->List items are indexed, the first item has index [0], the second item has index [1] etc.
   ->It is Indexed

    #Input methods
   -> x = input("prompt")
   -> x = int(input().strip()) — removes extra spaces before converting
   -> x = int(input()) — single integer input
   -> x, y = input().split() — multiple inputs
   -> x, y = map(int, input().split()) — multiple integer inputs

    #Access

   -> a[1] → access by index
   -> b[-1] → negative indexing (last item)
   -> L[2:5] → slicing; includes index 2, excludes index 5


    #example of negetive indexing and positive indexing
   le = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
   print(le[-4:-1])  #prints-> ('orange', 'kiwi', 'melon')     #(new)
   print(le[1:4])    #prints-> ("banana", "cherry", "orange")

    #Negative indexing means starting from the end of the tuple.
   #This example returns the items from index -4 (included) to index -1 (excluded)
   #Remember that the last item has the index -1   



    #Changing Items

   -> Direct: c[1] = "new_value"
   -> Range replace: d[1:3] = ["x", "y"] — replaces a slice; if you insert more items than you replace, remaining items shift accordingly
   -> Here '3' is not included

    #Adding Items
   -> .append(item) → adds at the end
   -> .insert(index, item) → adds at specific position
   -> .extend(iterable) → adds elements from another iterable (not just lists — can be tuples, sets, dicts, etc.)
   -> Difference from .append(): .append() adds the whole object as ONE item; .extend() unpacks and adds each element individually

    #Removing Items

   -> .remove(value) → removes first matching value
   -> .pop(index) → removes item at index (or last item if no index given)
   -> del list[index] → removes item at index (uses [])
   -> del list → deletes the entire list object
   -> .clear() → empties the list (keeps the object, just empty)

    #Other Methods (noted but not demoed)

   ->.copy() → returns a copy of the list
   ->.count(value) → counts occurrences
   ->.reverse() → reverses order in place
   ->.sort() → sorts in place

    #General Notes

   -> Check if a number is in a range: num in range(x, y) → x included, y excluded (equivalent to x <= num < y)
   -> Check odd number: n % 2 != 0 or n % 2 == 1
   -> To find the range :  range(stop)  or  range(start, stop)  or  range(start, stop, step)
   -> Reverse range: range(start, 0, -1) — start is the highest number
   -> Python does not use = inside a for loop header


    #TOPIC-2(TUPLES)
   -> written with round brackets -> ()
   -> Tuples are used to store multiple items in a single variable.
   -> It is a collection which is ordered and unchangeable ie cannot be added or removed
   -> It is Indexed

    #Unpacking
   ->In Python, we are also allowed to extract the values back into variables. This is called "unpacking"

      ta = ("apple", "banana", "cherry")
      (green, yellow, red) = ta
      print(green)
      print(yellow)
      print(red) 

   ->  #Note: The number of variables must match the number of values in the tuple, if not, you must use an 
           # asterisk to collect the remaining values as a li

   -> (g, y, *r) = tz → r becomes a list of all remaining items
   -> * can be placed on any variable (not just last) — Python assigns values until the remaining count matches the remaining variables:

   -> (gr, re, *tr) = s → gr gets first item, re gets last item, tr gets everything in between as a list

    Example of Using an Asterisk
   tz = ("apple","banana","cherry","strawberry","raspberry")
    (g,y,*r) =  tz
    print(g)
    print(y)
    print(r)  #prints -> #apple
                         #banana
                         #['cherry', 'strawberry', 'raspberry']


        #TOPIC-3(SETS)                  
   ->  Sets are written with curly brackets --> {}
    -> Sets are used to store multiple items in a single variable.
    -> A set is a collection which is unordered, unchangeable, unindexed and do not allow duplicate values.
    -> Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    -> Set items are unchangeable, but you can remove items and add new items   
    -> Set items can be of any data type i.e. string,int,boolean
    -> A single set can contain multiple data types  
    -> Note: the set list is unordered, meaning: the items will appear in a random order.
    
    #Basic example 
   set = {"apple", "banana", "cherry"}
    print(set)      #prints -> {"apple", "banana", "cherry"} OR {"cherry", "banana", "apple"} OR Any Patterns as Unordered


    #Duplicates not allowed:
   ti = {"apple", "banana", "cherry", "apple"}
    print(ti)       #prints -> {'banana', 'cherry', 'apple'}
    
    
    #Note:- " set() " can be used to remove the duplicates
    #Example:- scores=[2,4,5,3,3,1,1,2]  --> set(scores) --> [2,4,5,3,1]

   -> True and 1 are treated as the same value (duplicates)
   -> False and 0 are treated as the same value (duplicates)

    #Other Notes
   -> len(set) → number of items
   -> type(set) → <class 'set'>
   -> .add(item) → adds a single item
   -> .update(iterable) → merges another iterable into the set — does NOT have to be a set; can be a list, tuple, dict, etc.


    #Removing Items

   -> .remove(value) → raises an error if value not found
   -> .discard(value) → does NOT raise an error if value not found
   -> .pop() → removes and returns a random item (sets are unordered, so you can't predict which)
   -> .clear() → empties the set (set())
   -> del set_name → deletes the set entirely (accessing it after raises an error)



       #TOPIC-4(DIRECTORIES)
   -> Dictionaries are used to store data values in key:value pairs.
    ->Dictionaries are written with curly brackets, and have keys and values ->{"breed": "cats"}
    ->A dictionary is a collection which is ordered*,changeable and do not allow duplicate (my version is Python 3.14.5)
    ->As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    
    #Basic Example-
   dl = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
       }
    print(dl["brand"])  #prints -> Ford
                        #You can also use get() function like x=art.get("breed") -> print(x)


    #OTHER Points                      
   1.len() used to find length of directory   like print(length(art))
   2.The values in dictionary items can be of any data type:
   3.Use type() function to find data type
   4.Use dict() method to convert to directory

    #Access

  ->  dict["key"] → direct access
  -> .get("key")  → alternative access method         

    #Views (dynamic — update automatically when dict changes)

   -> .keys() → returns all keys
   -> .values() → returns all values
   -> .items() → returns key-value pairs as tuples    

    #Checking & Updating

   -> dict["key"] = new_value → changes value for existing key, or adds new key if it doesn't exist
       Example :- car["year"] = 2020
                  print(xe)              # prints ->dict_values(['Ford', 'Mustang', 2020])

   -> Get all values: values() returns an updating view:
     xe = car.values()      # print ->dict_values(['Ford', 'Mustang'])
  

  ->  .update({...}) → updates existing key or adds new key-value pair    
    Example:- car.update({"year": 2020})   # changes year
              car.update({"color": "red"}) # adds if new


    #Other Methods

   -> .pop(key) → removes specific key
   -> .popitem() → removes the last inserted key-value pair
   -> del dict[key] → removes specific key
   -> del dict → deletes entire dictionary
   -> .clear() → empties the dictionary
   -> dict.fromkeys(seq, value) → creates a new dict using seq as keys, all set to the same value (default None if value omitted)
   -> setdefault() method returns the value of the item with the specified key.
      #keyname -> 	Required. The keyname of the item you want to return the value from
      #value   ->   Optional.If the key exist, this parameter has no effect.
                            # If the key does not exist, this value becomes the key's value
                            #Default value None
                            

        #TOPIC-4(CONDITIONALS)     
    
   #Python If:-
    i) All other logical conditions are same like a == b,a != b,a < b,a <= b,a > b,a >= b,true,false
    ii) But here we take "if condition: " symbol instead of "if(condition)"
    iii) Here indentation is important ie give space before writing print line
    iv) We can have multiple statement (i.e. multiple print statement) in if block\


   print("Basic Example")
    a = 33
    b = 200
    if b > a:
     print("b is greater than a")  #prints-> b is greater than a
     
   Note:- Boolean variables can be used directly in if statements without comparison operators:
    is_logged_in = True
    if is_logged_in:
     print("Welcome back!")

    #Elif
   Like "else if" — written as elif
   Can chain multiple elifs; Python checks each in order and executes the first one that's true


    #Else
   Executes only if the if (and all elifs) are False

    #Short Hand If
   One-liner: if "condition": statement
   One-line if/else: print("A") if condition else print("B")  


    #Assign Value with If...Else (Ternary)
   Syntax: variable = value_if_true if condition else value_if_false


    #Multiple Conditions on One Line
   Can chain: print("A") if a > b else print("=") if a == b else print("B")
   Note: keep these short for readability



           


    
                             
