x = 5
if (type(x) is int): 
    print("True")
else:
    print("False")



x = 5.0
if (type(x) is not float): 
    print("True")
else:
    print("False")


x = 20
y = 20
if (x is y): 
    print("x & y  Same Indentity")
y = 30
if (x is not y):
    print("x & y have Different Indentity")
  
