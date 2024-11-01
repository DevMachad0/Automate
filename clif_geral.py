from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import tkinter as tk
from tkinter import filedialog

def wait_for_downloads(directory):
    while True:
        if not any(filename.endswith('.part') for filename in os.listdir(directory)):  # O Edge usa .part para downloads
            break
        time.sleep(1)

def choose_download_directory():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    directory = filedialog.askdirectory()  # Abre o seletor de diretório
    return directory

def open_link2(login, senha, datainicio, datafim, time_interval, armazem_index):
    arquivo_data = choose_download_directory()  # Escolha o diretório
    arquivo_data = os.path.normpath(arquivo_data)  # Normaliza o caminho

    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("prefs", {
        "download.default_directory": arquivo_data,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "safebrowsing.disable_download_protection": True,
    })

    driver = webdriver.Edge(options=edge_options)
    try:
        print(time_interval)
        print(arquivo_data)
        # Acesse o link desejado
        driver.get("https://sesce.clif.rvimola.com.br/")

        # Espera alguns segundos para garantir que a página carregue
        time.sleep(5)

        # Clica no link desejado
        driver.find_element(By.XPATH, '//*[@id="conteudo_home"]/p/a').click()
        time.sleep(2)  # Espera 2 segundos

        # Clica no campo de login
        driver.find_element(By.XPATH, '//*[@id="UsuarioLogin"]').send_keys(login)

        # Clica no campo de senha
        driver.find_element(By.XPATH, '//*[@id="UsuarioSenha"]').send_keys(senha)

        # Clica no botão de login
        driver.find_element(By.XPATH, '//*[@id="UsuarioLoginForm"]/div[4]/input').click()
        # Espera a página carregar após o login
        time.sleep(10)

        # Acesse o novo link após o login
        driver.find_element(By.XPATH, '//*[@id="div-modulo"]/div[1]').click()

        time.sleep(10)

        while True:  # Loop infinito
            print("NOVO LOOP")
            driver.get("https://sesce.clif.rvimola.com.br/Relsaidasgerals/filtrosaidas")
            time.sleep(10)  # Espera a página carregar

            # Seleciona o armazém pelo índice
            select_armazem = Select(driver.find_element(By.XPATH, '//*[@id="filtro_unidade"]'))
            select_armazem.select_by_index(armazem_index)  # Seleciona pelo índice
            
            # Data início
            driver.find_element(By.XPATH, '//*[@id="filtro_dtcreate_ped_before"]').send_keys(datainicio)
            # Data fim
            driver.find_element(By.XPATH, '//*[@id="filtro_dtcreate_ped_after"]').send_keys(datafim)

            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="RelsaidasgeralTipofiltro"]/option[2]').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="FormRelatorio"]/div[5]/div/input').click()

            # Nome do arquivo que será baixado
            filename = os.path.join(arquivo_data, 'relatorio_saidas_geral_col.xlsx')  # Ajuste o nome e extensão conforme necessário

            # Remove o arquivo se ele já existir
            if os.path.exists(filename):
                os.remove(filename)

            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="XLSX"]').click()

            # Aguardar pelo intervalo definido antes da próxima iteração
            time.sleep(time_interval * 60)  # Converte minutos para segundos

    finally:
        driver.quit()  # Fecha o navegador
