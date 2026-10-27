def calculate():

    num1 = float(input("digite seu numero: "))
    num2 = float(input("digite o segundo: "))
    op = input("digite  soma + - / * : ")

    if op == "+":
        print(f"resultado {num1 + num2}")   
    elif op == "-":
        print(f"resultado {num1 - num2}")    
    elif op == "/":
        print(f"resultado {num1 / num2}")   

        if num2 != 0:
            print(f"resultado {num1 / num2}")
        else:
            print("divisao por zero pae? ai nn")   

    elif op == "*":
        print(f"resultado {num1 * num2}")    

calculate()