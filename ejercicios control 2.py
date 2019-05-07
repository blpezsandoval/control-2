lista=[]
asignatura=[]
fecha_nota=[]
notas=[]
opcion=0
while opcion != 4 :
    print("BLOCK DE NOTAS")
    print("--------------")
    print("1.Subir una nota:")
    print("2.visualizar nota:")
    print("3.buscar nota:")
    opcion=int(input("ingrese una opcion:"))
    if opcion == 1:
        n=int(input("ingresar el numero de notas que entrara:"))
        for i in range(n):
            print("ingrese nota")
            nota=input()
            notas.append(nota)
    elif opcion == 2:
        print(notas)
