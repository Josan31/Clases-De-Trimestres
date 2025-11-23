from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def conexion():
    
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='Prueba_Conexión',
            user='postgres',
            password='123456',
            port=5432
        )
        
        print("Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prueba_conexión')
def prueba_conexion():
    return render_template('Prueba_Conexión.html')

@app.route('/usuarios', methods=['POST'])

def guarda():
    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    mensaje = request.form['mensaje']
    
    if not nombre or not apellido or not correo or not telefono or not direccion:
        return "Error: Estos campos son obligatorios."
    
    conexion_db = conexion()
    
    if conexion_db is None:
        return "Error: No se pudo conectar a la base de datos."
    
    try:
        cursor = conexion_db.cursor()
        insert_query = """
            INSERT INTO formulario (nombre, apellido, correo, telefono, direccion, mensaje)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (nombre, apellido, correo, telefono, direccion, mensaje))
        conexion_db.commit()
        cursor.close()
        print("Usuario guardado exitosamente.")
        return redirect('/')
    
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return f"Error al guardar el usuario: {e}"
    
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        try:
            conexion_db.close()
        except Exception:
            pass

if __name__ == '__main__':
    app.run(debug=True)