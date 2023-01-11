import math as m
PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    '''
    (int)->float
    takes diameter of a pizza as an integer and returns its area as float.
    
    exemples:
    >>> get_pizza_area(10)
    78.53981633974483
    
    >>> get_pizza_area(18)
    254.46900494077
    
    >>> get_pizza_area(20)
    314.15926535898
    '''
    area=float(((diameter/2)**2)*m.pi)
    return area




def get_fair_quantity(diameter1,diameter2):
    '''
    (float,float)->int
    
    Takes two positive floats, for the diameter of two pizzas. Returns as an integer the minimum number of small
    pizzas that must be ordered to get at least the same amount of pizza (by area) as one large pizza. And if FAIR
    is False return 1.5 the amount of pizzas.
    
    Exemples:
        FAIR being True:
    >>> get_fair_quantity(14.0, 8.0)
    4
    
    >>> get_fair_quantity(45, 3.8)
    141
    
    >>> get_fair_quantity(3.29, 2)
    3
    
    >>> get_fair_quantity(20, 20)
    1
    
    
        FAIR being False:
    >>> get_fair_quantity(14.0, 8.0)
    4
    
    >>> get_fair_quantity(45, 3.8)
    210
    
    >>> get_fair_quantity(20, 20)
    1
    '''
    if diameter1<diameter2:
        min_d=diameter1
        max_d=diameter2
    elif diameter1>=diameter2:
        min_d=diameter2
        max_d=diameter1
    min_area=get_pizza_area(min_d)
    max_area=get_pizza_area(max_d)
    true_amount=(max_area/min_area)
    if  true_amount<=round( true_amount):
        number_of_pizza=round(true_amount)
    else:
        number_of_pizza=round(true_amount)+1
    if not FAIR:
        FAIR_TRUE_AMOUNT=round(1.5*true_amount)
        if FAIR_TRUE_AMOUNT<=1.5*true_amount:
            number_of_pizza=FAIR_TRUE_AMOUNT
        else:
            number_of_pizza=FAIR_TRUE_AMOUNT-1
    return number_of_pizza

def get_pizza_diameter(area):
    """
    (float)->float
    
    takes area of a pizza as a float and returns its diameter as float.
    
    Exemples:
    >>> get_pizza_diameter(10.0)
    3.5682482323055
    
    >>> get_pizza_diameter(1.0)
    1.1283791670955126
    
    >>> get_pizza_diameter(7.58)
    3.1066309322306913

        """
    diameter=2*m.sqrt(area/m.pi)
    return diameter


def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    '''
    (float,float,float,float,int)->float
    
    Takes four positive floats (diameter of large and small pizza, and cost of large and small pizza) and one
    positive integer (number of small pizzas) as input. Exactly one of the five inputs will be the integer -1.
    The function must use the other four values to calculate and return the missing input value as a float,
    rounded to two decimal places.
    
    Exemples:
    >>> pizza_formula(12.0, 6.0, 10.0, -1, 2)
    5.0
    
    >>> pizza_formula(19.0, -1, 3.0, 2.5, 10)
    6.0
    
    >>> pizza_formula(15.89, 5.8, 17.3, 7.8,-1)
    3.38
    '''
    if(d_large<0 or c_large<0):
        a_small=get_pizza_area(d_small)
        The_Amount=(n_small*a_small)/c_small
        if d_large<0:
            a_large=(The_Amount*c_large)
            d_large=get_pizza_diameter(a_large)
            return round(d_large,2)
        a_large=(d_large/2)**2*m.pi
        c_large=a_large/The_Amount
        return round(c_large,2)
    a_large=get_pizza_area(d_large)
    The_Amount=(a_large/c_large)
    if d_small<0:
        a_small=(The_Amount*c_small)/n_small
        d_small=get_pizza_diameter(a_small)
        return round(d_small,2)
    elif c_small<0:
        a_small=get_pizza_area(d_small)
        c_small=(n_small*a_small)/The_Amount
        return round(c_small,2)
    a_small=get_pizza_area(d_small)
    n_small=The_Amount*c_small/a_small
    return round(n_small,2)



def get_pizza_cake_cost(base_diameter, height_per_level):
    """(int,float)->float

    Takes one positive integer (diameter of base)and one positive float (height in centimetres per level) as inputs.
    Returns the cost of the pizza cake as a float rounded to two decimal places.
    
    Exemples:
        FAIR being True
    >>> get_pizza_cake_cost(2, 1.0)
    15.71
    
    >>> get_pizza_cake_cost(5, 2.5)
    431.97
    
    >>> get_pizza_cake_cost(20, 1)
    9016.37
    
    
        FAIR being False
    >>> get_pizza_cake_cost(5, 2.5)
    647.95
    """
    diameter_of_the_pizza=base_diameter
    total_volume=0
    for loop in  range(base_diameter):
        area_of_the_pizza=get_pizza_area(diameter_of_the_pizza)
        total_volume=total_volume+area_of_the_pizza*height_per_level
        diameter_of_the_pizza=diameter_of_the_pizza-1
    total_cost=total_volume*PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
    if not FAIR:
        return round(1.5*total_cost,2)
    return round(total_cost,2)
    

        
def get_pizza_poutine_cost(diameter, height):
    """(int,float)->float

    Takes one positive integer (diameter of the poutine cylindrical cup) and one positive float (height in centimetres)
    as inputs. Returns the cost of the pizza poutine as a float rounded to two decimal places.
    
    Exemples:
        FAIR veing True
    >>> get_pizza_poutine_cost(2, 1.0)
    9.42
    
    >>> get_pizza_poutine_cost(11,3.6 )
    1,026.36
    
        FAIR being False
    >>> get_pizza_poutine_cost(1095,3.5654 )
    15109110.37
    """
    area_base=get_pizza_area(diameter)
    volume=area_base*height
    cost_pizza_poutine=PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED*volume
    if not FAIR:
        return round(1.5*cost_pizza_poutine,2)
    return(round(cost_pizza_poutine,2))
    
def display_welcome_menu():
    """
    ()->None
    
    Displays to the screen a menu with a welcome message and the three options available to the user.
    
    Exemple:
    >>> display_welcome_menu()
    Welcome To The Best Pizza Place. And if you don't want pizzas we have wheels.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    """
    print("Welcome To The Best Pizza Place. And if you don't want pizzas we have hot wheels!")
    print("Please choose an option:")
    print("A. Special Orders")
    print("B. Formula Mode")
    print("C. Quantity Mode")


def special_orders():
    """
    ()->None
    
    Takes no inputs and returns nothing. Asks the user to choose between cake
    and poutine, asks them to enter a value for the diameter and for the height, and if they want the
    special ingredient, then prints out the total cost of the order.
    
    Exemples:
        FAIR being true
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole? yes
    The cost is $35.7
    
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 5
    Enter height: 2.5
    Do you want the guacamole? yes
    The cost is $451.96
    
    
        FAIR being false
    >>> special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 5
    Enter height: 2.5
    Do you want the guacamole? no
    The cost is $647.95
    
    >>> special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 1095
    Enter height: 3.5654
    Do you want the guacamole? yes
    The cost is $15109130.36

    """
    cake_poutine=input("Would you like the cake or poutine? " )
    diameter=int(input("Enter diameter: " ))
    height=float(input("Enter height: "))
    if cake_poutine=="poutine":
        cost=get_pizza_poutine_cost(diameter, height)
    elif cake_poutine=="cake":
        cost=get_pizza_cake_cost(diameter, height)
    ingredient=input("Do you want the "+SPECIAL_INGREDIENT+"? ")
    if ingredient=="yes" or ingredient=="y":
        cost=cost+SPECIAL_INGREDIENT_COST
    print("The cost is $"+str(round(cost,2)))
def quantity_mode():
    """
    ()->None
    
    Takes no inputs and returns nothing. Asks the user to enter in the diameters of two pizzas, and then prints out the
    minimum number of smaller pizzas they would need to buy to get at least the same amount of pizza (by area)
    as one large pizza.
    
    Exemples:
        FAIR being True
    >>> quantity_mode()
    Enter diameter 1: 8
    Enter diameter 2: 14
    You should buy 4 pizzas.
    
    >>> quantity_mode()
    Enter diameter 1: 45
    Enter diameter 2: 3.8
    You should buy 141 pizzas.
    
    
        FAIR being False
    >>> quantity_mode()
    Enter diameter 1: 20
    Enter diameter 2: 20
    You should buy 1 pizzas.
    
    >>> quantity_mode()
    Enter diameter 1: 45
    Enter diameter 2: 3.8
    You should buy 210 pizzas.
    """
    diameter1=float(input("Enter diameter 1: "))
    diameter2=float(input("Enter diameter 2: "))
    print("You should buy",get_fair_quantity(diameter1,diameter2),"pizzas.")



def formula_mode():
    """
    ()-> None
    
    Takes no inputs and returns nothing. Asks the user to enter in the diameter of a large and small pizza, cost of
    a large and small pizza, and number of small pizzas (in that order), with one of the values being -1, and prints
    out the actual value of the input that was given as -1.
    
    Exemples:
    >>> formula_mode()
    Enter large diameter: 12
    Enter small diameter: 6
    Enter large price: 10
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    
    >>> formula_mode()
    Enter large diameter: 15.89
    Enter small diameter: 5.8
    Enter large price: 17.3
    Enter small price: 7.8
    Enter small number: -1
    The missing value is: 3.38
    
    >>> formula_mode()
    Enter large diameter: 19.0
    Enter small diameter: -1
    Enter large price: 3.0
    Enter small price: 2.5
    Enter small number: 10
    The missing value is: 5.48
    """
    d_large=float(input("Enter large diameter: "))
    d_small=float(input("Enter small diameter: "))
    c_large=float(input("Enter large price: "))
    c_small=float(input("Enter small price: "))
    n_small=int(input("Enter small number: "))
    print("The missing value is:",pizza_formula(d_large, d_small, c_large, c_small, n_small))




def run_pizza_calculator():
    """
    ()-> None
    
    Takes no inputs and returns nothing. Displays a welcome message to the user and list of program options, asks
    the user to input an option, and then calls the appropriate function. If the user inputs an invalid option,
    prints out "Invalid mode.".
    
    Exemples:
        FAIR being True
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. And if you don't want pizzas we have hot wheels!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1
    Do you want the guacamole? y
    The cost is $35.7
    
    
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. And if you don't want pizzas we have hot wheels!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter: 12
    Enter small diameter: 6
    Enter large price: 10
    Enter small price: -1
    Enter small number: 2
    The missing value is: 5.0
    
    
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. And if you don't want pizzas we have hot wheels!
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: C
    Enter diameter 1: 45
    Enter diameter 2: 3.8
    You should buy 141 pizzas.
    """
    display_welcome_menu()
    your_choice=str(input("Your choice: "))
    if(your_choice=="A" ):
        special_orders()
    elif(your_choice=="B" ):
        formula_mode()
    elif(your_choice=="C" ):
        quantity_mode()
    else:
        print("Invalid mode.")
    
    
    
    
    
    
    
    
    
    
    
