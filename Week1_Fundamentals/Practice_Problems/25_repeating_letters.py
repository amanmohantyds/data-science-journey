def double_char(txt):
    # Loop through each character 'c', double it, and join them back into one string
    return "".join(c * 2 for c in txt)

print(double_char("String"))