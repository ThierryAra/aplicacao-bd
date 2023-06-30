from conexao import Conexao_bd
from sql import editar_banco
from tabels import Menu
from rich.console import Console


console = Console()
menu = Menu()
bd = Conexao_bd()
con = bd.conectar()
edit = editar_banco(con)

console.print("[bold]Bem vindo!!![/]")

console.print("Por favor selecione uma das opções abaixo para a operação desejada!")

opcoes = menu.get_options_table()
console.print(opcoes)

try:
    opcao_escolhida = int(input("Digite a opção desejada: "))
except ValueError:
    console.print("[bold] Por favor digite um número[red] inteiro [/]")

if opcao_escolhida == 1:
    console.print("Vamos agora inserir uma [bold]nova comunidade[/] ao banco\n Para isso, precisamos dos dados preenchidos")
    try:
        id: int = int(input('Id: '))

        nome: str = input('Nome: ').upper()
        if not nome.isalpha():
            raise ValueError
        
        estado: str = input('Estado: ').upper()
        if not estado.isalpha() or len(estado) > 30:
            raise ValueError
        
        qtd_hab: int = int(input('Número de habitantes: '))

        referencia: str = input('Referência de localização: ').upper()
        if not referencia.isalpha():
            raise ValueError
        
        coord: str = input('Coordenadas: ')
        if not coord.isalpha():
            raise ValueError
        
        etnia: str = input('Etnia: ').upper()
        if not etnia.isalpha():
            raise ValueError

        comunidade = (id, estado, nome, qtd_hab, referencia, coord, etnia)
        edit.INSERT_NEW_COMUNIDADE(comunidade)
    except ValueError:
        print("Por favor coloque inteiros/palavras quando necessário e de tamanhos corretos (ex.: Estado deve ter no máximo 30 caracteres)")

elif opcao_escolhida == 2:
    comunidades = menu.get_community_table()
    resultado = edit.SELECT_ALL_COMUNIDADES()
    for comunidade in resultado:
        comunidades.add_row(str(comunidade.id), str(comunidade.estado), str(comunidade.nome), str(comunidade.qtd_hab), str(comunidade.referencia), str(comunidade.coord), str(comunidade.etnia))
    
    console.print(comunidades)
elif opcao_escolhida == 3:
    comunidade_desejada = input("\nQual é a comunidade desejada? ").upper()
    resultado = edit.SELECT_ALL_COMUNIDADES(comunidade_desejada)
    if resultado: 
        comunidades = menu.get_community_table("Comunidade selecionada")
        for comunidade in resultado:
            comunidades.add_row(str(comunidade.id), str(comunidade.estado), str(comunidade.nome), str(comunidade.qtd_hab), str(comunidade.referencia), str(comunidade.coord), str(comunidade.etnia))
        
        console.print(comunidades)
    else:
        console.print("\nA comunidade desejada [bold]não[/] existe\n")

bd.desconectar(con)