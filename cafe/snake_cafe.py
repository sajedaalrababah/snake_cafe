     

menu = {
    "Appetizers" : ["Wings" , "Cookies", "Spring Rolls"],
    "Entrees" : ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts" : ["Ice Cream", "Cake", "Pie"],
    "Drinks" : ["Coffee", "Tea", "Unicorn Tears"]
}
def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
''')
def munee():       
 for key, value in menu.items():
    print("")  
    print(key)
    print("----------")
    for item in value:
        print(item)


def user_insertion():
    print('''
    ***********************************
    What would you like to order?
    ***********************************
    ''')
  
def end_application():
    print("thanks for using snakes cafe application !") 

orders = []
def main():
    user_input=''
    while (user_input.lower() != "quit"):
      user_input=input(">") 
    
      if user_input in [item for sublist in menu.values() for item in sublist]:
        orders.append(user_input)
        count = orders.count(user_input)
        print(f"** {count} order of {user_input} have been added to your meal **")
      else:
        print("** Sorry, what you ordered is not on the menu. **")
    print("**************************************")
    print(f"Your order is: {orders}")
    print("**************************************")
      
   
 

  




if __name__=="__main__": 
    intro()  
    munee()
    user_insertion()
    main()
    end_application()

