def menu():
    print("-------COMMAND LINE CALCULATOR-------")
    print("Option 1: Arithmetic Operation (Example: 10 - 2)")
    print("Option 2: Clear")
    print("Option 3: Exit")

def parse_no(x):
    if x.lower() == "clear":
        return "clear", None, None
    p_x = x.split()
    if len(p_x) != 3:
        return None, None, None
    if p_x[1] not in ['+','-','*','/']:
        return None, None, None
    try:
        n1 = float(p_x[0])
        o = p_x[1]
        n2 = float(p_x[2])
    except ValueError:
        return None, None, None
    return o, n1, n2

def calculate(o, n1, n2):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    elif o == '/':
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2

def main():
    r = 0
    while True:
        menu()
        print("Current Result:", r)
        x = input("Enter the Arithmetic Expression: ")
        if x.lower() == "exit":
            print("Exitting Calculator")
            break
        o, n1, n2 = parse_no(x)
        if o == "clear":
            r = 0
            print("Calculator cleared")
        elif o is None:
            print("Invalid Input")
        else:
            result = calculate(o, n1, n2)
            if isinstance(result, str):
                print(result)
            else:
                r = result
                print("Result:", r)

main()
