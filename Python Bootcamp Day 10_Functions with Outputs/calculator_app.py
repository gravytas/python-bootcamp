#calculator application

from replit import clear
import art


def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2 

def mult(n1, n2):
  return n1 * n2 

def div(n1, n2):
  return n1 / n2

operators = {
  "+" : add,
  "-" : sub,
  "*" : mult,
  "/" : div
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?: "))
  calculate = True

  while calculate:
    op_symbol = input("Pick an operation: '+', '-', '*', '/':  ")
    num2 = float(input("What's the next number?: "))
    answer = operators[op_symbol](num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    cont = input(f"Type 'y' to continue calculating with {answer} and 'n' to begin a new calculation: ")
    
    if cont == "y":
      num1 = answer
    else:
      calculate = False
      clear()
      calculator()


calculator()
    
  
