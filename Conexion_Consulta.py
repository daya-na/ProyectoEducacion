import psycopg2

try:
    conexion = psycopg2.connect(user="usuario",
                                password="clave",
                                database="bd",
                                host="host",
                                port="puerto")
    print("Conexión correcta!")
    
    sql1 = """select name
         from country
         order by 1;"""
    

#Se ejecuta la sentencia para mostrar los nombres de los países
    cursor = conexion.cursor()
    cursor.execute(sql1)
    country = cursor.fetchone()
    print("****PAISES****")
    while country:
        print(country [0])
        country = cursor.fetchone()
    
    
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    conexion.close()
