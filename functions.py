
##argument funtion
def my_function(fname):
  print("My first name is "+fname);
  
my_function("Gunti") 

##function wirh multiple arguments
def my_funtion(fname,lname):
  print("My name is "+fname+" "+lname)
  
my_funtion("Gunti","Vineela")

##Arbitrary Arguments
def my_function1(*profession):
  print("I am a "+profession[2])
  
my_function1("Doctor", "Lawyer", "Software Engineer")


##keyword Arguments
def my_function2(k3,k2,k1):
  print("Second keyword is "+k2)
  
my_function2(k1="key1", k2="key2", k3="key3")

##Arbitrary Keyword Arguments
def my_function3(**k):
  print("Third keyword is "+k["k3"])
my_function3(k1="key1", k2="key2", k3="key3")  

##function returning value
def my_function4(x):
    return 5*x
for y in range(1,11):    
  print(my_function4(y))   
  
##recursive function
def sum_all(list):
  if len(list) == 1:
    return list[0]
  else:
    return list[0] + sum_all(list[1:])
    
print("sum "+str(sum_all([1,2,3,4,5])))    
    
