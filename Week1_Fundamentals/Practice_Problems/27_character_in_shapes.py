def count_characters(lst):
    # Smash all rows into one string, then count all characters at once
    return len("".join(lst))

# Takes lines of input until you press Enter on an empty line
user_shape = list(iter(input, ""))

print(f"➞ {count_characters(user_shape)}")