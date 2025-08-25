import json
import colorama

print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +"                                                       ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ╔═╗╔═╗    ╔═══╗╔╗            ╔═══╗          ╔╗        ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ║║╚╝║║    ║╔═╗╠╝╚╗           ║╔═╗║          ║║        ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ║╔╗╔╗╠╗ ╔╗║╚══╬╗╔╬═╦══╦══╦╗╔╗║╚══╦══╦══╦═╦══╣╚═╦══╦═╗ ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ║║║║║║║ ║║╚══╗║║║║╔╣║═╣╔╗║╚╝║╚══╗║║═╣╔╗║╔╣╔═╣╔╗║║═╣╔╝ ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ║║║║║║╚═╝║║╚═╝║║╚╣║║║═╣╔╗║║║║║╚═╝║║═╣╔╗║║║╚═╣║║║║═╣║  ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +" ╚╝╚╝╚╩═╗╔╝╚═══╝╚═╩╝╚══╩╝╚╩╩╩╝╚═══╩══╩╝╚╩╝╚══╩╝╚╩══╩╝  ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +"      ╔═╝║                                             ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +"      ╚══╝                                             ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)
print(colorama.Fore.BLACK + colorama.Style.BRIGHT + colorama.Back.BLUE +"                                                       ".center(125) +colorama.Fore.RESET + colorama.Back.RESET)

#////////FUNCIONES\\\\\\\\

'//MOSTRAR LA LISTA COMPLETA DE PELÍCULAS'
def mostrar_peliculas(peliculas):
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "="*125 + "\n" + "LISTA DE PELICULAS".center(125) + "\n" + "="*125)
    print(f"{'NRO'.center(5)}\t{'NOMBRE'.center(40)}\t{'GÉNERO'.center(15)}\t{'PLATAFORMA'.center(15)}\t{'DURACIÓN'.center(15)}\t{'FECHA DE ESTRENO'.center(15)}" + "\n" + colorama.Fore.RESET)
    for peli in peliculas: # mostrar la 'peli' en la lista de 'peliculas'
        print(f"{str(peli['nro_orden']).center(5)}\t{peli['nombre'].capitalize().center(40)}\t{peli['genero'].capitalize().center(15)}\t{peli['plataforma'].upper().center(15)}\t{peli['duracion'].center(15)}\t{str(peli['fecha_estreno']).center(15)}")

'//MOSTRAS PELICULAS SEGUN FILTROS'
def filtrar_por_plataforma(peliculas, plataforma_filtro):
    peliculas_filtradas = []
    for pelicula in peliculas:
        if pelicula['plataforma'].lower() == plataforma_filtro.lower():
            peliculas_filtradas.append(pelicula)
    if peliculas_filtradas:
        print("=" * 125 + "\n" + f"PELÍCULAS FILTRADAS POR PLATAFORMA:  {plataforma_filtro}".center(125) + "\n" + "="*125)
        print(f"{'NRO'.center(5)}\t{'NOMBRE'.center(40)}\t{'PLATAFORMA'.center(15)}\t{'DURACIÓN'.center(15)}\t{'FECHA DE ESTRENO'.center(15)}" + colorama.Fore.RESET)
        for peli in peliculas_filtradas: #estaba mal dentro del for anterior porque lo imprimía cada vez, tiene que ir separada con un if  
            print(f"{str(peli['nro_orden']).center(5)}\t{peli['nombre'].capitalize().center(40)}\t{peli['plataforma'].upper().center(15)}\t{peli['duracion'].center(15)}\t{str(peli['fecha_estreno']).center(15)}")
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +"ERROR. \nPor favor ingrese una opción valida." + colorama.Fore.RESET)
    return peliculas_filtradas

def filtrar_por_genero(peliculas, genero_filtro):
    genero_filtradas = []
    for pelicula in peliculas:
        if pelicula['genero'].lower() == genero_filtro.lower(): 
            genero_filtradas.append(pelicula)
    if genero_filtradas:
        print(f"=" * 125 + "\n" + f"PELÍCULAS FILTRADAS POR GENERO:  {genero_filtro}".center(125) + "\n" + "="*125)
        print(f"{'NRO'.center(5)}\t{'NOMBRE'.center(40)}\t{'GENERO'.center(15)}\t{'DURACIÓN'.center(15)}\t{'FECHA DE ESTRENO'.center(15)}" + colorama.Fore.RESET)
        for peli in genero_filtradas: #estaba mal dentro del for anterior porque lo imprimía cada vez, tiene que ir separada con un if
            print(f"{str(peli['nro_orden']).center(5)}\t{peli['nombre'].capitalize().center(40)}\t{peli['genero'].upper().center(15)}\t{peli['duracion'].center(15)}\t{str(peli['fecha_estreno']).center(15)}")
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +"ERROR. \nPor favor ingrese una opción valida." + colorama.Fore.RESET)
    return genero_filtradas

'//MOSTRAR LAS PELÍCULAS FAVORITAS'
def mostrar_favoritos_peli():
    print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "="*125 + "\n" + "LISTA DE PELICULAS FAVORITAS".center(125) + "\n" + "="*125)
    print(f"{'NRO'.center(5)}\t{'NOMBRE'.center(40)}\t{'GÉNERO'.center(15)}\t{'PLATAFORMA'.center(15)}\t{'DURACIÓN'.center(15)}\t{'FECHA DE ESTRENO'.center(15)}" + colorama.Fore.RESET)
    for peli in favoritos_peli: # mostrar las 'peli' que se guardaron en 'favoritos_peli'
        print(f"{str(peli['nro_orden']).center(5)}\t{peli['nombre'].capitalize().center(40)}\t{peli['genero'].capitalize().center(15)}\t{peli['plataforma'].upper().center(15)}\t{peli['duracion'].center(15)}\t{str(peli['fecha_estreno']).center(15)}")

'//LEER Y GUARDAR ARCHIVO JSON'

def leer_json (usuario):
    nombre_archivo = f'favoritos{usuario.lower()}.json'
    try:
        archivo = open (nombre_archivo, 'r')
        datos = json.load(archivo)
    except FileNotFoundError:
        datos = []
    except json.JSONDecodeError:
        datos = []
    return datos

def guardar_json(usuario, favoritos_peli):
    nombre_archivo = f'favoritos{usuario.lower()}.json'
    archivo = open(nombre_archivo, 'w')
    datos = favoritos_peli
    json.dump(datos, archivo, indent=4)

'//AGREGAR UNA PELÍCULA A FAVORITOS'
def agregar_peli_favorito(favoritos_peli, peliculas):
    facha = "-" * 31
    print(colorama.Fore.MAGENTA+ colorama.Style.BRIGHT + "\n" + "AGREGAR PELÍCULA A TUS FAVORITOS." + colorama.Fore.RESET)
    mostrar_peliculas(peliculas)
    while True:
        eleccionfav = int(input(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + f"\n" + "INGRESA EL NÚMERO DE PELÍCULA ELEGIDA O INGRESA 0 PARA VOLVER AL MENU PRINCIPAL " + colorama.Fore.RESET))    
        try:
            if eleccionfav == 0: # hacemos un if para que al salir no siga ejecutando toda la función
                break
            elif eleccionfav != 0:
                encontrado = False
                for peli in favoritos_peli:
                    if peli ["nro_orden"] == eleccionfav:
                        print (colorama.Fore.RED + "La película ya estaba en la lista." + colorama.Fore.RESET)
                        encontrado = True
                        break
            if not encontrado:
                for peli in peliculas:  # mostrar 'peli' en la lista de 'peliculas'
                        if peli["nro_orden"] == eleccionfav: # si la peli está en la lista el codigo sigue, nombre en minuscula para compatibilidad
                            favoritos_peli.append(peli) # agrega la película a la lista de favoritos
                            guardar_json(usuario, favoritos_peli)
                            print(colorama.Fore.GREEN + f"\n{facha}\n|Película agregada a favoritos|\n{facha}" + colorama.Fore.RESET)
                            return
                print(colorama.Fore.RED + "La película no esta en la lista." + colorama.Fore.RESET)                     
        except ValueError:
                    print(colorama.Fore.RED + "Por favor, ingrese un número válido." + colorama.Fore.RESET)
                    continue

'//ELIMINAR PELÍCULA FAVORITA'
def eliminar_pelicula_favoritos():
    facha = "-" * 36
    print(colorama.Fore.MAGENTA+ colorama.Style.BRIGHT + "\n" + "ELIMINAR PELÍCULA A TUS FAVORITOS." + colorama.Fore.RESET)
    mostrar_favoritos_peli()
    while True:
        try:
            favborrado= int(input(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + f"\n" + "INGRESA EL NÚMERO DE PELÍCULA FAVORITA A BORRAR O INGRESA 0 PARA VOLVER AL MENU PRINCIPAL " + colorama.Fore.RESET))
            if favborrado == 0: # hacemos un if para que al salir no siga ejecutando toda la función
                break
            else:
                for peli in favoritos_peli:  # mostrar 'peli' en la lista de 'peliculas'
                    if peli["nro_orden"] == favborrado: # si la peli está en la lista el codigo sigue, nombre en minuscula para compatibilidad
                        favoritos_peli.remove(peli) # agrega la película a la lista de favoritos
                        guardar_json(usuario, favoritos_peli)
                        print(colorama.Fore.GREEN + f"\n{facha}\n|Película eliminada de favoritos|\n{facha}" + colorama.Fore.RESET)
                        return 
                print(colorama.Fore.RED + "La película no esta en la lista." + colorama.Fore.RESET)
        except ValueError:
                    print(colorama.Fore.RED + "Por favor, ingrese un número válido." + colorama.Fore.RESET)
                    continue

#////////DICCIONARIOS\\\\\\\\

peliculas = [
    {
        "nro_orden": 1,
        "nombre": "animales nocturnos",
        "genero": "thriller",
        "plataforma": "netflix",
        "duracion": "115 min",
        "fecha_estreno": "1 de Junio"
    },
    {
        "nro_orden": 2,
        "nombre": "chicas pesadas",
        "genero": "comedia",
        "plataforma": "netflix",
        "duracion": "97 min",
        "fecha_estreno": "4 de Junio"
    },
    {
        "nro_orden": 3,
        "nombre": "cuando acecha la maldad",
        "genero": "terror",
        "plataforma": "netflix",
        "duracion": "99 min",
        "fecha_estreno": "14 de Junio"
    },
    {
        "nro_orden": 4,
        "nombre": "get out",
        "genero": "terror",
        "plataforma": "netflix",
        "duracion": "103 min",
        "fecha_estreno": "16 de Junio"
    },
    {
        "nro_orden": 5,
        "nombre": "detonantes",
        "genero": "thriller",
        "plataforma": "netflix",
        "duracion": "106 min",
        "fecha_estreno": "21 de Junio"
    },
    {
        "nro_orden": 6,
        "nombre": "un asunto familiar",
        "genero": "comedia",
        "plataforma": "netflix",
        "duracion": "105 min",
        "fecha_estreno": "28 de Junio"
    },
        {
        "nro_orden": 7,
        "nombre": "madame web",
        "genero": "accion",
        "plataforma": "max",
        "duracion": "116 min",
        "fecha_estreno": "3 de Junio"
    },
    {
        "nro_orden": 8,
        "nombre": "trolls 3: se armó la banda",
        "genero": "infantil",
        "plataforma": "max",
        "duracion": "91 min",
        "fecha_estreno": "5 de Junio"
    },
    {
        "nro_orden": 9,
        "nombre": "am i ok",
        "genero": "drama",
        "plataforma": "max",
        "duracion": "86 min",
        "fecha_estreno": "7 de Junio"
    },
    {
        "nro_orden": 10,
        "nombre": "five nights at freddy's",
        "genero": "terror",
        "plataforma": "max",
        "duracion": "110 min",
        "fecha_estreno": "8 de Junio"
    },
    {
        "nro_orden": 11,
        "nombre": "evidencias del amor",
        "genero": "comedia",
        "plataforma": "max",
        "duracion": "105 min",
        "fecha_estreno": "23 de Junio"
    },
    {
        "nro_orden": 12,
        "nombre": "power of the dream",
        "genero": "documental",
        "plataforma": "prime",
        "duracion": "133 min",
        "fecha_estreno": "18 de Junio"
    },
    {
        "nro_orden": 13,
        "nombre": "federer: los doce últimos días",
        "genero": "documental",
        "plataforma": "prime",
        "duracion": "125 min",
        "fecha_estreno": "20 de Junio"
    },
    {
        "nro_orden": 14,
        "nombre": "soy céline dion",
        "genero": "documental",
        "plataforma": "prime",
        "duracion": "102 min",
        "fecha_estreno": "25 de Junio"
    },
    {
        "nro_orden": 15,
        "nombre": "divorce in the black",
        "genero": "drama",
        "plataforma": "prime",
        "duracion": "143 min",
        "fecha_estreno": "11 de Junio"
    },
    {
        "nro_orden": 16,
        "nombre": "my spy: the eternal city",
        "genero": "comedia",
        "plataforma": "prime",
        "duracion": "150 min",
        "fecha_estreno": "18 de Junio"
    },
    {
        "nro_orden": 17,
        "nombre": "diane von furstenberg: definiendo estilo",
        "genero": "documental",
        "plataforma": "disney",
        "duracion": "97 min",
        "fecha_estreno": "25 de Junio"
    },
    {
        "nro_orden": 18,
        "nombre": "los descendientes: corazon rebelde",
        "genero": "accion",
        "plataforma": "disney",
        "duracion": "102 min",
        "fecha_estreno": "12 de Junio"
    },
    {
        "nro_orden": 19,
        "nombre": "canta y no llores",
        "genero": "comedia",
        "plataforma": "disney",
        "duracion": "92 min",
        "fecha_estreno": "26 de Junio"
    },
    {
        "nro_orden": 20,
        "nombre": "se busca cita",
        "genero": "comedia",
        "plataforma": "disney",
        "duracion": "105 min",
        "fecha_estreno": "3 de Junio"
    },
    {
        "nro_orden": 21,
        "nombre": "jim henson: el hombre y las ideas",
        "genero": "documental",
        "plataforma": "disney",
        "duracion": "107 min",
        "fecha_estreno": "31 de Junio"
    }
]

#se hace diccionario de usuarios para que haya varios, eventualmente se podía poner la opción crear usuario nuevo
usuarios = {
    #usuario  contraseña
    "user_Mar": "123",
    "user_Nic": "213",
    "user_Agus": "312",
    "user_Vis": "132",
    "user_Norberto":"elprofe"
}

#////////MENÚ- Buscar estreno de peliculas por plataforma.\\\\\\\\
print (colorama.Fore.CYAN + colorama.Style.BRIGHT + "\n" + "Inicio de sesión".center(125,' ') + "\n" + colorama.Fore.RESET)
contador = 0
while contador <= 3:
    contador += 1
    usuario = input("Usuario: ") 
    contraseña = input ("Contraseña: ")
    if usuario in usuarios and contraseña == usuarios[usuario]:  #datos para iniciar sesión
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "="*125 + "\n" + "Iniciando sesión...".center(127) + "\n" + "|ACCESO CONCEDIDO|".center(125) + "\n" + "="*125 + colorama.Fore.RESET)
        favoritos_peli = leer_json (usuario)
        while True:
            print("\n" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "="*125 + "\n" + "|MENU|".center(125) + "\n" + "="*125 + colorama.Fore.RESET)
            print(colorama.Fore.LIGHTMAGENTA_EX + "ELIGE UNA OPCIÓN:" + colorama.Fore.RESET)
        #AGREGUÉ VALIDACIÓN DE ERRORES
            try:
                opcion = int(input("1- Ver todos los estrenos de películas.\n2- Buscar película.\n3- Mis Favoritos.\n4- Salir del programa.\n\nOpción: "))
            except ValueError:
                print(colorama.Fore.RED + "Por favor, ingrese un número válido.")
                continue
            print(" ")
            match opcion:
                case 1: #muestra la lista completa de películas
                    mostrar_peliculas(peliculas)
                case 2: #hace una busqueda según los filtros (genero y plataforma de streaming)
                    while True:
                        print("\n" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "="*125 + "\n" + "|BUSCAR PELÍCULA|".center(125) + "\n" + "="*125 + "\n" + "ELIGE ENTRE ESTAS OPCIONES:" + colorama.Fore.RESET)
                        try:
                            eleccion = int(input("1- Filtrar por plataforma \n2- Filtrar por genero \n3- Volver al menú principal. \n\nOpción: "))
                            if eleccion == 1:
                                plataforma_filtro = input(colorama.Fore.MAGENTA +colorama.Style.BRIGHT +"\nPLATAFORMA ELEGIDA: ")
                                peliculas_filtradas = filtrar_por_plataforma(peliculas, plataforma_filtro)
                            elif eleccion == 2:
                                genero_filtro = input(colorama.Fore.MAGENTA + colorama.Style.BRIGHT +"\nGENERO ELEGIDO: ")
                                genero_filtradas = filtrar_por_genero(peliculas, genero_filtro)
                            elif eleccion == 3:
                                print(colorama.Fore.GREEN + colorama.Style.BRIGHT+"Saliendo al menú principal...".center(125) + colorama.Fore.RESET)
                                break
                        except ValueError:
                            print(colorama.Fore.RED + "Por favor, ingrese un número válido.")
                            continue    
                case 3: #sección favoritos (mostrar lista, agregar películas y eliminar películas)
                    while True:
                        print("\n" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "="*125 + "\n" + "|FAVORITOS|".center(125) + "\n" + "="*125 + colorama.Fore.RESET)
                        print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "\nELIGE ENTRE ESTAS OPCIONES: ")
                        print(colorama.Fore.RESET)
                        try:
                            eleccion = int(input("1- Agregar película a favoritos.\n2- Ver mis películas favoritas.\n3- Eliminar película de favoritos.\n4- Volver al menú principal.\n\nOpción: "))
                            if eleccion == 1:
                                agregar_peli_favorito(favoritos_peli, peliculas)
                            elif eleccion == 2:
                                mostrar_favoritos_peli()
                            elif eleccion == 3:
                                eliminar_pelicula_favoritos()
                            elif eleccion == 4:   
                                print(colorama.Fore.GREEN + colorama.Style.BRIGHT+"Saliendo al menú principal...".center(125) + colorama.Fore.RESET)
                                break
                        except ValueError:
                            print(colorama.Fore.RED + "Por favor, ingrese un número válido.")
                            continue
                case 4: #salir del programa
                    print(colorama.Fore.GREEN + colorama.Style.BRIGHT +"="*125 + "\n" + "¡¡¡GRACIAS POR UTILIZAR NUESTRA PLATAFORMA!!!".center(125) + "\n" + "VUELVA PRONTO".center(125) + "\n" + "="*125 + colorama.Fore.RESET)
                    exit()
                case _: #en caso de que 
                    print(colorama.Fore.RED +"ERROR".center(125) + "\n" + "Por favor elija una opción valida.".center(125) + colorama.Fore.RESET)
    elif contador <= 3:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "=" * 125 + "\n" + "|ACCESO DENEGADO|".center(125) + "\n" + f"POR FAVOR INTENTE NUEVAMENTE. (Intento {contador} de {3})".center(125) + "\n" + "=" * 125 + colorama.Fore.RESET)
    elif contador >= 3:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "=" * 125 + "\n" + "|ACCESO BLOQUEADO|".center(125) + "\n" + "HA EXCEDIDO EL NÚMERO MÁXIMO DE INTENTOS.".center(125) + "\n" + "=" * 125 + colorama.Fore.RESET)