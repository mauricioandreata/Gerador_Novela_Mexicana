# Gerador de Novelas Mexicanas

from random import randint

def escolheDeLista(nomeLista):
    return nomeLista[randint(0, len(nomeLista)-1)] # Escolhe o valor de uma posição aleatória em uma lista enviada

class Personagem: # Classe onde estarão todas as personagens
    def __init__(self, genFem): # Atributos de nossa classe: genFem (Verifica se é Homem ou Mulher), nome e sobrenome
        self.genFem = genFem
        self.nome = ""
        self.sobrenome = ""

    def __str__(self):
        return f"{self.nome} {self.sobrenome}" # Retorna o nome completo da personagem quando chamado

    def completar(self): # Atualiza o objeto personagem com seu nome e sobrenome

        if(self.genFem == True):# Caso mulher
            arq = open("nomes_femininos.txt", mode = 'r', encoding="utf8") # Busca nomes femininos
            nomes = arq.read()
            listaNomes = nomes.split("\n")
            self.nome = escolheDeLista(listaNomes) # E atribui ao nome do objeto
            arq.close()
        else: # Caso homem
            arq = open("nomes_masculinos.txt", mode = 'r', encoding="utf8") # Busca nomes masculinos
            nomes = arq.read()
            listaNomes = nomes.split("\n")
            self.nome = escolheDeLista(listaNomes) # E atribui ao nome do objeto
            arq.close()

        arq = open("sobrenomes.txt", mode = 'r', encoding="utf8") # Busca sobrenomes
        sobrenomes = arq.read()
        listaSobrenomes = sobrenomes.split("\n")
        self.sobrenome = escolheDeLista(listaSobrenomes) # E atribui ao sobrenome do objeto
        arq.close()

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}" # Retorna o nome completo do objeto quando chamado


numeroProtagonistas = int(input("Digite o número de protagonistas (Par): ")) # Número de Protagonistas
listaProtagonistas = [] # Protagonistas armazenados em uma lista
for i in range(numeroProtagonistas):
    if(i+1 <= numeroProtagonistas/2): # Primeira metade dos protagonistas 
        q = Personagem(genFem=True)   # Serão mulheres
        q.completar()
        listaProtagonistas.append(q)  #Adicionando o protagonista na lista

    else:                             # Senão (Segunda metade dos protagonistas)
        q = Personagem(genFem=False)  # Serão homens
        q.completar()
        listaProtagonistas.append(q)  #Adicionando o protagonista na lista

numeroViloes = int(input("Digite o número de vilões (Par): ")) # Número de Vilões
listaViloes = [] # Vilões armazenados em uma lista
for i in range(numeroViloes):
    if(i+1 <= numeroViloes/2):       # Primeira metade dos vilões 
        q = Personagem(genFem=True)  # Serão mulheres
        q.completar()
        listaViloes.append(q) #Adicionando o vilão na lista

    else:                            # Senão (Segunda metade dos vilões)
        q = Personagem(genFem=False) # Serão homens
        q.completar()
        listaViloes.append(q) #Adicionando o vilão na lista

numeroCoadjuvantes = int(input("Digite o número de coadjuvantes (Par): ")) # Número de Coadjuvantes
listaCoadjuvantes = [] # Coadjuvantes armazenados em uma lista
for i in range(numeroCoadjuvantes):
    if(i+1 <= numeroCoadjuvantes/2):  # Primeira metade dos coadjuvantes 
        q = Personagem(genFem=True)   # Serão mulheres
        q.completar()
        listaCoadjuvantes.append(q)   # Adicionando o coadjuvante na lista

    else:                             # Senão (Segunda metade dos coadjuvantes)
        q = Personagem(genFem=False)  # Serão homens
        q.completar()
        listaCoadjuvantes.append(q)   # Adicionando o coadjuvante na lista

nomeNovela = str(input("Digite o nome da novela: ")) # Nome da Novela
numeroEpisodios = int(input("Digite o número de episódios da novela:")) # Número de Episódios

arqNovela = open(f"Resenha_de_{nomeNovela}.txt", mode = 'w') # Criando um arquivo de texto para a novela e apaga outros do mesmo nome
arqNovela.close()
arqNovela = open(f"Resenha_de_{nomeNovela}.txt", mode = 'a') # Com o modo 'a' não apagamos o texto existente, só colocamos na frente

print(f"\n*** Novela {nomeNovela.upper()} ***")
arqNovela.write(f"*** Novela {nomeNovela.upper()} ***\n")

print("\nProtagonistas")
arqNovela.write("\nProtagonistas\n")

print("=============")
arqNovela.write("=============\n")

for protagonista in listaProtagonistas:
    print(protagonista.nomeCompleto())                  # Escrevendo o nome dos protagonistas
    arqNovela.write(protagonista.nomeCompleto()+"\n")

print("\nVilões")
arqNovela.write("\nVilões\n")

print("======")
arqNovela.write("======\n")

for vilao in listaViloes:
    print(vilao.nomeCompleto())                 # Escrevendo o nome dos vilões
    arqNovela.write(vilao.nomeCompleto()+"\n")

print("\nCoadjuvantes")
arqNovela.write("\nCoadjuvantes\n")

print("============")
arqNovela.write("============\n")

for coadjuvante in listaCoadjuvantes:
    print(coadjuvante.nomeCompleto())                 # Escrevendo o nome dos coadjuvantes
    arqNovela.write(coadjuvante.nomeCompleto()+"\n")

arq = open("acoes.txt", mode = 'r', encoding="utf8")  # Abre o arquivo de ações
acoes = arq.read()
listaAcoes = acoes.split("\n")                        # E cria uma lista delas
arq.close()

arq = open("locais.txt", mode = 'r', encoding="utf8") # Abre o arquivo de locais
locais = arq.read()
listaLocais = locais.split("\n")                      # E cria uma lista deles
arq.close()


for i in range(1, numeroEpisodios+1): # Criando a história da novela

    if(i < numeroEpisodios): # Se o episódio não for o último
        print(f"\nEpisódio {i}")
        arqNovela.write(f"\nEpisódio {i}\n")

        print("===========")
        arqNovela.write("===========\n")

        for protagonista in listaProtagonistas:             # Para todo protagonista
            acao = escolheDeLista(listaAcoes)               # Escolhe aleatoriamente uma ação

            if(acao.find("@") != -1):                       # Se tiver '@' na ação 
                if(protagonista.genFem == True):            # Substitue por 'a' ou 'o' dependendo do gênero do protagonista
                    acao = acao.replace("@", "a")
                else:
                    acao = acao.replace("@", "o")
                
            coad = escolheDeLista(listaCoadjuvantes)        # Escolhe aleatoriamente um coadjuvante
            local = escolheDeLista(listaLocais)             # Escolhe aleatoriamente um local 

            if(local.find("@") != -1):                      # Se tiver '@' no local
                if(coad.genFem == True):                    # Substitue por 'a' ou 'o' dependendo do gênero do coadjuvante
                    local = local.replace("@", "a")
                else:
                    local = local.replace("@", "o")

            print(f"{protagonista.nome} {acao} {coad.nome} {local}")# Escreve o episódio da forma "<Protagonista> <ação> <coadjuvante> <local>"
            arqNovela.write(f"{protagonista.nome} {acao} {coad.nome} {local}\n")

        for vilao in listaViloes:                         # Para todo vilão
            acao = escolheDeLista(listaAcoes)             # Escolhe aleatoriamente uma ação

            if(acao.find("@") != -1):                     # Se tiver '@' na ação 
                if(vilao.genFem == True):                 # Substitue por 'a' ou 'o' dependendo do gênero do vilão
                    acao = acao.replace("@", "a")
                else:
                    acao = acao.replace("@", "o")

            protag = escolheDeLista(listaProtagonistas)   # Escolhe aleatoriamente um protagonista
            local = escolheDeLista(listaLocais)           # Escolhe aleatoriamente um local 

            if(local.find("@") != -1):                    # Se tiver '@' no local
                if(protag.genFem == True):                # Substitue por 'a' ou 'o' dependendo do gênero do protagonista
                    local = local.replace("@", "a")
                else:
                    local = local.replace("@", "o")

            print(f"{vilao.nome} {acao} {protag.nome} {local}")# Escreve o episódio da forma "<Vilão> <ação> <protagonista> <local>"
            arqNovela.write(f"{vilao.nome} {acao} {protag.nome} {local}\n")

        for protagonista in listaProtagonistas:          # Para todo Protagonista
            acao = escolheDeLista(listaAcoes)            # Escolhe aleatoriamente uma ação

            if(acao.find("@") != -1):                    # Se tiver '@' na ação 
                if(protagonista.genFem == True):         # Substitue por 'a' ou 'o' dependendo do gênero do protagonista
                    acao = acao.replace("@", "a")
                else:
                    acao = acao.replace("@", "o")

            vil = escolheDeLista(listaViloes)            # Escolhe aleatoriamente um vilão
            local = escolheDeLista(listaLocais)          # Escolhe aleatoriamente um local

            if(local.find("@") != -1):                   # Se tiver '@' no local
                if(vil.genFem == True):                  # Substitue por 'a' ou 'o' dependendo do gênero do vilão
                    local = local.replace("@", "a")
                else:
                    local = local.replace("@", "o")

            print(f"{protagonista.nome} {acao} {vil.nome} {local}")# Escreve o episódio da forma "<Protagonista> <ação> <vilão> <local>"
            arqNovela.write(f"{protagonista.nome} {acao} {vil.nome} {local}\n")

    else:        # Se o episódio for o último
        print("\nEpisódio Final")
        arqNovela.write("\nEpisódio Final\n")

        print("==============")
        arqNovela.write("==============\n")

        for vilao in listaViloes: # Para todo vilão
            arq = open("finais_viloes.txt", mode = 'r', encoding="utf8") # Abre o arquivo dos desfechos dos vilões
            desfechosVilao = arq.read()
            listaDesfechosVilao = desfechosVilao.split("\n") # Cria uma lista de desfechos dos vilões
            arq.close()

            desfVilao = escolheDeLista(listaDesfechosVilao) # Pega um desfecho aleatório
            if(desfVilao.find("@") != -1):
                if(vilao.genFem == True):                   # Se tiver '@'
                    desfVilao = desfVilao.replace("@", "a") # Substitue por 'a' se a vilã for mulher
                else:
                    desfVilao = desfVilao.replace("@", "o") # Ou por 'o' se o vilão for homem

            if(desfVilao.find("#") != -1):                  # Se tiver '#'
                protag = escolheDeLista(listaProtagonistas) # Substitue pelo nome de algum protagonista aleatoriamente
                desfVilao = desfVilao.replace("#", protag.nome)
            print(f"{vilao.nome} {desfVilao}") # Escreve o episódio final da forma "<Vilão> <desfecho>"
            arqNovela.write(f"{vilao.nome} {desfVilao}\n")

        for protagonista in listaProtagonistas: # Para todo protagonista
            arq = open("finais_protagonista.txt", mode = 'r', encoding="utf8") # Abre o arquivo dos desfechos dos protagonistas
            desfechosProtagonista = arq.read()
            listaDesfechosProtagonista = desfechosProtagonista.split("\n") # Cria uma lista de desfechos dos protagonistas
            arq.close()

            desfProtagonista= escolheDeLista(listaDesfechosProtagonista)  # Pega um desfecho aleatório
            if(desfProtagonista.find("@") != -1):
                if(protagonista.genFem == True):                          # Se tiver '@'
                    desfProtagonista = desfProtagonista.replace("@", "a") # Substitue por 'a' se a protagonista for mulher
                else:
                    desfProtagonista = desfProtagonista.replace("@", "o") # Ou por 'o' se o protagonista for homem

            if(desfProtagonista.find("#") != -1):                         # Se tiver '#'
                vil = escolheDeLista(listaViloes)                         # Substitue pelo nome de algum vilão aleatóriamente
                desfProtagonista = desfProtagonista.replace("#", vil.nome)
            print(f"{protagonista.nome} {desfProtagonista}") # Escreve o episódio final da forma "<Protagonista> <desfecho>"
            arqNovela.write(f"{protagonista.nome} {desfProtagonista}\n")

print("\n\n===")
print(f"Arquivo <Resenha_de_{nomeNovela}.txt> salvo com sucesso!")
arqNovela.close() # Fecha o arquivo com o texto da novela