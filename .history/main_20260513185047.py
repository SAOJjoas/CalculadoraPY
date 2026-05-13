#Variaveis

num1 = float(input("\nDigite 1 número:\n> "))
change = int(input("[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n> "))
num2 = float(input("\nDigite 1 número:\n> "))
match change:
    case 1:
        print(num1, " + ", num2," = ", num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 / num2)
        
