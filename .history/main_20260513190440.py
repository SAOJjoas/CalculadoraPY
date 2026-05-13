#Variaveis
while True:
    print("BEM VINDO!\nCALCULADORA EM PYTHON:\n")
    change = int(input("[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n[0] sair\n> "))
    match change:
        case 1:
            
            print(num1, " + ", num2, " = ", num1 + num2)
        case 2:
            num1 = float(input("\nDigite 1 número:\n> "))
            num2 = float(input("\nDigite 1 número:\n> "))
            print(num1, " - ", num2," = ", num1 - num2)
        case 3:
            num1 = float(input("\nDigite 1 número:\n> "))
            num2 = float(input("\nDigite 1 número:\n> "))
            print(num1, " * ", num2," = ", num1 * num2)
        case 4:
            num1 = float(input("\nDigite 1 número:\n> "))
            num2 = float(input("\nDigite 1 número:\n> "))
            print(num1, " / ", num2," = ", num1 / num2)
        case 0: 
            print("VOLTE SEMPRE!\nCALCULADORA EM PYTHON.")
            break

def soma(a, b):
    num1 = float(input("\nDigite 1 número:\n> "))
    num2 = float(input("\nDigite 1 número:\n> "))