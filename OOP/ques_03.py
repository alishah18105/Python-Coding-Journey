#Create a class with a class attribute a. Create an object from it and set a directly using object.a = 0. Does 
# this change the class attribute?

class test:
    a =10

obj = test()
print(obj.a)  # this will print 10 as it is accessing the class attribute
obj.a = 0 
print(obj.a)  # this will print 0 as we have set the value of a using object
print(test.a) # this will print 10 as the class attribute is not changed

#So the answer is No, setting a directly using object.a = 0 does not change the class attribute.