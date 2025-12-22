nome= input("insira seu nome: ")
idade= int(input("insira sua idade: "))

if nome and idade!="":
    print(f'''Seu nome é {nome}
              Seu nome invertido é {nome[::-1]}
              Tem espaços no seu nome?: {"" in nome}
              Seu nome tem {len(nome)} letras
              A primeira letra do seu nome é: {nome[0]}
              Última letra do seu nome é {nome[-1:]}
                              ''')
else:
    print("você não digitou nada krl")    