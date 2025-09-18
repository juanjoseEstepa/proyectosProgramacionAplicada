######DICTIONARIES######
########################
#en este ejemplo se toma la locación de las camaras y sensores en una casa
sensors={"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
#al imprimir las variables se muestra los mismo que hay entre los corchetes con ellos incluidos
print(sensors)
print(num_cameras)
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)
#esta parte del codigo verifica los errores del compilador, por tal razon como este se va a utilizar como clave en phyton existen dos tipos de datos inmutable y mutable como estaba antes era una lista un dato mutable que se  puede cambiar con el tiempo en canbio la tupla es inmutable para mantener la seguridad del diccionario 
powers = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}
print(powers)
#se muestra ahora uno con el ejemplo niños
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)
#se pueden crear diccionarios vacios
my_empty_dictionary = {}
print(my_empty_dictionary)
#en este apartado se crea un menu 
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#se imrpime con un before
print("Before: ", menu)
#se pone menu[] con un elemento que se quiera agregar igualado a un numero  se agrega al final 
menu["cheesecake"] = 8
print("After", menu)
#se pone una sucesion de componentes con un numero que indica la cantidad
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
#se compila solo el ultimo ya que es el que tiene componentes tal cual como esta identado
print(animals_in_zoo)
#se reutiliza la variable sensors 
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)
#se usa el metodo uptade para agragar elementos con sus respectivasd claves 
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)
#se vuelve usar con un variable nueva y claves
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#se muestra aqui que no se puede agregar otra antes de volverla a definir, por otro lado se puede sobreescribir una elemento con una clave distinta 
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)
#no solo se puede renombrar claves numericas si no tambien strings 
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)
#se tienen dos listas que se quieren combinar
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
#la funcion zip permite unilas dos listas pero al hacer print("zipStudents: ", zipStudents) muestra objeto zip un iterador 
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)
#para ver como queda en un diccionario
print(list(zipStudents))
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
#permite jutar  las listas 
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)
#realiza una impresión como no iterador
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
#se hace los mismo pero ya se imprime directamente con el cambio 
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
#se agrega  una camcuion al fianl pero una de eelas como ya esta no se vuelve a agregar
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
#se encadena la impresion y se puede agregar un elemento al final dejando el dinal de la libreria
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)


