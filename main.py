from menu import MENU as m
from menu import resources as r

money = 0 # variable global para el dinero
on = True # controla el while principal

def report():
  """Chequea el estado de la máquina """
  global money
  for re in r:
    print(f"{re}: {r[re]}")
  print(f"Money: {money}$")

def checkResource(pro):
  """Chequea que haya el suficiente stock para el 
  producto deseado, recibe el producto y devuelve 
  un boleano"""
  check = False
  ing = pro['ingredients']
  for p in ing:
    if ing[p] <= r[p]:
      check = True
    else:
      return p
  return check

def makeCoffee(pro):
  """Resta los ingredientes del producto al
  stock de la máquina"""
  ing = pro['ingredients']
  for p in ing:
    r[p] -= ing[p]

def checkCoins(prod):
  """Verifica que se introduzca la cantidad necesaria de
  monedas para el producto seleccionado, recibe el producto
  y devuelve un boleano"""
  global money
  print("Inset coins..")
  quarters = float(input("How many quarters?: "))
  dimes = float(input("How many dimes?: "))
  nickel = float(input("How many nickel?:"))
  pennies = float(input("How many pennies?:"))
  total = quarters*0.25+dimes*0.10+nickel*0.05+pennies*0.01
  if total >= prod['cost']:
    print(f"Here is ${total - prod['cost']} dollars in change.")
    money += prod['cost']
    return True
  else:
    return False
  
while on:
  check = False
  state = input("“What would you like? (espresso/latte/cappuccino):")

  if state == "off":
    print("Shutting off the coffee machine")
    on = False
  elif state == "report":
    report()
  elif state == "espresso" or state == "latte" or state == "cappuccino" :
    check = checkResource(m[state])
    
    if check == True:
      if checkCoins(m[state]):
        print(f"Here is your {state}. Enjoy")
        makeCoffee(m[state])
      else:
        print(f"Sorry that's not enough money. Money refunded.")
    else:
      print(f"Sorry there is not enough {check}")
  
