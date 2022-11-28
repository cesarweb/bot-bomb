from time import sleep
from random import choice
from termcolor import colored
from colorama import init
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import JavascriptException ,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pyperclip,json,sys

abecedario ='abcdefghijlmnopqrstuv'
init(autoreset=True)
lettersArray=[]
for letter in abecedario:
        lettersArray.append(letter)
print('Iniciando el Browser...')
Options().add_argument('disable-infobars')
driver = webdriver.Chrome(options=Options())
driver.implicitly_wait(5)

print('Navegando al sitio de JKLM...')
driver.get('https://jklm.fun/')

loaded = False
while not loaded:
        print("Elije el juego! presiona enter cuando estes listo. Asegurate de estar en el juego!")
        AD=input('> ')
        loaded=True

def enviar(word):
        A = word
        A = list(A)
        lettersArray=[]
        for E in range(10):
                lettersArray.append([choice(U),d.BACKSPACE])
                F=choice([True,False])
        if F:
                I=choice([1,2,3])
                for E in range(I):A.insert(choice(range(len(A))),choice(lettersArray))
                A=[lettersArray for driver in A for lettersArray in driver]
        D=driver.find_element_by_css_selector('.selfTurn input')
        for J in A:K=G([0.02,0.04,0.03]);D.send_keys(J);H(K)
        H(0.2);D.send_keys(d.ENTER)




with open('espanol.txt','r', encoding="utf8")as Palabras:
        Lineas=Palabras.read().splitlines()
        print('Diccionario Cargado.')
        sleep (1)
        print("'CTRL+C' para salir.")
        sleep (1)
        palabras=[]
        print("Buscando el juego")

        try:
                WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,'game')))
                print('Encontrado! Buscando frame...')
                M=driver.find_elements(By.TAG_NAME, 'iframe')
                print(len(M))
                driver.switch_to.default_content
                print('Frame encontrado. cambiando...')
                driver.switch_to.frame(M[0])

        except Exception as ex:
                print('Error con el frame.' + repr(ex))

        print('Esperando por la silaba...')
        N=False
        while not N:
                WebDriverWait(driver,30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'syllable')));
                # silaba = input('enter al empezar> ')
                N=True
        while True:
                try:
                        lettersArray=[]
                        D=''
                        V=''
                        while True:
                                I=[]
                                if not lettersArray:
                                        for K in abecedario:
                                                lettersArray.append(K)
                                X=False
                                while not X:
                                        q=driver.find_element(By.CSS_SELECTOR,'selfTurn').get_attribute('hidden')
                                        if q!='true':
                                                X=True

                                D=driver.find_element(By.CSS_SELECTOR,'syllable').text
                                # AttributeError: 'WebDriver' object has no attribute 'find_element_by_css_selector'

                                D=D.lower()
                                # D = input('silaba > ')
                                O=False


                                for P in Lineas:
                                        if D in P.lower():
                                                I.append(P)
                                                O=True
                                if not O:
                                        print('No encuentro una palabra')
                                else:

                                        Q=[A for A in I for B in lettersArray if B in A.lower()]
                                        if Q:
                                                E=choice(Q)
                                        else:
                                                E=choice(I)
                                        print('Result: {}'.format(colored(E,'green')))
                                        # X = True # selector eliminar relacionado con linea 88 de codigo
                                        if X:
                                                input('Use la palabra > ' + E)
                                                # Enviar(E)
                                        sleep(0.3)
                                        Lineas.remove(E)

                                        for R in E:
                                                if R.lower()in lettersArray:
                                                        lettersArray.remove(R.lower())
                                                V=D
                except KeyboardInterrupt:
                        driver.quit()
                        sys.exit()

                except JavascriptException:
                        pass

                except ElementNotInteractableException:
                        pass

                except Exception as ex:
                        print(ex)
