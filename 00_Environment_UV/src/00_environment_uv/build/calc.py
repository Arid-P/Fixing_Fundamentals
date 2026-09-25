def to_continue () -> None:
    print("Press any except n to continue (or type no to not continue).")
    repeat = input()
    
    if repeat in ["n", "no"] :
        print("Thanks for using us")
    
    return main()


def zero (num: int) -> int :
    while True :
        if num == 0 :
            print("Error: division by 0 is not possible")
            print("Enter a proper value for b.")
            num = input()
            num = is_valid_num(num)
        else:
            break
    
    return num

def is_valid_operation (op: str) -> int :
    operations = ["+", "a", "-", "b", "*", "m", "/", "d"]
    
    if op not in operations: 
        print("\nEnter a valid operation.")
        op = input("Enter operation:   ")
        op = is_valid_operation(op)
    
    return op


def is_valid_num (num: str) -> int :
    while True :
        try :
            num = int(num)
            break
        except ValueError :
            print("\nEnter a valid integral value!")
            num = input()
    
    return num


def main () -> None :
    #raise ValueError('main not implemented')
    n1 = input("Enter the first number (n1):   ")
    n1 = is_valid_num(n1)
    n2 = input("\nEnter the first number (n2):   ")
    n2 = is_valid_num(n2)
    
    print("\nChoice the operation by type its symbol at the start.")
    print("+ or n1:  performs addition of the two numbers")
    print("- or s:  performs subtraction of the two numbers")
    print("* or m:  performs multiplication of the two numbers")
    print("/ or d:  performs division of the two numbers")
    
    op = input("\nEnter the operation:   ")
    op = is_valid_operation(op)
    
    
    if(op == "+" or op == "a") :
        result = n1 + n2
    
    elif(op == "-" or op == "s") :
        result = n1 - n2
    
    elif(op == "*" or op == "m") :
        result = n1 * n2
    
    elif(op == "/" or op == "d") :
        n2 = zero(n2)
        result = n1 / n2
    
    elif(op == "%" or op == "r") :
        n2 = zero(n2)
        result = n1 % n2
    
    else :
        print("\nInvalid operation\n\n")
        return main()
    
    print(f"\nResult = {result}\n\n")
    
    return to_continue()

if __name__ == "__main__" :
    main()