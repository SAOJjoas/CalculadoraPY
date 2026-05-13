def soma(a, b):
    result = a + b
    return result

def subtacao(a, b):
    result = a - b
    return result

def multiplicacao(a, b):
    result = a * b
    return result

def divisao(a, b):
    result = a / b
    return result

def elevar(a, b):
    result = a ** b
    return result

def sqr(a, b):
    result = a ** (1 / b)
    return result

while True:
    print("BEM VINDO!\nCALCULADORA EM PYTHON:\n")
    change = int(input("[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n[5] elevar\n[6] raiz\n[0] sair\n> "))
    
    if change == 0:
        print("VOLTE SEMPRE!\nCALCULADORA EM PYTHON.")
        break

    num1 = float(input("\nDigite 1 número:\n> "))
    num2 = float(input("\nDigite 1 número:\n> "))
    #MOSTRAR NO TERMINAL
    match change:
        case 1:
            print(soma(num1, num2))
        case 2:
            print(subtacao(num1, num2))
        case 3:
            print(multiplicacao(num1, num2))
        case 4:
            print(divisao(num1, num2))
        case 5:
            print(elevar(num1, num2))
        case 6:
            print(sqr(num1,num2))
