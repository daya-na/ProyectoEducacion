import psycopg2

try:
    conexion = psycopg2.connect(user="postgres",
                                password="171096",
                                database="proyecto_educacion",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")

    sql1 = """select *
          from departamento;"""

    sql2 = """select *
          from municipio;"""
    
    sql3 = """select *
          from institucion;"""
    
    sql4 = """select *
          from telefono;"""
          
    sql5 = """select *
          from area_conocimiento;"""

    sql6 = """select *
          from poseer;"""

    sql7 = """select *
          from nucleo_conocimiento;"""     
         
    sql8 = """select *
          from programa_academico;"""   
    
    sql9 = """select *
          from matricula;"""   

#Se ejecuta la sentencia para mostrar los nombres de los departamentos
    cursor = conexion.cursor()
    cursor.execute(sql1)
    departamentos = cursor.fetchall()
    print("****DEPARTAMENTOS****")
    for departamento in departamentos :
        print("Id", departamento[0])
        print("Nombre Departamento", departamento[1], "\n")
    
#Se ejecuta la sentencia para mostrar los nombres de los municipios
    cursor = conexion.cursor()
    cursor.execute(sql2)
    municipios = cursor.fetchall()
    print("****MUNICIPIOS****")
    for municipio in municipios :
        print("Id", municipio[0])
        print("Nombre Municipio", municipio[2], "\n")

#Se ejecuta la sentencia para mostrar los nombres de las instituciones
    cursor = conexion.cursor()
    cursor.execute(sql3)
    instituciones = cursor.fetchall()
    print("****INSTITUCIONES****")
    for institucion in instituciones :
        print("Id", institucion[0])
        print("Nombre Institución", institucion[2])
        print("Sector", institucion[3])
        print("Tipo Institución", institucion[4], "\n")
    
#Se ejecuta la sentencia para mostrar los nombres de los telefonos
    cursor = conexion.cursor()
    cursor.execute(sql4)
    telefonos = cursor.fetchall()
    print("****MUNICIPIOS****")
    for telefono in telefonos :
        print("Telefono", telefono[0], "\n")

#Se ejecuta la sentencia para mostrar los nombres de las areas de conocimiento
    cursor = conexion.cursor()
    cursor.execute(sql5)
    areasConocimiento = cursor.fetchall()
    print("****DEPARTAMENTOS****")
    for areaConocimiento in areasConocimiento :
        print("Id", areaConocimiento[0])
        print("Nombre Area", areaConocimiento[1], "\n") 
    
#Se ejecuta la sentencia para mostrar los nombres de la tabla poseer
    cursor = conexion.cursor()
    cursor.execute(sql6)
    poseer = cursor.fetchall()
    print("****TABLA POSEER****")
    for posee in poseer :
        print("Id Institucion", posee[0])
        print("Id Area", posee[1], "\n")

#Se ejecuta la sentencia para mostrar los nombres de los nucleos de conocimiento
    cursor = conexion.cursor()
    cursor.execute(sql7)
    nbcs = cursor.fetchall()
    print("****NUCLEOS DE CONOCIMIENTO****")
    for nbc in nbcs :
        print("Id", nbc[0])
        print("Nombre NBC", nbc[2], "\n")
    
#Se ejecuta la sentencia para mostrar los nombres de los programas academicos
    cursor = conexion.cursor()
    cursor.execute(sql8)
    programas = cursor.fetchall()
    print("****PROGRAMAS ACADEMICOS****")
    for programa in programas :
        print("Id", programa[0])
        print("Nombre", programa[2])
        print("Nivel Academico", programa[3])
        print("Cant Creditos", programa[4])
        print("Metodologia", programa[5])
        print("Periodicidad", programa[6])
        print("Cant periodos", programa[7], "\n")

#Se ejecuta la sentencia para mostrar las matriculas
    cursor = conexion.cursor()
    cursor.execute(sql9)
    matriculas = cursor.fetchall()
    print("****MATRICULAS****")
    for matricula in matriculas :
        print("Semestre", matricula[0])
        print("Año", matricula[2])
        print("Cant Matriculados", matricula[3], "\n")

except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    conexion.close()
