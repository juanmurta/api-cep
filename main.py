import requests
import pprint
import pandas as pd

# pesquisar cep
cep = '35054874'
cep = cep.replace('-', '').replace('.', '').replace(',', '')

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao.json())

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(uf, cidade, bairro)
else:
    print('Cep Invalido')


# buscar endereco e trazer cep
uf = 'RJ'
cidade = 'Rio de Janeiro'
endereco = 'Rio Branco'

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)

dic_requisicao = requisicao.json()

print(dic_requisicao)
pprint.pprint(dic_requisicao)

tabela = pd.DataFrame(dic_requisicao)
print(tabela)