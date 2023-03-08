#https://api.nfse.io/validate/NaturalPeople/taxNumber/
import requests
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

lista = input('Digite o nome do arquivo que contém os cpfs: ') #

arquivo = open(lista, "r", encoding="latin-1").readlines()

for line in arquivo: #Verififa linha por linha do arquivo
    cpf = line.split()[0]

    #Variavel pra identificar url
    url = f'https://api.nfse.io/validate/NaturalPeople/taxNumber/{cpf}'

    #começa a requisição
    req = requests.get(url)
    #transforma o resultado da requisição em json
    req_json = req.json()

    #Try = tentar
    try:
        if req_json['valid']: #se conter 'valid' no retorno
            print(Back.GREEN + 'Cpf valido! ' + cpf)
        else: #se não encontrar
            print(Back.RED + 'Cpf invalido! '+ cpf)
    except: #caso dê algum erro que não foi passado nos parametros
        print('erro!')   

