import comandos.basicos as b
import os
import pyperclip as pipe

#menus
def menu_principal():
    print("Elige una opcion: ")
    print("[1] Configuraciones rapidas (ej: Cambio de nombre, un puerto trunk, etc..).")
    print("[2] Configuraciones completas.")
    print("[3] Acerca de (!)")

def menu_ConfRa():
    print("Elige una opcion: ")
    print("[1] Cambio de mnombre.")
    print("[2] Texto al iniciar el dispositivo.")
    print("[3] Nombre de usuario y contraseña.")
    
    
#limpiar la terminal
def clear():
    print("\n"*50)
    
#copiar directo
def cp(txt):
    pipe.copy(txt)  
    
#control
def control ():
    print("Recerda tener tu dispositivo sin el modo admin (antes de dar >enable)")
    con =  input("preciona ENTER para continuar\n")      
   
     
#cambiar nombre
def cambiar_nombre(x):
    nombre = input(f"Ingresa el nombre que le asignaras a tu dispositivo {x}\n>")
    
    clear()
    control()
    clear()
    return "\n".join((
        b.habilitar(),
        b.mod_configurarcion(),
        b.cambiar_nombre(nombre),
        b.salir(),
        b.guardar_config(),        
        b.comentario(f"Se puso el nombre correctamente al dispositivo"),
        "",
    ))
    
#texto al inicio
def texo_inicio(x):
    txt = input(f"Ingresa el texto que mostraras al inicio de tu dispositivo: {x}\n>")
    
    clear()
    control()
    clear()
    
    return "\n".join((
        
        b.habilitar(),
        b.mod_configurarcion(),
        
        #Aqui ya pon los comandos
        b.text_inicial(txt)
        
        #esto se queda si o si
        b.salir(),
        b.guardar_config(),        
        b.comentario(f"Se puso el nombre correctamente al dispositivo"),
        "",
    ))    


    