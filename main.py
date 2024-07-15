def mensagem():
    print("***********************************************")
    print("Bem vindo ao sistema de recomendação de musicas")
    print("***********************************************")



        

def recomendar_rock():
        print("Genero escolhido: Rock")
        recomenda = (str(input("Gostaria de uma recomendação de musica? (Sim/Não)"))).lower() 

        if recomenda == 'sim':
            rockMusic = (str(input('Escolha uma banda: ACDC, Queen, Nirvana: ' ))).lower() 
            print("banda escolhida: ", rockMusic)

            if rockMusic == 'ACDC'.lower() :
                print("Musica recomendada: Thunderstruck")
            elif rockMusic == 'Queen'.lower() :
                print("Musica recomendada: Bohemian Rhapsody")
            elif rockMusic == 'Nirvana'.lower() :
                print("Musica recomendada: Smells Like Teen Spirit")
            else:
                 print("Banda não conhecida, por favor tente outra vez.")


        else:
            print("Ok, obrigado")



         
  
def recomendar_pop():
    print(f'Genero escolhido: Pop')
    recomenda = (str(input("Gostaria de uma recomendação de musica? (Sim/Não)"))).lower()  

    if recomenda == "sim":
        popMusic = (str(input('Escolha um cantor(a): Bruno Mars, Britney Spears, Taylor Swift :  '))).lower()
        print("Cantor(a) escolhido: ", popMusic)

        if popMusic == 'Bruno Mars'.lower() :
            print("Musica recomendada: Just the Way You Are")
        elif popMusic == 'Britney Spears'.lower() :
            print("Musica recomendada: Oops!... I Did It Again")
        elif popMusic == 'Taylor Swift'.lower() :
            print("Musica recomendada: Blank Space")
        else:
                print("Banda não conhecida, por favor tente outra vez.")


    else:
        print("Ok, obrigado")


def recomendar_hiphop():
        print("Genero escolhido: Hiphop")

        recomenda = (str(input("Gostaria de uma recomendação de musica? (Sim/Não)"))).lower()  

        if recomenda == "sim":
            hiphopMusic = (str(input('Escolha um(a) rapper: Travis Scott, Kendrick Lamar, Cardi B :'  ))).lower()
            print("Rapper escolhido: ", hiphopMusic)


            if hiphopMusic == 'Travis Scott'.lower() : 
                print("Musica recomendada: SICKO MODE")

            elif hiphopMusic == 'Kendrick Lamar'.lower() :
                print("Musica recomendada: DNA")

            elif hiphopMusic == 'Cardi B'.lower() :
                print("Musica recomendada: I Like It")

            else:
                    print("Banda não conhecida, por favor tente outra vez.")


        else:
            print("Ok, obrigado")



def recomenda_indie():
        print("Genero escolhido: indie")

        recomenda = (str(input("Gostaria de uma recomendação de musica? (Sim/Não)"))).lower() 

        if recomenda == 'sim':
            
            indieMusic = (input('Escolha um grupo: Arctic Monkeys, Tame Impala, Muse :' ))
            
            if indieMusic == 'Arctic Monkeys'.lower() :
                print("Musica recomendada: Do I Wanna Know?")

            elif indieMusic == 'Tame Impala'.lower() : 
                print("Musica recomendada: The less I know the better")

            elif indieMusic == 'Muse'.lower() :
                print("Musica recomendada: Uprising ")

            else:
                    print("Banda não conhecida, por favor tente outra vez.")


        else:
            print("Ok, obrigado")

def musicas():
     mensagem()
     generoMusical = input("Escolha o genero musical que deseja (Rock, Pop, Hiphop, indie): ").lower()

     if generoMusical == 'rock':
        recomendar_rock()

     elif generoMusical == 'pop':
        recomendar_pop()

     elif generoMusical == 'hiphop':
        recomendar_hiphop()

     elif generoMusical == 'indie':
        recomenda_indie()

     else:
        print("Genero musical invalido")

musicas()