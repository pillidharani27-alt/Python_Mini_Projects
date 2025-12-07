Menu={
    "latte":{"ingredients":{"water":200,"milk":150,"coffee":24,},"cost":150},
    "espresso":{"ingredients":{"water":200,"coffee":24,},"cost":100},
    "cappuccino":{"ingredients":{"water":200,"milk":150,"coffee":24,},"cost":250,}
}
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":150,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("please insert coins.")
    total=0
    coins_five=int(input("how many 5rs coins?: "))
    coins_ten = int(input("how many 10rs coins?: "))
    coins_twenty = int(input("how many 20rs coins?: "))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total
def is_payment_successful(money_received,coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs{change} in changes.")
        return True
    else:
        print("Sorry that's not enough money.... money refunded.")
        return False
def make_coffee(coffee_name,cofee_ingredients):
    for item in cofee_ingredients:
        resources[item]-=cofee_ingredients[item]
    print(f"Here is your {coffee_name} coffee....Enjoy !!!")
is_on=True
while is_on:
    choice=input("What would you like to have?(latte/espresso/Cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}gm")
        print(f"money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type["cost"]):
                make_coffee(choice,coffee_type["ingredients"])
