#programa que leia um número inteiro qualquer e peça para usuario escolher a base de conversão
num = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL""")
opçao = int(input("Sua opção: "))
if opçao == 1:
    print(f"{num} convertido para binário é igual a {bin(num)[2:]}")
elif opçao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opçao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("opção inválida.")