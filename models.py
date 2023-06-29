class Comunidade:
    def __init__(self, id, estado, nome, qtd_hab, referencia,coord, etnia):
        self.id = id
        self.estado = estado
        self.nome = nome
        self.qtd_hab = qtd_hab
        self.referencia = referencia
        self.coord = coord
        self.etnia = etnia
    
    def __str__(self) -> str:
        comunidade = f'''Comunidade ({self.id}):
            \tNome  : {self.nome}
            \tEstado: {self.estado}
            \tEtnia : {self.etnia}
            \tCoordenadas: {self.coord}
            \tReferência : {self.referencia}
            \tNúmero de habitantes: {self.qtd_hab}
            '''
        
        comunidade = '\n\t'.join(line.strip() for line in comunidade.split('\t'))
        return comunidade