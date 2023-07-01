from connection_bd import Conexao_bd
from sql import Editar_banco
from tabels import Menu
from rich.console import Console
from time import sleep
import sys, os, signal

bd  = Conexao_bd()
con = bd.conectar()

def apagar_linhas(qtd:int = 2):
    for _ in range(qtd):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K') 
        
def limpar_console():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')
               
# Finalização do programa (CTRL + C)
def handler(signal, frame):
    limpar_console()
        
    print("Programa finalizado. Desconectando...\n")
    
    bd.desconectar(con)
    sys.exit(0)
signal.signal(signal.SIGINT, handler)


def run():
    if not con:
        return -1
    
    console = Console()
    menu = Menu()
    edit = Editar_banco(con)
    
    console.print("\n[bold]Bem vindo!!![/]\n")

    opcao_escolhida = None
    while(opcao_escolhida != '0'):
        opcao_escolhida = None
        console.print("Por favor selecione uma das opções abaixo para a operação desejada!")

        opcoes = menu.get_options_table()
        console.print(opcoes)

        erros = 1
        while opcao_escolhida not in range(4):
            try:
                opcao_escolhida = int(input("Digite a opção desejada: "))
                if opcao_escolhida not in range(4):
                    raise ValueError
            except ValueError:
                apagar_linhas(erros)
                erros = 2
                console.print("[bold] Por favor digite um número[red] inteiro válido[/]")

        if opcao_escolhida == 1:
            inserir_comunidade(console, edit)
                
        elif opcao_escolhida in [2, 3]:
            comunidade_desejada = None
            
            if opcao_escolhida == 3:
                comunidade_desejada = input("\nQual é a comunidade desejada? ").upper()
                
            buscar_comunidade(console, menu, edit, comunidade_desejada)
        
    bd.desconectar(con)
    
def inserir_comunidade(console:Console, edit:Editar_banco):
    console.print('''Vamos agora inserir uma [bold]nova comunidade[/] ao banco\n 
            Para isso, precisamos dos dados preenchidos''')
            
    try:
        id: int = int(input('ID: '))
        if not isinstance(id, int):
            raise ValueError
        
        nome: str = input('Nome: ').upper()
        if not isinstance(nome, str):
            raise ValueError
        
        estado: str = input('Estado: ').upper()
        if not isinstance(estado, str) or len(estado) > 2:
            raise ValueError
        
        qtd_hab: int = int(input('Número de habitantes: '))
        if not isinstance(qtd_hab, int):
            raise ValueError
        
        referencia: str = input('Referência de localização: ').upper()
        if not isinstance(referencia, str):
            raise ValueError
        
        coord: str = input('Coordenadas: ')
        if coord[0] == ';':
            raise ValueError
        
        etnia: str = input('Etnia: ').upper()
        if not isinstance(etnia, str):
            raise ValueError

        comunidade = (id, estado, nome, qtd_hab, referencia, coord, etnia)
        edit.INSERT_NEW_COMUNIDADE(comunidade)
    except ValueError as e:
        print('''\nPor favor coloque inteiros/palavras quando necessário e
          de tamanhos corretos (ex.: Estado deve ter no máximo 30 caracteres)''')
        print('\t',e.args)
        sleep(5)
    except Exception as e:
        print('Não foi possível realizar a inserção. \nErro desconhecido: ', e)
        return -1
  
def buscar_comunidade(console:Console, menu:Menu, edit:Editar_banco, mensagem:str = None):
    comunidades = menu.get_community_table()
    resultado = edit.SELECT_COMUNIDADES(mensagem)
    
    if resultado:
        for comunidade in resultado:
            comunidades.add_row(str(comunidade.id), str(comunidade.estado), 
                                str(comunidade.nome), str(comunidade.qtd_hab), 
                                str(comunidade.referencia), str(comunidade.coord), 
                                str(comunidade.etnia))
        
        console.print(comunidades)
    elif resultado != -1:
        console.print("\n[bold]Não[/] existem comunidades ", 
                      "com esse padrão.\n\n" if mensagem else "cadastradas.\n\n", style='red')