from selenium import webdriver # para instalar a biblioteca abra o prompt ou o PowerShell e digite "pip install selenium"
from selenium.webdriver.common.keys import Keys # importa ferramentar para realizar e facilitar algumas funções como escrever e usar a tecla "ENTER" com o codigo
import random # seletor aleatório
import time # time é usado para o controle de tempo no codigo: time.sleep(~tempo em segundos~) por exemplo

class botinho:
    def __init__(self):
        
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Ailton\Desktop\VScod\Python\chromedriver.exe")# assista o video
    def home(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/") # abre o driver do chrome na pagina informada
        time.sleep(15) # espera 15 segundos para escanear o QRcode (time.sleep(15) pode ser substituido por input() e após escanear o QR deverá inserir algo no prompt como letra ou numero)

        while(1):
            if ( len((driver.find_elements_by_class_name("_38M1B"))) > 0 ): 
                # 'elements' retorna uma lista dos elementos encontrados, se for maior que 0 significa que o elemento buscado nao é vazio 

                campo_msg = driver.find_element_by_class_name("_38M1B") # _38M1B é o nome dado a classe que notifica uma nova mensagem recebida
                print("mensagem printada: ",campo_msg)
                campo_msg.click() # clicamos no campo da notificação
                time.sleep(3) # esperamos 3 segundos

                if ( len((driver.find_elements_by_xpath("//footer[@class='_3uxr9']"))) > 0 ): # _3uxr9 existe no html quando o campo para escrever mensagens existe (este if serve para evitar erros no codigo como tentar enviar mensagem onde "Somentes admins podem enviar mensagens")
                    print("possui chat")
                    envia_msg = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]") # procura o campo para escrever a mensagem
                    envia_msg.send_keys('Hi -bot') # escreve a mensagem
                    envia_msg.send_keys(Keys.ENTER) # usa a tecla Enter para enviar a mensagem escrita
                    time.sleep(5) 

                else:
                    print("naao possui chat")
                    time.sleep(2)
            else:# (linha 19) se nem uma mensagem for detectada espera 15 segundos para verificar novamente
                time.sleep(15)
    
bot = botinho()
bot.home()
