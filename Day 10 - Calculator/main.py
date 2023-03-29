#Defining all the functions



def add(a, b):
  sum = a + b
  return sum

def subtract(a, b):
  diff = a - b
  return diff

def multiply(a, b):
  prod = a * b
  return prod

def divide(a, b):
  div = a / b
  return div

#creating operations dict

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide

}

#creating variables

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

operation_symbol = input("What operation do you want to use? Enter '+' for Addition, '-' for subtraction, '*', for Multiplication and '/' for Division")

operation = {}

# operation_choice = input("Press 1 to end program /n Press 2 to continue operating with the same numbers /n Press 3 to enter new numbers.") 