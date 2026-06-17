def Comprehensions_and_Lamda():
    #Topic_1:List Compression
    
    
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]    # prints the entire list
    newlist = [x for x in fruits]
    print(newlist)   
    
    fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
    nl = [x for x in fruits if x != "apple"]
    print(nl)   # prints-> ['banana', 'cherry', 'kiwi', 'mango']
    
    newlist2 = [x for x in range(10)]
    print(newlist2)   #prints-> numbers from 0 to 9
    
    newlist3 = [x for x in range(10) if x<5]
    print(newlist3)
    
    newlist4 = [x.upper() for x in fruits] 
    print(newlist4)
    
    newlist5 = [x*x for x in range(5)] 
    print(newlist5)          #prints: [0,1,4,9,16]
    
    newlist6 = ["hello" for x in fruits]
    print(newlist6)          #Where there was a item in fruits ,it prints "hello"
    
    newlist7 = [x if x != "banana" else "orange" for x in fruits]
    print(newlist7)        #if-else inside a for-loop 
    
                      
                       
    #Topic_2:Lamda Functions
    #-> The power of lambda is better shown when you use them as an anonymous function inside another function
    
    
    double=lambda x: x * 2
    avg=lambda x,y: x+y/2
    
    #using map()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    doubled = list(map(lambda x: x * 2, numbers))
    print(doubled)                   # doubles all the number in the list
    
    """ 
      What is map() ?
       ->syntax: map(function, iterable) 
       ->Apply this function to every item in the list.
        Example:-
        names = ["Aman", "Rahul", "Priya"]
        result = map(len, names)
        print(list(result))  #prints->[4, 5, 5]
       
    """
    #using filter() :  creates a list of items for which a function returns True
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(odd_numbers)               
    
    #using sorted() :  uses a lambda as a key for custom sorting
    students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
    sorted_students = sorted(students, key=lambda x: x[1])
    print(sorted_students)           #For every tuple, use the value at index 1 (the age) for sorting
    
    words = ["apple", "pie", "banana", "cherry"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)             #Sort strings by length
Comprehensions_and_Lamda()