# Menú y llamado de métodos

from TPRonronear import *

print("\n\tBienvenido a la App Ronronear.")
menu = input("\t1: Entrar a su usuario\n\t2: Listar Tweets\n\t0: Salir\n\t")
while menu != "0":
    if menu == "1":
        App1.IngresarUsuario()
        Benito1.leerTweet()
        Wally1.leerTweet()
    elif menu == "2":
        menu2 = input("\t1: Ver todos los tweets\n\t2: Ingresar a home\n\t")
        if menu2 == "1":
            App1.listaTweets()
        elif menu2 == "2":
            Terminator1.listadoTweet()
        else:
            menu2 = input("\t1: Ver todos los tweets\n\t2: Ingresar a home\n\t")
    else:
        print("No es una elección valida.")
    menu = input("\n\t1: Entrar a su usuario\n\t2: Listar Tweets\n\t0: Salir\n\t")
