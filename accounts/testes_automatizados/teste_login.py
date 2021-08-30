from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from time import sleep

# Código para testar tela de login adicionando usuarios ficticios 

class testeLogin:
    def __init__(self):
        # executa o silenium no background
        # self.firefox = Options()
        # self.firefox.add_argument("-headless")
        self.navegador = webdriver.Firefox(options=self.firefox)

    def acessaLogin(self, site):
        self.navegador.get(site)

    def logarUser(self, key, value):
        key = self.navegador.find_element_by_name(f"{key}")
        key.send_keys(value)

    def button_entrar(self):
        button = self.navegador.find_element_by_name("enter")
        button.click()

    def sair(self):
        self.navegador.quit()

if __name__ == "__main__":

    dados_login = [{'user': 'kroos@gmail.com', 'password': 'Kros1234'}, {'user': 'bezema@gmail.com', 'password': 'Bezema1234'}, {'user': 'ramos@gmail.com', 'password': 'Ramos1234'}, {'user': 'nacho@gmail.com', 'password': 'Nacho1234'}, {'user': 'varame@gmail.com', 'password': 'Varame1234'}, {'user': 'bale@gmail.com', 'password': 'Bale1234'}, {'user': 'casemiro@gmail.com', 'password': 'Casemiro1234'}, {'user': 'isco@gmail.com', 'password': 'Isco1234'}]
    
    for dados in dados_login:

        login = testeLogin()
        login.acessaLogin("http://127.0.0.1:8000/")

        for key, value in dados.items():
            login.logarUser(key, value)
        
        sleep(1)
        login.button_entrar()
        print(f'Usuário {dados["user"]} logado com sucesso.')
        sleep(4)
        login.sair()
    
    print('')
    print('')
    print("Usuarios logados com sucesso! Tela de login funcionando!")

