from rich.console import Console
from rich.table import Table

class Menu(object):
    def __init__(self) -> None:
        pass
    
    def get_options_table(self):
        opcoes = Table(title="Opções")
        opcoes.add_column("Opção", style='cyan')
        opcoes.add_column("Comando", style= 'magenta')
        opcoes.add_row("1", "Inserir um novo registro no banco")
        opcoes.add_row("2", "Selecionar todas as comunidades do banco")
        opcoes.add_row("3", "Selecionar uma comunidade específica no banco")
        return opcoes

    def get_community_table(self, title_text = 'Todas as Comunidades Registradas'):
        comunidades = Table(title=title_text)
        comunidades.add_column('ID')
        comunidades.add_column('Estado')
        comunidades.add_column('Nome')
        comunidades.add_column("Qtd. Habitantes")
        comunidades.add_column("Referência")
        comunidades.add_column("Coordenadas")
        comunidades.add_column("Etnias")
        return comunidades