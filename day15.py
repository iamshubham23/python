MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources={
    "water":600,
    "milk":500,
    "coffee":100
}
def is_resource_sufficient(order_ingredients):
    """return true when the order can be made,false if ingredientsare in sufficient"""
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item] >=resources[item]:
            print(f"sorry there is not enough {item}.")
            is_enough=False
            return True
        
def process_coins():
    """reutrn the total calculated from the coins insertes"""
    print("enter the coins")
    total=int(input("how many quaters"))*0.25 
    total+=int(input("how many dymes"))*0.1 
    total+=int(input("how many nickels"))*0.05
    total+=int(input("how many pennies"))*0.01
    return           

def is_transaction_successfull(money_recieved,drink_cost):
    """return true when the payment is accepted,or false if money is unsucessful"""
    if money_recieved >= drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"here is the change {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry thats not enough money ,money refunded")
        return False

def make_coffe(drink_name,order_ingredients):
    """deduct the required ingredients from the resources """    
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
        print(f" Here is your {drink_name}")


is_on=True
while is_on:
    choice=input("what would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice =="report":
        print("water:100ml")
        print("milk:50ml")
        print("coffe:76g")
        print("money:$2.5")
    else:
        drink=MENU[choice]
        print(drink)    
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffe(choice, drink["ingredients"])