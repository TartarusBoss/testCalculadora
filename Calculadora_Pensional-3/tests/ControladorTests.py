import sys
sys.path.append("C:/Users/b12s307/testCalculadora/Calculadora_Pensional-3")
import unittest
from src.model.User import Usuario
from src.controller.app_controller import ControladorUsuarios

class ControladorUsuariosTest(unittest.TestCase):

    def setUp(self):
        self.controlador = ControladorUsuarios()

    def test_InsertarUsuarioNormal(self):
        # Insertar un usuario
        usuario_prueba = Usuario(nombre="Pepito", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)

        # Verificar que el usuario se inserta correctamente
        usuarios = self.controlador.ObtenerUsuarios()
        nombres_insertados = [usuario.nombre for usuario in usuarios]
        self.assertIn(usuario_prueba.nombre, nombres_insertados)


    def test_InsertarUsuarioError(self):
    # Intentar insertar un usuario con datos incorrectos o faltantes
        with self.assertRaises(TypeError):
            usuario_prueba = Usuario(nombre="", apellido="Perez", sexo="masculino", edad=30)
            self.controlador.InsertarUsuario(usuario_prueba)


    def testModificarUsuarioNormal(self):
        usuario_prueba = Usuario(nombre="Pepito", apellido="Perez", sexo="masculino", edad=30)
        self.controlador_usuarios.InsertarUsuario(usuario_prueba)
        usuario_modificado = Usuario(nombre="Carlos", apellido="Gomez", sexo="masculino", edad=35)
        self.controlador_usuarios.ModificarUsuario(usuario_prueba.id, usuario_modificado)
        usuario_obtenido = self.controlador_usuarios.ObtenerUsuarioPorID(usuario_prueba.id)
        self.assertEqual(usuario_modificado, usuario_obtenido)

    def testModificarUsuarioInexistente(self):
        usuario_modificado = Usuario(nombre="Carlos", apellido="Gomez", sexo="masculino", edad=35)
        with self.assertRaises(Exception):
            self.controlador_usuarios.ModificarUsuario(99999, usuario_modificado)

    def testEliminarUsuarioNormal(self):
        """Prueba la eliminación normal de un usuario de la base de datos."""
        usuario_prueba = Usuario(nombre="Juan", apellido="Perez", sexo="masculino", edad=30)
        self.controlador_usuarios.InsertarUsuario(usuario_prueba)
        self.controlador_usuarios.EliminarUsuario(usuario_prueba.id)
        usuarios = self.controlador_usuarios.ObtenerUsuarios()
        self.assertNotIn(usuario_prueba, usuarios)

    def testEliminarUsuarioInexistente(self):
        """Prueba que se lance una excepción al intentar eliminar un usuario inexistente."""
        with self.assertRaises(Exception):
            self.controlador_usuarios.EliminarUsuario(99999)

    def testListarUsuariosNormal(self):
        """Prueba que se obtengan los usuarios de manera normal."""
        usuarios = self.controlador_usuarios.ObtenerUsuarios()
        self.assertIsInstance(usuarios, list)

    def testRealizarCalculoNormal(self):
        """Prueba el cálculo normal de una operación."""
        # Supongamos un escenario de cálculo específico y probemos el resultado
        pass

    def testRealizarCalculoError(self):
        """Prueba que se maneje correctamente un error durante el cálculo."""
        # Probemos un escenario donde el cálculo debería fallar y verifiquemos que se maneje adecuadamente
        pass

    def testHistorialNormal(self):
        """Prueba que se obtenga el historial de manera normal."""
        historial = self.controlador_usuarios.ObtenerHistorialCalculos()
        self.assertIsInstance(historial, list)

    def testHistorialError(self):

        pass

if __name__ == '__main__':
    unittest.main()
