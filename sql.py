import oracledb
import models as md

bd = None
con = None

class Editar_banco():
    def __init__(self, conexao: oracledb.Connection) -> None:
        self.conn = conexao
    
    def INSERT_NEW_COMUNIDADE(self, comunidade:tuple) -> int:
        cursor = self.conn.cursor()
        
        try:
            cursor.execute('''INSERT INTO COMUNIDADE(ID_COMUNIDADE, ESTADO, NOME, NUM_HABITANTES, 
                                                    REFERENCIA_LOC, COORDENADAS_LOC, ETNIA) 
                                VALUES (:1, :2, :3, :4, :5, :6, :7)''', comunidade)
            self.conn.commit()
            cursor.close()
            
            print('\nInserção realizada com sucesso!!\n\n')
            
        except oracledb.IntegrityError as e:
            error_message = str(e.args[0]).lower()
            
            print()
            if 'fk_comunidade_estado' in error_message:
                print("Estado inválido!")
            elif 'pk_comunidade' in error_message:
                print("ID da comunidade já existe!")
            elif 'sk_comunidade' in error_message:
                print("Comunidade já cadastrada nesse estado!")
            elif 'ck_num_habitantes' in error_message:
                print("A quantidade de habitantes deve ser um número positivo maior que 0!")
            else:
                print("Erro de integridade:", error_message)
            print()
                
        except Exception as e:
            print("Erro ao executar a inserção")
            print(e.args)
    
    def SELECT_COMUNIDADES(self, filtro:str = None):
        cursor = self.conn.cursor()
        
        try:
            if filtro:
                filtro = '%'+filtro+'%'
                cursor.execute('SELECT * FROM COMUNIDADE WHERE NOME LIKE :filtro', filtro=filtro)
            else:
                cursor.execute('SELECT * FROM COMUNIDADE')

            linhas = cursor.fetchall()
            comunidades = [md.Comunidade(*linha) for linha in linhas]

            cursor.close()

            return comunidades
        
        except Exception as e:
            print('Erro ao executar a busca: ', e)
            return 0
        
    def DELETE_COMUNIDADE(self):  
        cursor = self.conn.cursor()
    
        try:
            id = input('Digite o id da comunidade que deseja remover do banco e dados:') 
            cursor.execute('DELETE FROM COMUNIDADE WHERE ID_COMUNIDADE = :id;', id=id)
            cursor.close()

        except Exception as e:
            print('Erro ao executar a remoção.', e)
            return -1


# Teste para inserções/selects
from conexao import Conexao_bd
if __name__ == '__main__':
    bd = Conexao_bd()
    con = bd.conectar()
    edit = Editar_banco(con)
    
    # comunidade = (202, 'comunidade z', 'roraima', )
    resultado = edit.SELECT_COMUNIDADES()
    
    bd.desconectar(con)