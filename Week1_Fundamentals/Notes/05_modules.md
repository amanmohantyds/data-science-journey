    #Module
    It is same as same as a code library
    You can name the module file whatever you like, but it must have the file extension .py

   lets,
    Save this code Below in a file named mymodule.py
    def greeting(name):
      print("Hello, " + name)

   Now we can use the module we just created, by using the import statement:

   import mymodule
   mymodule.greeting("Jonathan")           #Note:- When using a function from a module, 
                                                   use the syntax: module_name.function_name.  


    #Variables in Module
    It can contain variables of all types (arrays, dictionaries, objects etc)

   -> You can use it to call the value from the directory using the key and import module

   -> You can create an alias when you import a module, by using the "as" keyword
       Example:
        import myfile.py as f
        then use, f.function_name
    
   -> There are several built-in modules in Python, which can be called whenever you like


    #dir() Function
   ->List all the defined names belonging to the module
       syntax: dir(module_name)

    #Import from the module
   -> You can choose to import only parts from a module, by using the from keyword
     Example:
     The module named mymodule has one function named "greetings" and one dictionary names "person1"
     from mymodule import person1
      print(person1["age"])