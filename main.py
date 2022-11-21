import hospital_clases
import random


class MetodosCreate:
    num_hos = 0
    num_doctor = 0
    num_enfer = 0

    def __init__(self, hospital_clas):
        self.hs = hospital_clas

    # CREA 2 DOCTORES
    def crear_doctores(self):
        doctores = []
        for num_doc in range(2):
            print("vuelta ", num_doc)
            self.num_doctor += 1
            nombre_d = "DOC" + str(self.num_doctor)
            apellido_d = nombre_d + " " + nombre_d
            dni_d = str(self.num_doctor) + "dni"
            especialidades_list = ["Alergología", "Anestesiología y reanimación", "Aparato digestivo", "Cardiología"]
            especialidad = random.choice(especialidades_list)
            print(especialidad)
            doctores = hs.Doctor(nombre_d, apellido_d, dni_d, especialidad)
        return doctores

    # CREA 2 ENFERMEROS
    def crear_enfermero(self):
        list_enfermeros = []
        for num_enf in range(2):
            print("vuelta ", num_enf)
            self.num_enfer += 1
            nombre_e = "Enf" + str(self.num_enfer)
            apellido_e = nombre_e + " " + nombre_e
            dni_e = str(self.num_enfer) + "dnienfermero"

            plantas_list = [1, 2, 3, 4, 5]
            planta = random.choice(plantas_list)
            print("trabaja en la planta", planta)
            list_enfermeros = self.hs.Enfermeros(nombre_e, apellido_e, dni_e, planta, False)
        return list_enfermeros

    # CREA Hospital
    def crear_hospital(self):
        doctores = self.crear_doctores()
        enfermeros = self.crear_enfermero()
        self.num_hos += 1
        nombre_h = "h" + str(self.num_hos)
        ubicacion_h = "u" + str(self.num_hos)
        hospital = hs.Hospital(nombre_h, ubicacion_h, doctores, enfermeros, enfermos=[])
        return hospital

    # IMPRIME LO QUE HAY EN LAS SALAS DE ESPERA
    def motrar_sala_espera(self, sala):
        print("EN LA SALA DE ESPERA HAY:")
        for p in sala:
            print("\t- ", p.nombre)


sala_de_espera = []
hs = hospital_clases

mCreate = MetodosCreate(hs)
# Crear 4 Pacientes y meterlos en la sala de espera

p1 = hs.Paciente("Jose", "Jose Jose", "1111A", "", False)
p2 = hs.Paciente("Maria", "Maria Maria", "2222B", "", False)
p3 = hs.Paciente("Pepa", "Pepa Pepa", "3333C", "", False)
p4 = hs.Paciente("Antonio", "Antonio Antonio", "4444D", "", False)

sala_de_espera = [p1, p2, p3, p4]
mCreate.motrar_sala_espera(sala_de_espera)

# Creamos hospital y sus trabajadores
hopital1 = mCreate.crear_hospital()