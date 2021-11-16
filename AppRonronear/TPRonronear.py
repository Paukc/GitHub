""" Horwell Murillo
Ailín Perez
Flor Frez
Micaela Christmann
Paula Agüero"""


diccionario = {"Wally": [], "Benito": []}
lista_usuarios = ["Benito", "Wally", "911"]
lista_tweet = []
lista_arrobados = []
lista_noarrobados = []
usuario = ''
tweet = ''


class App:

    def __init__(self):
        pass

    def IngresarUsuario(self):
        global usuario
        usuario = input("Ingrese su usuario: ").lower()
        if usuario != lista_usuarios:
            lista_usuarios.append(usuario)
        self.crearTweet()

    def crearTweet(self):
        global diccionario
        global usuario
        global tweet
        tweet = input("Ingrese el tweet: ").lower()
        if tweet == "":
            print("El tweet ingresado esta vacio")
        else:
            separar = tweet.split(" ")
            if len(separar) < 16:
                nuevoTweet = "@{0}: {1}".format(usuario, tweet)
                if usuario in diccionario.keys():
                    diccionario[usuario].append(tweet)
                else:
                    diccionario[usuario] = [tweet]
                print(nuevoTweet)
            else:
                print("{0}, sobrepasa el limite de palabras para un tweet.".format(tweet))

    def listaTweets(self):
        global diccionario
        for i, j in diccionario.items():
            print('@'+i, ':', j)


App1 = App()


class Bot:
    def __init__(self, lista_negra, dict_marcas):
        self.lista_negra = ["matar", "robar", "ilegal", "drogas", "porno"]
        self.dict_marcas = {"Ariel": "lavar"}
   
    def listadoTweet(self):
        global tweet
        global lista_arrobados
        global lista_noarrobados
        if "@" in tweet:
            lista_arrobados.append(tweet)
        else:
            lista_noarrobados.append(tweet)

    def leerTweet(self):
        pass


class Benito(Bot):

    def __init__(self, lista_negra, dict_marcas):
        Bot.__init__(self, lista_negra, dict_marcas)

    def alertar(self, usuario, tweet):
        global diccionario
        alerta = "@911, Sistema de alerta automatica.\n\tusuario: @{0};\n\tTweet: {1}".format(usuario, tweet)
        diccionario['Benito'].append(alerta)
        print(alerta)

    def leerTweet(self):
        global usuario
        global tweet
        tweet_separado = tweet.split(" ")
        for i in tweet_separado:
            if i in self.lista_negra:
                self.alertar(usuario, tweet)


class Wally(Bot):
    def __init__(self, dict_marcas):
        Bot.__init__(self, "", dict_marcas)
        
    def promocionar(self, usuario, tweet):
        global diccionario
        alerta = "La marca @{0}, te ofrece un 10% en tu proxima compra, para acceder mandanos un privado. @{1}".format(self.dict_marcas.keys(), usuario)
        diccionario['Wally'].append(alerta)
        print(alerta)

    def leerTweet(self):
        global usuario
        global tweet
        tweet_separado = tweet.split(" ")
        for i in tweet_separado:
            if i in self.dict_marcas.values():
                self.promocionar(usuario, tweet)
               
                   
class Termitator(Bot):

    def __init__(self):
        Bot.__init__(self, "", "")

    def listadoTweet(self):
        global tweet
        global lista_arrobados
        global lista_noarrobados
        print("Ingrese el usuario del que quiere ver la pantalla principal:")
        self.usuariosol = input()
        for i, j in diccionario.items():
            j = tweet.split(" ")
            if '@'+self.usuariosol in j:
                if tweet not in lista_arrobados:
                    lista_arrobados.append(tweet)
                    print("Tweets de la Home del usuario:", lista_arrobados)
                elif tweet in lista_arrobados:
                    print("Tweets de la Home del usuario:", lista_arrobados)
                else:
                    print("El usuario no ha sido mencionado")
            if '@'+self.usuariosol in i:
                if tweet not in lista_noarrobados:
                    lista_noarrobados.append(tweet)
                    print("Tweets que no arroban a nadie:", lista_noarrobados)
                else:
                    print("Tweets que no arroban a nadie:", lista_noarrobados)
            if '@'+self.usuariosol not in i:
                if '@'+self.usuariosol not in j:
                    print("El usuario ingresado es incorrecto")


Bot1 = Bot("", "")
Benito1 = Benito("", "")
Wally1 = Wally("")
Terminator1 = Termitator()
