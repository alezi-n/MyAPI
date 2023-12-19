from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
        Endpoint que exibe uma mensagem incrivel do mundo da programação!
    '''
    return {'Hello':'World'}

@app.get('/api')
def hello_world():
    '''
        Endpoint que salva meu texto!
    '''
    text = 'Nesse curso, eu aprendi como avançar na Orientação a Objetos em Python e também como consumir APIs. Aprendi a consultar endpoints, fazer pesquisas específicas e até mesmo visualizar a documentação da API. Foi muito legal entender a importância de adicionar docstrings aos endpoints para documentar sua funcionalidade. Agora estou mais preparado para trabalhar com APIs e desenvolver projetos mais complexos em Python.'

    return {'Text':text}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
        Endpoint que exibe o cardapio dos restaurantes!
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    reponse = requests.get(url)

    if reponse.status_code == 200:
        dados_json = reponse.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'descricao': item['description']
                })
        
        return{'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else:
        return {'Erro':f'{reponse.status_code} - {reponse.text}'}