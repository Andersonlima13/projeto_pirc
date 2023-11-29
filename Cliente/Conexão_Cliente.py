class ClienteArquivos:
    def __init__(self,endereco_servidor,porta):
        pass
    # TENTA SE CONECTAR COM A PORTA DEFINIDA DO SERVIDOR  
       
    def enviar_comando(self,comando):
        pass
    # ENVIA COMANDOS AO SERVIDOR
    
    def receber_lista_arquivos(self):
        pass
    # RECEBE A LISTA DE ARQUIVOS DISPONIVEL NO SERVIDOR
       
    def enviar_arquivo(self,conexao_cliente,nome_arquivo):
        pass
    # ENVIA UM ARQUIVO PARA O SERVIDOR
    
    def receber_arquivo(self,conexao_cliente,nome_arquivo):
        pass
    # RECEBE UM ARQUIVO DO SERVIDOR
    
    def encerrar_conexao(self,conexao_cliente):
        pass
    # FINALIZA A CONEXÃO COM O SERVIDOR
        