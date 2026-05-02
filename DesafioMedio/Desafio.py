import random
#função pra ver se é primo
def VerifPrimo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

#função que gera uma lista
def gerar_lista(começo, fim):
    if fim - começo < 10:
        raise ValueError("O intervalo deve ter pelo menos 10 números.")
    return [random.randint(começo, fim) for _ in range(10)]

#função que multiplica os primo
def multiplicar(lista):
    produto = 1
    encontrou_primo = False
    for num in lista:
        if VerifPrimo(num):
            produto *= num
            encontrou_primo = True
    return produto if encontrou_primo else 0
#jogar ums valor
começo = 1
fim = 100
lista = gerar_lista(começo,fim)
print("lista:",lista)
resultado= multiplicar(lista)
print("resultado:",resultado)
