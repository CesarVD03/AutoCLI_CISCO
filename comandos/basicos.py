
#habilitar el router
def habilitar ():
    return "enable"
    
#configurarcion
def mod_configurarcion():
    return "configure terminal"
    
#salir
def salir():
    return "exit"

#linea de consola
def mod_linea_de_consola():
    return "line console 0"

#cambiar nombre del dispositivo
def cambiar_nombre(nombre):
    return f"hostname {nombre}"

#texto inicial
def text_inicial(txt):
    return f"banner motd #{txt}#"

#guardar la configuarcion
def guardar_config():
    return "write memory"

#comentario
def comentario(coment):
    return f"!{coment}"