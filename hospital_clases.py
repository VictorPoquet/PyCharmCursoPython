# Clase persona
class Persona:
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        print("Se ha creado el usuario : ", nombre)


# Clase Paciente con herencia de persona
class Paciente(Persona):
    diagnostico = ""
    atendido = False

    def __init__(self, nombre, apellidos, dni, diagnostico, atendido):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.diagnostico = diagnostico
        self.atendido = atendido
        print("Se ha creado el usuario : ", nombre)


# Clase Doctor con herencia de persona
class Doctor(Persona):
    especialidad = ""

    def __init__(self, nombre, apellidos, dni, especialidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.especialidad = especialidad
        print("Se ha creado el usuario : ", nombre)

    def fichar(dia, hora_entrada, hora_salida):
        print("El dia ", dia, "ha entrado ", hora_entrada, " y ha salido ", hora_salida)


# Clase Enfermeros con herencia de persona
class Enfermeros(Persona):
    planta = ""
    atendiendo = False

    def __init__(self, nombre, apellidos, dni, planta, atendiendo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.planta = planta
        self.atendiendo = atendiendo
        print("Se ha creado el usuario : ", nombre)

    def fichar(dia, hora_entrada, hora_salida):
        print("El dia ", dia, "ha entrado ", hora_entrada, " y ha salido ", hora_salida)


# Clase Enfermos con herencia de persona
class Enfermo:
    def __init__(self, paciente, enfermedad):
        self.Paciente = paciente
        self.enfermedad = enfermedad
        print("al paciente : ", paciente.nombre, " se le ha diacnositicado la enfermedad ", enfermedad)


# Clase Hospital con herencia de persona
class Hospital:
    def __init__(self, nombre, ubicacion, doctores=[], enfermeros=[], enfermos=[]):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.doctores = doctores
        self.enfermos = enfermos
        self.enfermeros = enfermeros
        print("Se ha creado el hostpial : ", nombre)
