produtos = {}

def cadastre_produto(produtos):
  """Essa função cadastra um novo produto com os campos:
    - nome do produto (obrigatório)
    - quantidade (opcional)
    - descrição (opcional)
    - outros campos
    Ps: o nome do produto é único, logo podemos pensar como uma chave única
  """

# Recebendo dados de imput
  nome = input('Qual o nome do produto para cadastrar? ').title()
  quantidade = input('Qual a quantidade para cadastrar? ')
  if quantidade == '':
    quantidade = 0
  quantidade = int(quantidade)
  if quantidade < 0:
    quantidade = 0
  descricao = input('Qual a descrição do produto para cadastrar? ').title()
  outros_valor = input('Informe as informações extras que deseja adicionar: ')

# Adicionado valores ao produto
  produto = {
    "nome": nome,
    "quantidade": quantidade,
    "descrição": descricao,
    "outros": outros_valor
  }

# Adicionado produtos ao dicionário de produtos
  produtos.update({nome: produto})
  print(f'O produto {produto} foi cadastrado')
  return produtos

def delete_produto(produtos):
  """ Essa função deleta um produto da base pelo `nome do produto`
  """
  deletar = input('Qual o nome do produto que voce deseja remover? ').title()
  if produtos.get(deletar):
    deletado = produtos.pop(deletar)
    print(f'O item de nome {deletado} foi apagado do sistema')
  else:
    print(f'Não foi encontrado o item de nome {deletar}')
  return produtos
  

def adicione_produto_estoque(produtos):
  """ Essa função adiciona ao estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """
  produto_modificar = input('Qual o nome do produto que você deseja modificar? ').title()
  if produtos.get(produto_modificar):
    quantidade = int(input('Quantos itens voce deseja adicionar ao estoque? '))
    if quantidade >= 0:
      quantidade_antes = produtos.get(produto_modificar).get('quantidade')
      quantidade_total = quantidade_antes + quantidade
      produtos[produto_modificar].update({"quantidade": quantidade_total})
      print(f'Foi adicionado {quantidade} itens ao produto {produtos[produto_modificar]}')
    else:
      print('Não é aceito quantidades negativas')
  else:
    print('O produto não existe')
  return produtos

def remova_produto_estoque(produtos):
  """ Essa função remove do estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """
  produto_modificar = input('Qual o nome do produto que você deseja modificar? ').title()
  if produtos.get(produto_modificar):
    quantidade = int(input('Quantos itens voce deseja remover do estoque? '))
    if quantidade >= 0:
      quantidade_antes = produtos.get(produto_modificar).get('quantidade')
      quantidade_total = quantidade_antes - quantidade
      if quantidade_total >= 0:
        produtos[produto_modificar].update({"quantidade": quantidade_total})
        print(f'Foi removido {quantidade} itens do produto {produtos[produto_modificar]}')
      else:
        print('Não é possivel ter estoque negativo, favor verificar a quantidade de itens retirados')
    else:
      print('Não é aceito quantidades negativas')
  return produtos

def consulte_produtos(produtos):
  """ Essa função mostra os produtos disponíveis no sistema (somente nome)
  """
  print('O produtos disponiveis são:')
  for chave, valor in produtos.items():
    print(chave)

def consulte_quantidade(produtos):
  """ Essa função mostra os produtos e a quantidade disponíveis no sistema
  """
  print('O produtos e quantidades disponiveis são:')
  for chave, valor in produtos.items():
    print(f'Item: {chave}, Quantidade: {valor["quantidade"]}')

def consulte_descricao_produto(produtos):
  """ Essa função mostra a descrição e as Informações adicionais de um dado produto
  """
  produto_consultar = input('Qual o nome do produto que você deseja consultar? ').title()
  if produtos.get(produto_consultar):
    produto = produtos[produto_consultar]['nome']
    descrição = produtos[produto_consultar]['descrição']
    outros = produtos[produto_consultar]['outros']
    print(f'Item: {produto}, Descrição: {descrição}, Outros: {outros}')


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
6. Produtos e quantidade disponível
7. Consultar a descrição de um produto específico
8. Fechar o programa
"""
    )
    if escolha == '1':
      produtos = cadastre_produto(produtos)
    elif escolha == '2':
      produtos = delete_produto(produtos)
    elif escolha == '3':
      produtos = adicione_produto_estoque(produtos)
    elif escolha == '4':
      produtos = remova_produto_estoque(produtos)
    elif escolha == '5':
      consulte_produtos(produtos)
    elif escolha == '6':
      consulte_quantidade(produtos)
    elif escolha == '7':
      consulte_descricao_produto(produtos)
    elif escolha == '8':
      print('Fechando o programa...')
      break
    else:
      print(f'O digito {escolha} é invalido, favor tentar novamente')


ative_sistema(produtos)