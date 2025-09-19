#####DICTIONARIES2####
######################
# Puedes acceder a un valor de un diccionario usando su clave (key):
building_heights = {"Burj Khalifa": 828,"Shanghai Tower": 632,"Abraj Al Bait": 601,"Ping An": 599,"Lotte World Tower": 554.5,"One World Trade": 541.3}
print(building_heights["Burj Khalifa"]) # Muestra 828
print(building_heights["Ping An"])      # Muestra 599
# Otro ejemplo con listas dentro de un diccionario:
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],"fire": ["Aries", "Leo", "Sagittarius"],"earth": ["Taurus", "Virgo", "Capricorn"],"air": ["Gemini", "Libra", "Aquarius"]}
# Muestra la lista de signos de tierra
print(zodiac_elements["earth"])
# Muestra la lista de signos de fuego
print(zodiac_elements["fire"]) 
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
building_heights["Landmark 81"]='no registrado'
# Si intentas acceder a una clave que no existe 
# errror al compilar 
# Para evitar el error, se puede revisar antes si la clave existe:
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])
#se define otro estructura y se define que energia no es un signo zodiacal
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
   print(zodiac_elements["energy"])
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#this line will return 632:
print(building_heights.get("Shanghai Tower"))
#compila none
print(building_heights.get("My House"))
#me muestra que si se quiere obtener la clave de un elemento se usa el condicional para si no esta definido darle valor
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
(user_ids.get("teraCoder"))
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else: 
    tc_id =(user_ids.get("teraCoder"))
    print(tc_id)
#ejemplo cuando no esta definino se agrega clave
    if user_ids.get("superStackSmash") == None:
      stack_id = 100000
print(stack_id)
#.pop() works to delete items from a dictionary, when you know the key value.
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
## Prints "Gift Basket"
print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
# # Prints "No Prize"
print(raffle)
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
# # Prints "Concert Tickets"
print(raffle)
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
#se reitera el eso del pop para eliminar las claves 
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)
#obtener todas las claves con el formato list
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
#ciclo for para imprimer cada elemento independiente
for student in test_scores.keys():
  print(student)
#obtener los elementos mediante sus claves
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#ciclo for para obetener por separado los valores del diccionario
for score_list in test_scores.values():
  print(score_list)
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
#suma de los valores del diccionario con sus claves
for exercises in num_exercises.values():
   total_exercises += exercises
print(total_exercises)
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
#en estos ejemplos se ve el uso de combinacion de obtencion de tanto clave como elemento para encadenadar los eleemento de cada diccionario logicamente
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for occupation, percentage in pct_women_in_occupation.items():
   print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
