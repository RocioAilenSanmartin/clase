#TICKETS
import pickle, sys, os, random
os.system("cls") #para limpiar 
print("Hola, bienvenido al sistema de Tickets")
while True:
    #Menú principal
    print("Menu Principal:")
    print(" 1 - Generar un Nuevo Ticket")
    print(" 2 - Leer un ticket")
    print(" 3 - Salir")
    opcion=int( input("A continuación, ingrese el número de la opción que desea seleccionar: "))
    #Funciones
    def crear_ticket():
        nombre= input("Ingrese su nombre:  ")
        apellido= input("Ingrese su apellido: ")
        sector= input("Ingrese su sector: ")
        oficina= input("Ingrese su número de oficina (Ej, C-005): ")
        edificio= input("Ingrese el número de edificio (Ej, 42): ")
        asunto= input("Asunto de la solicitud: ")
        detalle= input("Detalle de la solicitud/problema presentado: ")
        numero_ticket= random.randint(1000,9999)
        print(f"Usted generó correctamente una nueva solicitud. Su número de ticket es {numero_ticket}. Recuerde el número de ticket, ya que será necesario para el seguimiento de la solicitud.")
        return {
                "nombre":f"{nombre}",
                "apellido":f"{apellido}",
                "sector":f"{sector}",
                "oficina":f"{oficina}",
                "edificio":f"{edificio}",
                "asunto":f"{asunto}",
                "detalle":f"{detalle}",
                "numero_ticket" : f"{int(numero_ticket)}"}
        
    def mostrar_ticket(ticket):
        print("Este es su ticket: ")
        print("===================================================================")
        print("                     Ticket de servicio                            ")
        print("===================================================================")
        print(f"Solicitante: {ticket["apellido"]},{ticket["nombre"]}")
        print(f"Sector: {ticket["sector"]}      Oficina: {ticket["oficina"]}     Edificio: {ticket["edificio"]}")
        print(f"Asunto: {ticket["asunto"]}                                ")
        print(f"Detalle: {ticket["detalle"]}")
        print(f"               NÚMERO DE TICKET: {ticket["numero_ticket"]}        ")
        print("===================================================================")   

    #Opciones de menu:  
    match opcion: 
        case 1: #ALTA TICKET:  
            while True:
                    print("A continuación deberá ingresar los datos para generar un nuevo Ticket")
                    ticket=crear_ticket() #estoy generando el ticket numero x
                    guardar=ticket["numero_ticket"] #nombre de archivo para guardar el ticket numero x
                    with open(f"{guardar}", "wb") as f: #Con este comando van a generar y guardar el archivo
                        pickle.dump(ticket, f) #la palabra ticket es una variable que contendra el diccionario
                    mostrar_ticket(ticket) #para mostrar el ticket numero x.
                    crear_siguiente_ticket= input("¿Desea crear un nuevo Ticket? (si/no): ").lower()
                    if crear_siguiente_ticket=="no":
                        break
                        #se rompe el while, vuelvo al menu principal
                    elif crear_siguiente_ticket != "si" and crear_siguiente_ticket != "no":
                        print("Ingrese una respuesta correcta")
                        
        case 2: #LEER TICKET
            while True:
                numero_ingresado=input("Ingrese el número de ticket: ")
                ruta=f"{numero_ingresado}"
                comprobar=os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista
                if comprobar==True:
                    abrir=f"{numero_ingresado}"
                    with open(abrir, "rb") as f:# la palabra abrir contendra el nombre del archivo a abrir 
                        ticket = pickle.load(f) #la palabra ticket es el diccionario donde se guardara ese objeto          
                    mostrar_ticket(ticket)
                    while True:
                        leer_ticket= input("¿Desea leer un nuevo Ticket? (si/no): ")
                        if leer_ticket=="no":
                            break #volver al menu principal
                        elif leer_ticket!= "si" and leer_ticket!="no":
                                print("Ingrese una respuesta correcta")
                        elif leer_ticket=="si":
                            break
                    if leer_ticket=="no":
                        break
                else:
                    print("Por favor, ingrese un número de ticket correcto") 
                    while True: 
                        intentar_de_nuevo = input("¿Desea intentar con otro número? (si/no): ").lower()
                        if intentar_de_nuevo == "no":
                            break
                        elif intentar_de_nuevo!= "si" and  intentar_de_nuevo!="no":
                            print("Ingrese una respuesta correcta")
                        elif  intentar_de_nuevo== "si":
                            break
                    if intentar_de_nuevo == "no":
                        break
        case 3: #SALIR
            while True:
                finalizar=input("¿Esta seguro que desea finalizar? (si/no)").lower()
                if finalizar=="si":
                    break
                elif finalizar!="si" and finalizar!="no":
                    print("Ingrese una respuesta correcta")
                else:
                    break
            if finalizar=="si":
                print("Hasta pronto")
                sys.exit() #con este comando cierra la ejecucion del programa