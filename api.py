from flask import Flask, jsonify, request
from uteis.regras import verificarCondicao

altura: float = 0
valorFrete: float = 0
peso: float = 0
nomeEmpresa: str = 0 
largura: float = 0     

            
produtos = [{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}]


app = Flask (__name__)

#Deixei aqui caso necessário utilizar o método GET
@app.route('/produtos', methods=['GET'])
def obterProdutos():
    return jsonify(produtos)

#Deixei aqui caso necessário utilizar o método GET porém filtrando pelo Id do produto
@app.route('/produtos/<int:id>', methods=['GET'])
def obterProdutoNome(id):
 for produto in produtos:
      if produto.get('id') == id:
        return jsonify(produto)


@app.route('/produtos', methods=['POST'])

def criarNovoProduto():
    novoProduto = request.get_json()
    produtos.append(novoProduto)
    alt = novoProduto['dimensao']['altura']
    lar = novoProduto['dimensao']['largura']
    pes = novoProduto['peso']
    
    return verificarCondicao(alt,lar,pes)     

app.run(port=5000,host='localhost',debug=True)