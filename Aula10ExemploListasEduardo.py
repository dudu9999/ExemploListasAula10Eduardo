


listaDeNomes = ["aa","bbb","cccc","ddddd","eeeeee"]
listaDeIdades= ["11","22","33","44","55"]
somadasidades, mediaidades, contadorIdade = 0, 0, 0
#listaDeNomes = []
#listaDeIdades= []

menu = '''
Menu
0- FIM
1- Cadastro
2- Relatório
3- Altera Idade
4- Altera Nome
5- Média de Idades
6- Quantas Pessoas tem idade a cima da média
7- Limpar as Listas
8- Imprima um Retangulo em volta de cada nome cadastrado
Escolha: '''


while True:
    escolha = input(menu)

    if escolha == "0":
        print("\nFim.\nAte logo amigo!")
        break
    
    if escolha == "1":
        while True:
            print("\nCadastro:")
            nome  = input("Digite um nome: ")
            if len(nome) == 0 or nome.upper() == "FIM":
                print("\nFim do Cadastro")
                break
            idade = input("Digite a idade: ")        
            listaDeNomes.append(nome)
            listaDeIdades.append(idade)
        
    if escolha == "2":
        print("\nRelatório:")
        for x in range(len(listaDeNomes)):
            print("Nome: ",listaDeNomes[x],"\nIdade: ",listaDeIdades[x],"\n")

    if escolha == "3":
        print("Localiza Pessoa:")
        nome = input("Digite o nome para localizar: ")

        ind = 0
        for n in listaDeNomes:
            if nome == n:
                print("Localizei o",nome,listaDeIdades[ind])
                listaDeIdades[ind] = input("Nova Idade: ")
            ind += 1

    if escolha == "4":
        print("Localiza Pessoa:")
        nome = input("Digite o nome para localizar: ")

        ind = 0
        for n in listaDeNomes:
            if nome == n:
                print("Localizei o",nome,listaDeIdades[ind])
                listaDeNomes[ind] = input("Novo Nome: ")
            ind += 1

    if escolha == "5":
        x= 0
        for n in listaDeIdades:
            somadasidades = (int(somadasidades) + int(listaDeIdades[x]))
            x+=1
        mediaidades = (int(somadasidades) // len(listaDeIdades))
        print("\nA média das idades é: ",int(mediaidades))

    if escolha == "6":
        x= 0
        for n in listaDeIdades:
            somadasidades = (int(somadasidades) + int(listaDeIdades[x]))
            x+=1
        mediaidades = (int(somadasidades) // len(listaDeIdades))
        x= 0
        for n in listaDeIdades:
            if int(listaDeIdades[x]) > mediaidades:
                contadorIdade +=1               
            x+=1
        print("\nAcima da média das idades possui ",int(contadorIdade)," na lista.")

    if escolha == "7":
        listaDeIdades.clear()
        listaDeNomes.clear()
        print("\nListas limpa! ")

    if escolha == "8":
        for x in range(len(listaDeNomes)):
            print("\nNome:")
            print(listaDeNomes[x])
            linha = "#"*len(listaDeNomes[x])
            
            for x in range(len(listaDeNomes[x])):
                print(linha)



            

        
