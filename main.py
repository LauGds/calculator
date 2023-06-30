# Calculator
from replit import clear
from art import logo
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  continue_calc = True
  while continue_calc:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_calc == "y":
      num1 = answer
    elif continue_calc == "n":
      continue_calc = False
      clear()
      calculator()
    else:
      print("You type a different character. Try again!")

calculator()