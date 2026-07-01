states = {
    "Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
    "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
    "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]
}

def s_cities_count(cities_list):
    # Return the number of cities that begin with 'S'
    ct = 0
    for city in cities_list:
        if city[0] == 'S':
            ct = ct + 1
    return ct

print(sorted(states, key=lambda state: s_cities_count(states[state])))