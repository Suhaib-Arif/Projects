from art import logo
print(logo)
operation={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div
}
def calculator():
    conti=True
    num1=float(input("Please enter a number :"))
    for keys in operation:
            print(keys)
    while conti:
    # print(function(2,3))
        operation_symbol=input("\nPlease pick an operation from the above symbols : ")
        num2=float(input("Please enter another number :"))
        function=operation[operation_symbol]
        answer=function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Do you want to continue? with the same value  ").lower() =='no':
            conti=False
            calculator()
        else:
            num1=answer
            clear()
calculator()
