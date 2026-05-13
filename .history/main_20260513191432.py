def soma(a, b):
    result = a + b
    return result

def subtacao(a, b):
    result = a - b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

while True:
    print("BEM VINDO!\nCALCULADORA EM PYTHON:\n")
    change = int(input("[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n[0] sair\n> "))
    num1 = float(input("\nDigite 1 número:\n> "))
    num2 = float(input("\nDigite 1 número:\n> "))
    match change:
        case 1:
            print(soma(num1, num2))
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 0: 
            print("VOLTE SEMPRE!\nCALCULADORA EM PYTHON.")
            break
