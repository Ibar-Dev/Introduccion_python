personas = {"Juan": 30, "María": 25, "Pedro": 35}
edad_juan = personas["Juan"]
personas["Luis"] = 40
for nombre, edad in personas.items():
    print(nombre, edad)
