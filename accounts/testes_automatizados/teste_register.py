from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

[{'user': 'kroos@gmail.com', 'password': 'Kros1234'}, {'user': 'bezema@gmail.com', 'password': 'Bezema1234'}, {'user': 'ramos@gmail.com', 'password': 'Ramos1234'}, {'user': 'nacho@gmail.com', 'password': 'Nacho1234'}, {'user': 'varame@gmail.com', 'password': 'Varame1234'}, {'user': 'bale@gmail.com', 'password': 'Bale1234'}, {'user': 'casemiro@gmail.com', 'password': 'Casemiro1234'}, {'user': 'isco@gmail.com', 'password': 'Isco1234'}]

# Código para testar tela de cadastro adicionando usuarios ficticios 
class testeRegister:
    def __init__(self):
        self.firefox = Options()
        self.firefox.add_argument("-headless")
        self.navegador = webdriver.Firefox(options=self.firefox)
    def acessaRegister(self, site):
        self.navegador.get(site)

    def registerUser(self, key, value):
        key = self.navegador.find_element_by_name(f"{key}")
        key.send_keys(value)

    def button_cadastrar(self):
        button = self.navegador.find_element_by_xpath("//button[@name='button']")
        button.click()

    def sair(self):
        self.navegador.quit()


if __name__ == '__main__':

    dados_para_registrar = [{'nome': 'Kroos', 'Snome': 'Real', 'email': 'kroos@gmail.com', 'sexo': 'Masculino', 'password': 'Kros1234', 'Rsenha': 'Kros1234'}, {'nome': 'Bezema', 'Snome': 'Real', 'email': 'bezema@gmail.com', 'sexo': 'Masculino', 'password': 'Bezema1234', 'Rsenha': 'Bezema1234'}, {'nome': 'Ramos', 'Snome': 'Real', 'email': 'ramos@gmail.com', 'sexo': 'Masculino', 'password': 'Ramos1234', 'Rsenha': 'Ramos1234'}, {'nome': 'Nacho', 'Snome': 'Real', 'email': 'nacho@gmail.com', 'sexo': 'Masculino', 'password': 'Nacho1234', 'Rsenha': 'Nacho1234'}, {'nome': 'Varame', 'Snome': 'Real', 'email': 'varame@gmail.com', 'sexo': 'Masculino', 'password': 'Varame1234', 'Rsenha': 'Varame1234'}, {'nome': 'Bale', 'Snome': 'Real', 'email': 'bale@gmail.com', 'sexo': 'Masculino', 'password': 'Bale1234', 'Rsenha': 'Bale1234'}, {'nome': 'Casemiro', 'Snome': 'Real', 'email': 'casemiro@gmail.com', 'sexo': 'Masculino', 'password': 'Casemiro1234', 'Rsenha': 'Casemiro1234'}, {'nome': 'Isco', 'Snome': 'Real', 'email': 'isco@gmail.com', 'sexo': 'Masculino', 'password': 'Isco1234', 'Rsenha': 'Isco1234'}]

    lista_login = list()
    dicionario_login = dict()

    for dados in dados_para_registrar:
        dicionario_login['user'] = dados["email"]
        dicionario_login['password'] = dados["password"]
        lista_login.append(dicionario_login.copy())
        dicionario_login.clear()

        register = testeRegister()
        register.acessaRegister(str(input('Link: ')))

        for key, value in dados.items():
            register.registerUser(key, value)
        
        sleep(2)
        register.button_cadastrar()
        print(f'Usuário {dados["nome"]} {dados["Snome"]} adicionado com sucesso')
        sleep(3)
        register.sair()
    
    print('')
    print('')
    print("Usuarios cadastrados com sucesso! Tela de registro funcionando!")
    print('')
    print("=>" * 10, "Lista para login gerada", "=>" * 10)
    print(lista_login)

