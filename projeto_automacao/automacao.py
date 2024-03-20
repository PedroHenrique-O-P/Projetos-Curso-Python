import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=835, y=442)       
pyautogui.write("phenrique.tricolor17@gmail.com")

pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
  

import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.click(x=686, y=303)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna:
        pyautogui.write("")
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(900)
