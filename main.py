from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)

    print("---- Herencia alumno ----")
    al1 = Alumno("Jose", 19, "23442243", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("---- Herencia profe ----")
    profe1 = Profesor("Jesus", 30+16, 56465, "Ingenieria de Software")
    print(profe1)
    profe1.dormir()

    print("---- Herencia ayudante profe ----")
    ayudante = AyudanteProfesor("Adrian", 20, "2523", "ICO",234234,"Ingenieria de Software",4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abreham"
    ayudante.dar_clase("POO")

main()