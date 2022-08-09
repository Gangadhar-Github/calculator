# # simple caclulator 


# def calculator(a ,b):
#     """Enter both number for caculation"""
#     input_value = input("Enter which operation do you want to caalculate \n for addition enter +. \n for subsrtact enter -.\n for devide enter /.\n for multiply Eneter * ")
#     if input_value == "+":
#         addition = a + b
#         return addition
#     elif input_value == "-":
#         substract = a - b
#         return substract
#     elif input_value == "/":
#         devide = a / b
#         return devide
#     else:
#         multiply = a * b
#         return multiply


# F_num = float(input("Enter your First number. "))
# S_num = float(input("Enter your second number. "))


# answer = calculator(F_num, S_num)
# print(f"Your Answer is {answer}")


# Calculator usigng Dictionaries and Function



def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def dev(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": dev,
}

do_continue = True
while do_continue:
    num1 = float(input("Whats your first number?: "))
    num2 = float(input("Whats your second number?: "))
    
    
    
    for symbol in operations:
        print(symbol)
        
   
    operations_symbol = input("pick an operation from the line above: ")
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    
    response  = input("Do you want to contiue checking the other results? if yes type 'y' or else 'n. ")
    if response == 'n':
        do_continue = False



    
    