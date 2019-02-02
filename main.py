import validar

resName = False
resPass = False

while resName == False:
    name = str(input("Escriba un nombre de usuario: "))
    resName = validar.validarUser(name)

while resPass == False:
    passUsr = str(input("Escriba una contraseña: "))
    resPass = validar.validarPass(passUsr)
