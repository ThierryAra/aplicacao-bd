import oracledb
import models as md

class editar_banco():
    def __init__(self, conexao: oracledb.Connection) -> None:
        self.conn = conexao
    
    def INSERT_NEW_COMUNIDADE(self, comunidade):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO COMUNIDADE(ID_COMUNIDADE, ESTADO, NOME, NUM_HABITANTES, REFERENCIA_LOC, COORDENADAS_LOC, ETNIA) VALUES (:1, :2, :3, :4, :5, :6, :7)', comunidade)
            self.conn.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao executar a inserção")
            print(e.args)
    
    def SELECT_ALL_COMUNIDADES(self, filtro:str = None):
        cursor = self.conn.cursor()
        
        try:
            if filtro:
                cursor.execute('SELECT * FROM comunidade WHERE nome = :filtro', filtro=filtro)
            else:
                cursor.execute('SELECT * FROM comunidade')

            linhas = cursor.fetchall()
            comunidades = [md.Comunidade(*linha) for linha in linhas]

            cursor.close()

            return comunidades
        
        except Exception as e:
            print('Erro ao executar a busca.', e)
            return -1

from conexao import Conexao_bd
if __name__ == '__main__':
    bd = Conexao_bd()
    con = bd.conectar()
    edit = editar_banco(con)
    
    resultado = edit.SELECT_ALL_COMUNIDADES()
    
    bd.desconectar(con)