
libros =  {
    "1" : ["Titulo: Cien Años de Soledad","Genero:Novela", "Autor: Gabriel Garcia Marquez", "Don Quijote de la Mancha" ,"Titulo: Don Quijote de la Mancha","Genero:Aburrido", "Autor: Miguel de Cervantes", "Hamlet" , "Titulo: Hamlet","Genero:Teatro", "Autor: william Shakespeare", "El Principito" ,"Titulo: El Principito","Genero:Fantasia", "Autor: Antonie de Saint Exupery", "Orgullo y Prejuicio" , "Titulo: Orgullo y Prejuicio","Genero:Romantico", "Autor: Jane Austen", "1984" , "Titulo: 1984","Genero:Misterio", "Autor: George Orwell", "La Odisea " , "Titulo: La Odisea","Genero:Poesia", "Autor: Homero", "El Retrato de Dorian Grey" , "Titulo: El Retrato de Dorian Grey","Genero:Fantasia", "Autor: Oscar Wilde", "Lo que el Viento se LLevo" , "Titulo: Lo que el Viento se LLevo","Genero:Drama", "Autor: Margaret Mitchell", "Moby-Dick" , "Titulo: Hamlet","Genero:Fanatsia", "Autor: Herman Melville"]
     }

Personas =  {
         "Personas" : ["Nombres","Daniel Fernando Ballestero Umaña", "Milton Eliseo Lobo Nuñez", "Emilce Liseth Vargas Campos", "Roberto Elias Molina Rosales", "Carlos Mauel Zapata Cerdas", "Jose Alvares Cabalceta", "Cinthya Corrales Alvardo", "Gladys Jimenez solano", "Seidy Lopez Medina", "Alexis Vargas  Calderon", "Hector Segura Prado", "Miguel Angel Fuentes  Fuentes", "Herminia Maria Baldivia Hernandez", "Manuel Villa Vargas","Maria Matamoros Landazuri","Janina Ruth Castillo Pasos", "Jorge Flores Nuñez", "Jhovan Perez Navarrete", "Erika Reyes Aleman","Emidey Arias Hernandez","Nubia Marchena Viales", "Jessica Perlina Bent Morales", "Karla  Vanessa Mora Sanchez", "Flor de Maria Corella Monge", "Yessenia Ruiz Contreras", "Jennifer Guitierrez Vargas", "Juan Carlos Valverde Rivera", "Andrea Mejias Gomez", "Luis Alejandro Aponte Quiros", "Andrea Castillo Villalobos" ]
    
     }

def prestar():
    u=input("Ingrese libro: ")
    if u in libros:
        print("El libro ya se encuentra dentro de la biblioteca.")
    else:
        Genero="Genero: "+input("Ingrese genero: ")
        Autor="Autor: "+input("Ingrese autor: ")
    print("Titulo: "+ u + "Genero: "+ Genero +  "Autor: "+ Autor)
    libros[u]=[u, Genero,Autor]


def ver_lista():
    Personas=input("Ingrese el nombre de la persona: ")
    print(Personas)


def consultar():
      s=input("Ingrese libro: ")
      existe = 0 
      for libro in libros:
          if s == libro:
              existe = 1

      if (existe == 1):
            print("Tenemos ese libro en la Biblioteca.")
            print(libros[s])
      else:
            print("No tenemos ese libro en la Biblioteca.")
    
    
def modificar():
    m=input("Ingrese libro a modificar: ")
    print("Que desea modificar?")
    print("1.Genero")
    print("2.paginas")
    print("3.Autor")
    
    
    s=int(input("Elegir operacion: "))
    if(s==1):
        libros[m][1]="Genero: "+input("Genero:")
    elif(s==3):
        libros[m][3]="Autor"+input("Autor: ")
    
    
def listados():
        print("Operaciones de listados.") 
        print("1.Listar todos los autores existentes.") 
        print("2.Listar todos los libros existentes.") 
        print("3.Listar todos los libros de un genero determinado.")  
        print("4.Listar todos los libros que posee un autor determinado.") 
        p=int(input("Elegir operacion a realizar: "))
        if(p==1):
            for titulos in libros:
                print(libros[titulos][3])
        if(p==2):
            for titulos in libros:
                print(libros[titulos][0])
        elif(p==3):
            for titulos in libros:
                print(libros[titulos][1])
        elif(p==4):
            s="Autor: "+input("Autor: ")
            for titulos in libros:
                if(s == libros[titulos][3]):
                    print(libros[titulos][3])
        elif(p==5):
            for titulos in libros:
                print(libros[titulos][6])

a=1


while(a!=0):
    print("Operaciones")
    print("1.Prestar un libro.") 
    print("2.Ver lista.") 
    print("3.Consultar por un libro determinado.") 
    print("4.Modificar datos de un libro.") 
    print("5.Listados:") 
    print("6.Salir.")
    b=int(input("Elejir operacion a realizar: "))
    if(b==1):
        prestar()
        print("Desea seguir operando?")
        print("1.Si")
        print("2.No")
        s=int(input("Elegir operacion a realizar: "))
        if(s==1):
            a=1
        else:
            a=0
    elif(b==2):
        ver_lista()
        print("Desea seguir operando?")
        print("1.Si")
        print("2.No")
        s=int(input("Elegir operacion a realizar: "))
        if(s==1):
            a=1
        else:
            a=0
    elif(b==3):
        consultar()
        print("Desea seguir operando?")
        print("1.Si")
        print("2.No")
        s=int(input("Elegir operacion a realizar: "))
        if(s==1):
            a=1
        else:
            a=0
    elif(b==4):
        modificar()
        print("Desea seguir operando?")
        print("1.Si")
        print("2.No")
        s=int(input("Elegir operacion a realizar: "))
        if(s==1):
            a=1
        else:
            a=0
    elif(b==5):
        listados()
        print("Desea seguir operando?")
        print("1.Si")
        print("2.No")
        s=int(input("Elegir operacion a realizar: "))
        if(s==1):
            a=1
        else:
            a=0
    elif(b==6):
        a=0