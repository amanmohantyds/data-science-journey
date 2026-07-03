d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = list(d.keys())
best_key_so_far=ks[0] 
for k in ks:
    if d[k]>d[best_key_so_far]:
        best_key_so_far=k
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))