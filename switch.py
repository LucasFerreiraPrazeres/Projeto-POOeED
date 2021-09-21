class Switch:
    def __init__(self, nome, ip, mac, portas , tabela_mac):
        self.nome=nome
        self.ip=ip
        self.mac=mac
        self.portas=portas
        self.tabela_mac=tabela_mac
    
    def __str__(self) -> str:
        return "SWITCH: {nome}\nIP:{ip} \nMAC: {mac} \nPORTAS: {portas} \nTabela MAC \n {tabela_mac}"
    
    def cadastrar_switch(self, switch):
        pass
    
    def encontrar_mac_destino(self, mac_destino):
        pass
    
    
    