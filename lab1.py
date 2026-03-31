a=15
b=12

print("type of a-", type(a))
print("type of b-", type(b))


print("addition-",a+b)
print("subtract",a-b)
print("multiply",a*b)
print("division",a/b)


c=int(a/b)
print("value of c",c)
print("type of c",type(c))

c=float(c)
print("new value of c",c)
print("type of c-",type(c))

message="The result of a divided by b is"
print(message +str(c))

print("if a is greater than b",a>b)
print("a is equal to b",a==b)
