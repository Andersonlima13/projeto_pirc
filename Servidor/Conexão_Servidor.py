class ServidorArquivos:
    def __init__(self,porta):
        pass
    # DEFINE A PORTA A QUAL O SERVIDOR DEVE RODAR
    
    def iniciar(self):
        pass
    # INICIA E PASSA A AGUARDAR CONEXÃO
    
    def aceitar_conexão(self):
        pass
    # ACEITA CONEXÃO DO CLIENTE
    
    def receber_comando(self,conexao_cliente):
        pass
    # RECEBE COMANDOS DO CLIENTE
    
    def enviar_lista_arquivos(self,conexao_cliente):
        pass
    # ENVIA A LISTA DE ARQUIVOS DISPONIVEIS 
    
    def enviar_arquivo(self,conexao_cliente,nome_arquivo):
        pass
    # ENVIAR OS CONTEÚDOS DO ARQUIVO SOLICITADO
    
    def receber_arquivo(self,conexao_cliente,nome_arquivo):
        pass
    # RECEBE UM ARQUIVO ENVIADO DO LADO DO CLIENTE
    
    def encerrar_conexao(self,conexao_cliente):
        pass
    # FINALIZA A CONEXÃO COM O CLIENTE
        