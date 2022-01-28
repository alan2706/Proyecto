def if_integer(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

string1 = '132'
string2 = '-132'
string3 = 'abc'

print(if_integer(string1))
print(if_integer(string2))
print(if_integer(string3))