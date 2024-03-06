##necesitamos a sqlalchemy 
#Definir los atributos de objeto 
#pero con tipos raducible a sql y mysql en especifico 
from app import db 
from datetime import datetime 

class Medico(db.Model):
    
    __tablename__="medicos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellido = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True) 
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.Integer)
    especialidad = db.Column(db.String(50))
    
    citas = db.relationship("Cita" , backref = 'medico' )
    
    
class Paciente(db.Model):
    
    __tablename__= "pacientes"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellido = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True) 
    altura = db.Column(db.Integer)
    tipo_sangre = db.Column(db.String(2))
    
    citas = db.relationship("Cita" , backref = 'paciente' )
    
    
class Consultorio(db.Model):
        
    __tablename__= "consultorios"
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    
    citas = db.relationship("Cita" , backref = 'consultorio' )
    
class Cita(db.Model):
    
    __tablename__= "citas"     
    id = db.Column(db.Integer, primary_key = True) 
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"))
    medico_id = db.Column(db.Integer, db.ForeignKey("medicos.id"))
    consultorio_id = db.Column(db.Integer, db.ForeignKey("consultorios.id")) 
    valor  = db.Column (db.Integer)
    
    
    
    ## from app.models import Medico,Paciente,Cita,Consultorio 

## me2=Medico(nombre="Juliana", apellido="Osorio",tipo_identificacion="CC",numero_identificacion=9876543,especialidad="odontologia") 
## me1=Medico(nombre="Sofia", apellido="Gomez",tipo_identificacion="CC",numero_identificacion=87654,especialidad="Pediatra")
## me3=Medico(nombre="Pedro", apellido="Ortiz",tipo_identificacion="CC",numero_identificacion=2345643,especialidad="pediatra") 
## p1=Paciente(nombre="Milena",apellido="Arias",tipo_identificacion="TI",altura=160,tipo_sangre="A+")
## p2=Paciente(nombre="Julio",apellido="Rodriguez",tipo_identificacion="TI",altura=170,tipo_sangre="O+")  
## p3=Paciente(nombre="Nelson",apellido="Romero",tipo_identificacion="CC",altura=180,tipo_sangre="O+")   
## c1=Consultorio(numero=301)
## c2=Consultorio(numero=302) 
## c3=Consultorio(numero=303) 
##for ci in Cita.query.all():                                                                                                              
##     print("fecha:"+ str(c1.fecha)+"paciente identificacion:"+ str(ci.paciente.tipo_identificacion)+",paciente nombre:"+(ci.paciente.nombre)+"paciente apellido:"+( ci.paciente.apellido) + "registro medico:"+str(ci.medico.registro_medico) + "consultorio:" + str(ci.consultorio.numero) + "valor cita:"+str(ci.valor)) 