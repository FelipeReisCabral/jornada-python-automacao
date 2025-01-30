import pyautogui # type: ignore
from time import sleep
import pandas # type: ignore

# 1- Abrir o sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.press('win')
sleep(1)
pyautogui.click(x=767, y=1062)
sleep(2)
pyautogui.click(x=236, y=60)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# 2- Fazer o login
sleep(1)
pyautogui.click(x=695, y=373)
pyautogui.write('teste@automacao.com')
pyautogui.press('tab')
pyautogui.write('aasd%%454')
pyautogui.press('tab')
pyautogui.press('enter')

# 3- Importar a base de dados dos produtos
tabela = pandas.read_csv("produtos.csv")

# 4- Cadastrar os produtos até acabar os produtos
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    precoUni = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    observacao = tabela.loc[linha, "obs"]

    pyautogui.click(x=689, y=259)

    # código
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço unitário
    pyautogui.write(str(precoUni))
    pyautogui.press('tab')

    # custo
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Observação
    if str(observacao) == "nan":
        pyautogui.write("")
    else:
        pyautogui.write(str(observacao))
    pyautogui.press('tab')

    # salvar
    pyautogui.press('enter')
    pyautogui.press('home')
