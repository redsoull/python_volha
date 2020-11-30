# Task 1

string = "Hello, World"
mirror_string = string[::-1]
print(mirror_string)

# Task 2

string = "Hello, Lorld!"
string = "{0}{1}{2}".format(string[0:7], "W", string[8:])
print(string)

# Task 3
str = 'new string'
str.find('new') 
str.rfind('new') 
if str.find('new') > -1:
    print(str.find('new'))
elif str.rfind('ing') > -1:
    print(str.rfind('ing'))