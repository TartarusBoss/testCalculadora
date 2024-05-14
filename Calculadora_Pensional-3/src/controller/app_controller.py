import sys
sys.path.append(".")
import psycopg2
from src.model.User import Usuario
import secret_config

class ControladorUsuarios:
    def crear_tablas(self):
        with self.ObtenerCursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                              id SERIAL PRIMARY KEY,
                              nombre TEXT NOT NULL,
                              apellido TEXT NOT NULL,
                              sexo TEXT NOT NULL,                              
                              edad INTEGER NOT NULL
                            );""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS resultados_calculos (
                              id SERIAL PRIMARY KEY,
                              id_usuario INTEGER REFERENCES usuarios(id),
                              nombre_usuario TEXT NOT NULL,
                              tipo_calculo TEXT NOT NULL,
                              resultado NUMERIC NOT NULL,
                              fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            );""")
            cursor.connection.commit()

    def ObtenerCursor(self):
        connection = psycopg2.connect(database=secret_config.PGDATABASE, 
                                      user=secret_config.PGUSER, 
                                      password=secret_config.PGPASSWORD, 
                                      host=secret_config.PGHOST, 
                                      port=secret_config.PGPORT)
        return connection.cursor()
    
    def InsertarUsuario(self, usuario):
        with self.ObtenerCursor() as cursor:
            cursor.execute("""INSERT INTO usuarios (nombre, apellido, sexo, edad)
                              VALUES (%s, %s, %s, %s)""", (usuario.nombre, usuario.apellido, usuario.sexo, usuario.edad))
            cursor.connection.commit()

    def InsertarResultadoCalculo(self, id_usuario, tipo_calculo, resultado):
        # Obtener el nombre del usuario
        usuario = self.ObtenerUsuarioPorID(id_usuario)
        nombre_usuario = f"{usuario.nombre} {usuario.apellido}"

        # Insertar el resultado del cálculo en la base de datos
        with self.ObtenerCursor() as cursor:
            cursor.execute("""INSERT INTO resultados_calculos (id_usuario, nombre_usuario, tipo_calculo, resultado)
                            VALUES (%s, %s, %s, %s)""", (id_usuario, nombre_usuario, tipo_calculo, resultado))
            cursor.connection.commit()

    def ObtenerUsuarios(self):
        with self.ObtenerCursor() as cursor:
            cursor.execute("SELECT * FROM usuarios")
            usuarios = []
            for row in cursor.fetchall():
                usuario = Usuario(row[1], row[2], row[3], row[4])
                usuario.id = row[0]
                usuarios.append(usuario)
            return usuarios           

    def ObtenerHistorialCalculos(self):
        with self.ObtenerCursor() as cursor:
            cursor.execute("SELECT * FROM resultados_calculos")
            historial = []
            for row in cursor.fetchall():
                historial.append(row)
            return historial

    
    def ObtenerUsuarioPorID(self, id_usuario):
        with self.ObtenerCursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
            row = cursor.fetchone()
            if row:
                usuario = Usuario(row[1], row[2], row[3], row[4])
                usuario.id = row[0]
                return usuario
            else:
                raise ValueError("El usuario con el ID especificado no existe.")


    def ModificarUsuario(self, id_usuario, nombre, apellido, sexo, edad):
        with self.ObtenerCursor() as cursor:
            cursor.execute("""UPDATE usuarios
                            SET nombre = %s, apellido = %s, sexo = %s, edad = %s
                            WHERE id = %s""", (nombre, apellido, sexo, edad, id_usuario))
            cursor.connection.commit()


    def EliminarUsuario(self, id_usuario):
        with self.ObtenerCursor() as cursor:
            cursor.execute("""DELETE FROM resultados_calculos WHERE id_usuario = %s""", (id_usuario,))
            cursor.execute("""DELETE FROM usuarios WHERE id = %s""", (id_usuario,))
            cursor.connection.commit()

    def ObtenerResultadosCalculo(self, id_usuario):
        with self.ObtenerCursor() as cursor:
            cursor.execute("""SELECT tipo_calculo, resultado, mensaje_error, fecha
                              FROM resultados_calculos
                              WHERE id_usuario = %s""", (id_usuario,))
            return cursor.fetchall()


controlador_usuarios = ControladorUsuarios()
controlador_usuarios.crear_tablas()
