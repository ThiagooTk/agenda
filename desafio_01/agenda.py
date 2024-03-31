"""
### Regras da aplicação

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer 
com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
"""

def adicionar_novo_contato(contatos, nome, telefone, email):
  contato = {"nome": nome, "telefone" : telefone , "email": email, "favorito": False }
  contatos.append(contato)
  print(f"{nome} foi adicionado com sucesso na sua agenda!")
  return
#♥
def visualizar_lista(contatos):
  print("\nContatos: ")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "♥" if contato["favorito"] else "♡"
    nome =  contato["nome"]
    telefone =  contato["telefone"]
    email =  contato["email"]
    print(f"{indice}. nome: {nome}  telefone: {telefone} e-mail: {email}  - [{favorito}]")
  return

def editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email):
  indice_c = int(indice) - 1
  if indice_c >= 0 and indice_c < len(contatos):
    contatos[indice_c]["nome"] = novo_nome
    contatos[indice_c]["telefone"] = novo_telefone
    contatos[indice_c]["email"] = novo_email
    print(f"Contato {indice} foi atualizado com sucesso!")
  else:
    print("Indice de contato inválido")
  return

def favoritar_contato(contatos,indice):
  indice_f = int(indice) - 1
  if contatos[indice_f]["favorito"] == True:
    contatos[indice_f]["favorito"] = False
  else:
    contatos[indice_f]["favorito"] = True
  print(f"Contato {indice} marcada como favorito!")
  return

def visualizar_lista_favoritos(contatos):
  print("\nContatos favoritos: ")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"] == True:
      nome =  contato["nome"]
      telefone =  contato["telefone"]
      email =  contato["email"]
      favorito = "♥"
      print(f"{indice}. nome: {nome}  telefone: {telefone} e-mail: {email}  - [{favorito}]")
    else:
      next
  
def apagar_contato(contatos, indice):
  for i, contato in enumerate(contatos, start=1):
    if i == indice:
      contatos.remove(contato)
      print(f"Contato {indice} apagado para com sucesso!")
  return

contatos = []

while True:
  print("\n Menu da agenda de contatos \o/ ")
  print("1. Adicionar um novo contato. ")
  print("2. Visualizar a lista de contatos cadastrados. ")
  print("3. Editar um contato. ")
  print("4. Marcar ou desmarcar favoritos. ")
  print("5. Visualizar a lista de contatos favoritos. ")
  print("6. Apagar um contato. ")
  print("7. Sair. ")


  escolha = input("Digite a operação desejada: ")

  if escolha == "1":
    nome = input("Digite o nome do conato: ")
    telefone = input("Digite o telefone do conato: ")
    email = input("Digite o email do conato: ")
    adicionar_novo_contato(contatos, nome, telefone, email)
  elif escolha == "2":
    visualizar_lista(contatos)
  elif escolha == "3":
    visualizar_lista(contatos)
    indice= input("Digite o número do contato que você deseja atualizar: ")
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Digite o novo número de telefone do contato: ")
    novo_email = input("Digite o novo e-mail do contato: ")
    editar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)
  elif escolha == "4":
    visualizar_lista(contatos)
    indice= input("Digite o número do contato que você deseja marcar ou desmarcar favorito: ")
    favoritar_contato(contatos,indice)
  elif escolha == "5":
    visualizar_lista_favoritos(contatos)
  elif escolha == "6":
    visualizar_lista(contatos)
    indice= input("Digite o número do contato que você deseja apagar: ")
    apagar_contato(contatos, int(indice))
  elif escolha == "7":
    break
    




