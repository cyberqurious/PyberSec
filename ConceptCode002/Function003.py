# Function definition with "number of parameters" & Default Argument.
# Remember to pass the default value after the Non-default arguments
# Remember to return value from a function by return statement

# Default Argument Values.
def add_two_numbers(param_one, default_param=5):
  return param_one + default_param  # Returns the sum of the numbers, and is indented by 2 spaces.


# Simple function
def stringConcate(string_one, string_two):
  return string_one + string_two


# Calling function with Function_Name(number of arguments)
print(add_two_numbers(4, 8))  # 12

# with default value
print(add_two_numbers(4))  # 9

# Calling Simple function
print(stringConcate("Hello", str(77)))

# parameter packing
def mySum(*args):
  return sum(args)

# positional arguments
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

# arguments packing
def fun1(*arg): 
  a,b = arg # arguments un-packing
  print(b,a)

fun1(2,4) # calling function

# defining function within function
def sum1(n1, n2):
  def another_func(n1, n2):
    return n1 + n2
  return another_func(n1,n2)


print(sum1(20,30)) # or call with total(20,30) & sum1
    
# calling function within function call
def sum2(n1, n2):
  return n1 + n2

print(sum2(10,sum2(2,sum2(sum2(10,2),5))))


# Methods vs Functions

# function: can be called independenly
# list()
# print()
# input()

# user defined functions
def do_nothing():
  pass
do_nothing()

# Methods: associated with Objects & have to call with Objects
# list.count()
# dict.items()
# tuple.remove()


# doc string
def test(a):
  '''
  Info: this function does nothing
  '''
  return z

# help():  to give menu for a function.
help(test)
print(test.__doc__)


# Scope: what variable do a function have access to.

a = '3rd: Global' # Global: last priority

def parent():
  a = '2nd: Parent Local' # Parent function Local: 2nd priority
  def child():
    a = '1st: Local' # Local: 1st priority
    return a
    
  return child()

print(parent())
print(a)


# Global: Explicitly use the Global variable

glb = 5
print(id(glb))

def func():
  global glb # Explicitly using the Global variable
  print(id(glb)) # Same address as global var 'a'
  glb += 3
  return glb

print(func())

# Dependency injection: with out the Global Variable
var = 5

def func(var):
  var += 1
  return var

print(func(func(func(var)))) # Dependency injection


# nonlocal
def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner:",x)

  inner()
  print("outer:", x)

outer()

