# ============================================
# PYTHON LIST OPERATIONS - COMPLETE REFERENCE
# ============================================

     -> 1. MODIFYING LIST ITEMS"

"-> 1.1 Change a single item using index"
my_list = ["apple", "banana", "cherry"]
my_list[1] = "blueberry"      # changes second item
print(my_list)                # ['apple', 'blueberry', 'cherry']

"-> 1.2 Change a range of items using [x:y]"
my_list = ["apple", "banana", "cherry", "orange", "kiwi"]
my_list[1:3] = ["blackberry", "melon"]   # replaces indices 1 and 2
print(my_list)                # ['apple', 'blackberry', 'melon', 'orange', 'kiwi']


     -> 2. ADDING ITEMS"

 -> 2.1 append() - adds item at the end"
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)                 # ['apple', 'banana', 'cherry', 'orange']

 -> 2.2 insert() - adds item at specific index (index, item)"
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)                 # ['apple', 'orange', 'banana', 'cherry']

 -> 2.3 extend() - adds elements from another iterable (list, tuple, set, dict)"
 -> NOTE: .extend() is NOT the same as .append()"
fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
print(fruits)                 # ['apple', 'banana', 'cherry', 'orange']

 -> extend() works with any iterable"
fruits = ["apple", "banana"]
fruits.extend(("cherry", "orange"))   # tuple
print(fruits)                 # ['apple', 'banana', 'cherry', 'orange']


     -> 3. REMOVING ITEMS"

 -> 3.1 remove() - removes first occurrence of a value"
y = ["Hi", "Welcome", "to", "candy", "town"]
y.remove("Hi")
print(y)                      # ['Welcome', 'to', 'candy', 'town']

 -> 3.2 pop() - removes item at specified index (or last if index not given)"
x = ["apple", "banana", "cherry", "date"]
x.pop(1)                      # removes second item ("banana")
print(x)                      # ['apple', 'cherry', 'date']
x.pop()                       # removes last item ("date")
print(x)                      # ['apple', 'cherry']

 -> 3.3 del keyword - removes specified index OR deletes entire list"
k = ["apple", "banana", "cherry"]
del k[0]                      # deletes "apple"
print(k)                      # ['banana', 'cherry']

# del k                       # uncomment to delete entire list
# print(k)                    # NameError: name 'k' is not defined

 -> 3.4 clear() - empties the list (but keeps the list object)"
k = ["apple", "banana", "cherry"]
k.clear()
print(k)                      # []


     -> 4. REMOVING DUPLICATES"
 -> Use set() to remove duplicates, then optionally convert back to list"
scores = [2, 4, 5, 3, 3, 1, 1, 2]
unique_scores = list(set(scores))
print(unique_scores)          # order may vary: e.g., [1, 2, 3, 4, 5]


     -> 5. CREATING LISTS"
 -> Using list() constructor"
numbers = list((1, 2, 3))     # from tuple
print(numbers)                # [1, 2, 3]

letters = list("abc")         # from string
print(letters)                # ['a', 'b', 'c']


     -> 6. SORTING LISTS"

 -> 6.1 .sort() - sorts the list in-place (original list is changed)"
original = [3, 1, 4, 2]
original.sort()
print(original)               # [1, 2, 3, 4]  (original modified)

 -> 6.2 sorted() - returns a new sorted list, original stays unchanged"
original = [3, 1, 4, 2]
new_sorted = sorted(original)
print(new_sorted)             # [1, 2, 3, 4]
print(original)               # [3, 1, 4, 2]  (unchanged)

 -> When to use sorted() instead of .sort():"
 ->   - When you need to preserve the original order"
 ->   - When sorting data types other than lists (e.g., tuples, strings)"
text = "cba"
sorted_text = sorted(text)    # works on any iterable
print(sorted_text)            # ['a', 'b', 'c']


     -> 7. NEGATIVE INDEXING"
 -> Access items from the end using negative indices"
b = ["apple", "banana", "cherry"]
print(b[-1])                  # cherry (last item)
print(b[-2])                  # banana (second last item)
print(b[-3])                  # apple (first item)


     -> 8. TAKING INPUT & SPLITTING"
 -> Typical problem: first line gives number of items, second line gives values"
 -> Example input:"
 -> 5"
 -> 2 3 6 6 5"

 -> Step-by-step reading"
n = int(input())              # reads first line: number of scores
scores_string = input()       # reads second line: "2 3 6 6 5"

 -> split() divides a string into a list of strings using whitespace as separator"
scores_list = scores_string.split()
print(scores_list)            # ['2', '3', '6', '6', '5']

 -> Convert to integers (if needed)"
scores_int = list(map(int, scores_list))
print(scores_int)             # [2, 3, 6, 6, 5]

 -> Or combine steps:"
scores = list(map(int, input().split()))


     -> 9. RUNNER-UP SCORE (CLASSIC EXAMPLE)"
 -> Given list of scores, find the second highest (runner-up)"
scores = [2, 3, 6, 6, 5]

 -> 1. Remove duplicates with set()"
unique_scores = set(scores)          # {2, 3, 5, 6}
 -> 2. Sort ascending with sorted()"
sorted_unique = sorted(unique_scores) # [2, 3, 5, 6]
 -> 3. Pick second last element (index -2)"
runner_up = sorted_unique[-2]
print(runner_up)                      # 5

 -> One-liner"
runner_up = sorted(set(scores))[-2]
print(runner_up)                      # 5

## Finding the runner-up score
- Use set(arr) to remove duplicate scores
- sorted(set(arr)) sorts unique values ascending
- sorted(set(arr))[-2] gives the second-highest (runner-up)
- Example: sorted(set([2, 3, 6, 6, 5]))[-2] -> 5