import validar

resName = False
resPass = False

while resName == False:
    name = raw_input("Escriba un nombre de usuario: ")
    resName = validaciones.validarUser(name)

while resPass == False:
    passUsr = raw_input("Escriba una contraseña: ")
    resPass = validaciones.validarPass(passUsr)
