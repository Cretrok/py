import re


def validarUser(nameUser):
    numC = len(nameUser)
    if numC < 6:
        print("El nombre de usuario debe de contener al menos 6 caracteres")
        return False
    elif numC > 12:
        print("El nombre de usuario no puede contener mas de 12 caracteres")
        return False
    elif nameUser.isalnum() == True:
        return True


def validarPass(passUser):
    if not re.match("[\S]{8,}",passUser):
        print("La contrasea debe de tener al menos 8 caracteres")
        return False
    if not re.search("[A-Z]{1,}",passUser):
        print("Debe de tener al menos una mayuscula")
        return False
    if not re.search("[0-9]{1,}",passUser):
        print("Debe de tener al menos un numero")
        return False
    if not re.search("[#$%&*]{1,}",passUser):
        print("Debe de contenr al menos un caracter especial \"#\" \"$\" \"%\" \"&\" \"*\"")
        return False

    return True