from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from keyboard import press
import time 

musica = input("Link da musica: ")

PATH = "./chromedriver.exe"


chromeOptions = Options()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')

def script(mail, senha):
    driver = webdriver.Chrome(PATH, chrome_options=chromeOptions)

    driver.get("https://accounts.spotify.com/pt-BR/login/")
    time.sleep(2)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-username"]'))).send_keys(mail)
    time.sleep(2)

    print("Colocando email")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-password"]'))).send_keys(senha)
    time.sleep(1)

    print("Colocando Senha")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]/div[1]/p'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/button[2]'))).click()

    time.sleep(2)

    driver.get(musica)

    print("Entrando na musica")

    time.sleep(3)

    press('enter')

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div[1]/div[3]/div/div[3]/button'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div/div/button/div'))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div[1]/div[2]/div/div[1]/div[2]/button[2]'))).click()

    print("Tudo certo!")


script('testepythonapp@gmail.com', 'matheus30@')
script('testepythonapp21@gmail.com', 'matheus30@')
script('testepythonapp212@gmail.com', 'matheus30@')
script('testepythonapp2121@gmail.com', 'matheus30@')
script('testepythonapp21221@gmail.com', 'matheus30@')