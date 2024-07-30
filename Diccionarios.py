persona = {
    "nombre": "Felipe",
    "edad": 25,
    "Pais": "Australia"
}
print(persona)
print(len(persona))
print(type(persona))
nombre = persona["nombre"]
print(nombre)

persona["edad"] = 32
persona.update({"Pais": "Rusia"})
persona.update({"id": 27, "nombre": "Juan"})
print(persona)