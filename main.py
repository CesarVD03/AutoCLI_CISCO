import logica.metodos as mtd
linea = ""

print("=============================================================================================")
print("Bienvenido a CLI_WORK DICCIONARI")
print("=============================================================================================")

control = input("Preciona enter para continuar\n> ")

#menu principal
print("")
mtd.menu_principal()
op = int(input("> "))

match op:
    #Configuraciones rapidas
    case 1:
        print("")
        print("MENU DE CONFIGURACION RAPIDA")
        print("")
        
        mtd.menu_ConfRa()
        opI = int(input("Ingresa una opcion\n> "))
        
        match opI:
            #Cambiar nombre
            case 1:
                mtd.clear()
                linea = mtd.cambiar_nombre("")
                        
                print("\nPudes copiar desde aqui [puede que se haya copiaso ya]: \n")
                print(linea)
                mtd.cp(linea)
            
            #texto al iniciar el dispositvo
            case 2:    
                mtd.clear()
                linea = mtd.texo_inicio("")
                
                print("\nPudes copiar desde aqui [puede que se haya copiaso ya]: \n")
                print(linea)
                mtd.cp(linea)
        
