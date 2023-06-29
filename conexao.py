from dotenv import load_dotenv
import oracledb
import os

class Conexao_bd():
    def __init__(self):
        load_dotenv()
        
        self.USER = os.environ.get('LOGIN')
        self.PASS = os.environ.get('PASS')
        self.PORT = os.environ.get('PORT')
        self.SERVICE_NAME  = os.environ.get('SERVICE_NAME')
        self.HOST  = os.environ.get('HOST')

    def conectar(self):
        dsn = f'{self.HOST}:{self.PORT}/{self.SERVICE_NAME}'
        
        connection = None
        try:
            connection = oracledb.connect(user=self.USER, password=self.PASS, dsn=dsn)
        except oracledb.DatabaseError as e:
            error_code = e.args[0].code
            error_msg  = e.args[0].message
            
            print('Conexão não iniciada:')
            print('\t Código:', error_code)
            print('\t Mensagem:', error_msg)
            print('Atualize os dados de conexão e tente novamente!')
              
        return connection
    
    def desconectar(self, connection):
        try:
            connection.close()
            print('Conexão encerrada com sucesso!')
        except:
            print('Conexão não encerrada!')
            
if __name__ == '__main__':
    banco = Conexao_bd()
    
    con = banco.conectar()
    print('\n')
    banco.desconectar(con)