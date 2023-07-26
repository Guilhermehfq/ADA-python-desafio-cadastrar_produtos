produtos = {}

def cadastre_produto(produtos):
  """Essa função cadastra um novo produto com os campos:
    - nome do produto (obrigatório)
    - quantidade (opcional)
    - descrição (opcional)
    - outros campos
    Ps: o nome do produto é único, logo podemos pensar como uma chave única
  """
  nome = input('Qual o nome do produto para cadastrar? ')
  quantidade = input('Qual a quantidade para cadastrar? ')
  if quantidade == '':
    quantidade = 0
  else:
    quantidade = int(quantidade)
  descricao = input('Qual a descrição do produto para cadastrar? ')

  produto = {
    "nome": nome,
    "quantidade": quantidade,
    "descrição": descricao
  }
  produtos = {
    nome: produto
  }
  return produtos

def delete_produto(produtos):
  """ Essa função deleta um produto da base pelo `nome do produto`
  """
  deletar = input('Qual o nome do produto que voce deseja remover? ')
  if produtos.get(deletar) == deletar:
    deletado = produtos.pop(deletar)
    print(f'O item de nome {deletado} foi apagado do sistema')
    return produtos
  else:
    print(f'Não foi encontrado o item de nome {deletar}')
  

def adicione_produto_estoque(produtos):
  """ Essa função adiciona ao estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """
  produto_modificar = input('Qual o nome do produto que você deseja modificar? ')
  if produtos.get(produto_modificar) == produto_modificar:
    quantidade = int(input('Quantos itens voce deseja adicionar ao estoque? '))
    if quantidade >= 0:
      quantidade_antes = produto_modificar.get('quantidade')
      quantidade_total = quantidade_antes + quantidade
      produto_modificar.update({"quantidade": quantidade_total})
      print(f'Foi adicionado {quantidade} itens ao item {produtos.get(produto_modificar)}')
      return produtos
    else:
      print('Não é aceito quantidades negativas')

def remova_produto_estoque(produtos):
  """ Essa função remove do estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """
  produto_modificar = input('Qual o nome do produto que você deseja modificar? ')
  if produtos.get(produto_modificar) == produto_modificar:
    quantidade = int(input('Quantos itens voce deseja remover do estoque? '))
    if quantidade >= 0:
      quantidade_antes = produto_modificar.get('quantidade')
      quantidade_total = quantidade_antes - quantidade
      if quantidade_total >= 0:
        produto_modificar.update({"quantidade": quantidade_total})
      else:
        print('Não é possivel ter estoque negativo, favor verificar a quantidade de itens retirados')
    else:
      print('Não é aceito quantidades negativas')    

def consulte_produtos(produtos):
  """ Essa função mostra os produtos disponíveis no sistema (somente nome)
  """
  print('O produtos disponiveis são:')
  for keys, valores in produtos.items():
    print(keys)

def consulte_quantidade(produtos):
  """ Essa função mostra os produtos e a quantidade disponíveis no sistema
  """
  print('O produtos e quantidades disponiveis são:')
  for chave, valor in produtos.items():
    print(f'{chave} -> {valor["quantidade"]} itens')

def consulte_descricao_produto(produtos):
  """ Essa função mostra a descrição e as Informações adicionais de um dado produto
  """


def ative_sistema(produtos):
  """ Essa função aceita as interações do usuário, coordenando qual ação deve ser tomada
      Cada ação refere-se as funções desenvolvidas acima.
      Nota: o que fazer se for inserida uma ação inválida?
  """
  loop = True
  while loop:
    escolha = input(
      """
      Escolha uma das funções:
      1. Cadastrar um produto
      2. Apagar um produto
      3. Adicionar itens ao estoque de um produto
      4. Remover itens ao estoque de um produto
      5. Consultar produtos
      6. Consultar a descrição de um produto específico
      7. Fechar o programa
      """
    )
    if escolha == '1':
      cadastre_produto(produtos)
    elif escolha == '2':
      pass
    elif escolha == '3':
      pass
    elif escolha == '4':
      pass
    elif escolha == '5':
      consulte_produtos(produtos)
    elif escolha == '6':
      pass
    elif escolha == '7':
      pass
    else:
      pass


ative_sistema(produtos)