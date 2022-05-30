from os import system
system('cls')
def number_menu():
  system('pause')
  system('cls')
  print('1) Cadastrar funcionário ')
  print('2) Alterar funcionário ')
  print('3) Listar todos funcionários ')
  print('4) Excluir um funcionário ')
  print('5) Adicionar um aumento de salário ')
  print('0) Para sair do programa ' )
number_menu()
resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
system('cls')
dicionario = {}
while resultado_do_menu != -2:
  if resultado_do_menu == 1: 
    print('Vamos cadastrar o funcionário agora!!') 
    nome = (input('Digite o nome do funcionário que você quer cadastrar: '))
    email = (input('Digite o email do funcionário: '))
    codigo = (input('Digite o código que esse funcionário vai ter: '))
    admissao = (input('Digite a data de admissão desse funcionário: '))
    salario = (input('Digite o salário que ele inicialmente vai ganhar: '))  
    dicionario[nome] = { 'email':email,'codigo':codigo,'admissao':admissao,'salario':salario }
    number_menu()
    resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
    system('pause')
    system('cls')
  elif resultado_do_menu == 2:
    print('Vamos alterar o dado do funcionário: ')
    print('Esses são nossos funcionários: ')
    for funcionarios in dicionario:
      print(funcionarios)
    alterar_dados = input('Digite o nome do funcionário que você deseja alterar os dados dele: ')
    print('Esses são os dados do funcinário que você menicionou: ')
    print(dicionario[alterar_dados])
    if alterar_dados not in  dicionario:
      print('Desculpa mas esse funcionário ainda não foi cadastrado.')
      number_menu()
      resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
    dado_alterado = input('Qual dado você deseja alterar: ')
    dado_novo = input('Digite o dado novo que você quer colocar: ')
    dicionario[alterar_dados][dado_alterado] = dado_novo
    print('Dado alterado com sucesso')
    print(dicionario[alterar_dados])
    number_menu()
    resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
    system('pause')
    system('cls')
  elif resultado_do_menu == 3:
    if dicionario == {}:
      print('Desculpe mas ainda não temos funcionários na lista')
      system('pause')
      number_menu()
      resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: ')) 
    print(dicionario)
    system('pause')
    number_menu()
    resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: ')) 
    system('pause')
    system('cls')
 
  elif resultado_do_menu == 4:
    print('Vamos excluir o funcionário agora :)')
    print('Esses são nossos funcionários')
    for funcionarios in dicionario:
      print(funcionarios)
    funcionario_excluir = input('Digite o nome do funcionario que você deseja excluir: ')
    dicionario.pop(funcionario_excluir)
    print('Funcionário excluido com sucesso,até mais!')
    number_menu()
    resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
    system('pause')
    system('cls')
 
  elif resultado_do_menu == 5:
    print('Vamos fazer um aumento de salário: ')
    print('Esses são nossos funcionários')
    for funcionarios in dicionario:
      print(funcionarios)
    funcionario_aumento = input('Digite o nome do funcionário que você deseja da um aumento no salário : ')
    aumento = input('Você deseja que o salário desse funcionário fique quanto agora? : ')
    dicionario[funcionario_aumento]['salario'] = aumento
    print('Pronto o funcionário que você escolheu está recebendo agora o valor que você digitou')
    print(dicionario[funcionario_aumento])
    number_menu()
    resultado_do_menu = int(input('Digite um dos números da alternativa porfavor: '))
    system('pause')
    system('cls')
  elif resultado_do_menu == 0:
    print('Você saiu do programa, obrigado e até a próxima :) ')
    break 