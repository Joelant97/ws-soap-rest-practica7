import unirest #librerias
import json


#Listar Todos los Estudiantes: 

listEstudiantes= unirest.get("http://localhost:4567/wsRest/estudiantes/", headers={ "Accept": "application/json" })

print "Estudiantes: \n" + str(listEstudiantes.body)

#Consultar Estudiante: 

estudiante= unirest.get("http://localhost:4567/wsRest/estudiantes/" + str(20121776), headers={ "Accept": "application/json" })
print "Consulta correcta: " + str(estudiante.body)

#Crear un nuevo Estudiante: 
crearEstudiantes= unirest.post("http://localhost:4567/wsRest/estudiantes/", headers={ "Accept": "application/json"}, params=json.dumps({ "nombre": "Joel", "carrera": "isc", "correo": "joelant@gmail.com"}))

print "Se creo el nuevo estudiante: " + str(crearEstudiantes.body)