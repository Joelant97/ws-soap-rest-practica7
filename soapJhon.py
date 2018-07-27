#libreria de SOAP en Python
from zeep import Client

url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)

#Listar todos los Estudiantes: 
listEstudiantes = client.service.getAllEstudiante()
print "Estudiantes: \n\n\n" + str(listEstudiantes)

#Consultar una Asignatura:
asignatura = client.service.getAsignatura(415)

print "Asignatura fue Consultada: \n\n" + str(asignatura)

#Consultar un Profesor: 
profesor= client.service.getProfesor("123123")
print "Profesor fue Consultado: \n\n" + str(profesor) 