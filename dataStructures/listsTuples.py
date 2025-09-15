######LISTAS######
##################

#crear una lista en un arreglo en este caso de 5 colores
my_list=['Azul','Verde','Amarillo','Naranja','Morado']
#remplaza imput permite ver el contenido de la lista
print(my_list)
#muestra el tipo de objeto de my_list siendo un list
print(type(my_list))
#imprime la poscion numero 2 de la lista
print(my_list[2])
#uso de  len para medir el tamaño de la lista
print('my list size:',len(my_list))
#muestra la poscion 0 y 2
print(my_list[0:2])
#se puede ovear el 0 al no poner nada
print(my_list[:2])
#Extencion append para agregar elemento a la lista en la ultima poscion
my_list.append('Negro')
print(my_list)
#insert para agregar un elemento en una poscion especifica
my_list.insert(3, 'Blanco')
print(my_list)
#extend permite concatenar otra lista
my_list.extend(['Marron', 'Magenta'])   
print(my_list)
#index permite mostrar la posicion numerica de un valor de la lista
print(my_list.index('Azul'))
#remove quita el elemento nombrado
my_list.remove('Morado')
#pop imprime el ultimo elemento de la lista y recordar size por los cambio realizados 
print(my_list)
print(my_list.pop())
size = len(my_list)
print("size = ", size)
#el * permite multiplicar los elementos en este caso 3 veces
my_lista_3 = my_list*3
print("my_lista_3: ", my_lista_3)
#sort permite organizar la lista automaticamente pero solo con numeros 
#para strings es neceseraio dar parametros
print("Sort:")
print()
my_listaSort = my_list.sort()
print(my_listaSort)
#buen uso del sort en lita numerica de menor a mayor
my_NumList = [2, 1, 4, 3, 6 , 7 , 5, 10, 8, 9]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
#condicion re reverse como parametro para que sea de meyor a menor
my_NumList.sort(reverse = True)
print("De mayor a menor: ", my_NumList)

######TUPLAS######
##################
#las tuplas permiten organizar alfabeticamente la lista 
my_tupla = tuple(my_list)
print()#espacios
print()
print("my_tuple: ", my_tupla)
#en cambio en numeros es de mayor a menor
my_Numtupla = tuple(my_NumList)
print("my_tuple: ", my_Numtupla)
#imprime elemento en la poscion de la tupla pero adiferencia de las litas lo hace con espacio y el elemento que esta dentro de las comillas
print(my_tupla[0])
print(my_tupla[2])
#el metodo count permite verificar si hay un elemento dentro para esto usa el tipo de dato boleano 
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))
#se puede definir una tupla de un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)
#se puede conformar una tupla sin parentesis ni comilas se ponen en la impresion los parentisis y hasta deja las comillas 
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)
#se puede organizar la tupla juntando los elemntos con atributos para darle orden en la impresion
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)
#Se peude convertir un tupla en una lista y viseversa 
my_lista2=list(my_tupla)
print(my_lista2)




