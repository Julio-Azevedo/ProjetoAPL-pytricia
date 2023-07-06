import os
import datetime
from verifica import verifica_numerologia, definicao_numerologia

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função do menu iniciar
def menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Login",
        "2": "Cadastro",
        "0": "Sair"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Bem-vindo a PyTricia': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função de menu do usuário
def menu_usuario(busca):
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Horoscopo",
        "2": "Numerologia",
        "0": "Sair"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Bem-vindo a PyTricia ' + busca['username'].split()[0]:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que chama o menu do horoscopo
def horoscopo_menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Horoscopo do dia",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Horoscopo': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir a tela de mensagem do horoscopo
def horocopo_mensagem(astral, busca):
    conteudo = 100
    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'A mensagem do dia ' + data_formatada + ' para o Signo de ' + busca['sign']:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{astral:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")    
    

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir o menu de numerologia
def numerologia_menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Numerologia do Nome",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Numerologia': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    option = input("Digite a opção desejada: ")
    return option 


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir a numerologia do nome
def numerologia_nome_mensagem(definicao, nome):
    valor_nome = verifica_numerologia(nome)

    
    conteudo = 100

    print(f"+{'-' * conteudo}+")
    print(f"|{'Valor numerológico do nome ' + nome + ': ' + str(valor_nome):^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    definicao_str = ', '.join(definicao)
    print(f"|{definicao_str :^{conteudo}}|")
    print(f"+{'-' * conteudo}+")  
    
    
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´