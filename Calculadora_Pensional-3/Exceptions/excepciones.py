class ExcepcionesPersonalizadas:   
    
    def validaciones_tipo_ahorro_pensional(self, edad, salario, semanas_laboradas, rentabilidad_fondo, tasa_administracion):

        if not isinstance(salario, (int, float)):
            raise TypeError("El salario debe ser numérico. ")

        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un entero. ")

        if not isinstance(semanas_laboradas, (int, float)):
            raise TypeError("Las semanas laboradas deben ser numéricas. ")

        if not isinstance(tasa_administracion, (int, float)):
            raise TypeError("La tasa de administración debe ser numérica. ")

        if rentabilidad_fondo < 0 or rentabilidad_fondo > 1:
            raise ValueError("La rentabilidad de fondo debe estar entre 0 y 1. ")

        if semanas_laboradas < 0:
            raise ValueError("Las semanas laboradas tienen que ser positivas. ")

        if edad <= 0:
            raise ValueError("La edad ingresada es negativa, ingrese una edad válida. ")

        if salario <= 0:
            raise ValueError("El salario debe ser mayor a 0. ")

        return 
    
    
    def validaciones_tipo_calculo_pension(self, edad, ahorro_pensional_esperado, sexo, estado_civil, esperanza_vida):

        if not isinstance(sexo, str):
            raise TypeError("El sexo debe ser un string, no un número. Debe ser 'masculino' o 'femenino'. ")

        if not isinstance(estado_civil, str):
            raise TypeError("El estado civil debe ser 'soltero' o 'casado', tu ingresaste un número. ")

        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un entero, ingresa una edad válida. ")

        if sexo not in ['masculino', 'femenino']:
            raise TypeError ("El sexo debe ser 'masculino' o 'femenino'. ")

        if estado_civil not in ['casado', 'soltero']:
            raise TypeError ("El estado civil debe ser 'casado' o 'soltero'. ")

        if not isinstance(esperanza_vida, (int, float)):
            raise TypeError ("La esperanza de vida debe ser numérica. ")

        if not isinstance(ahorro_pensional_esperado, (int, float)):
            raise TypeError("El ahorro pensional esperado debe ser int o float. ")

        if edad < 0:
            raise ValueError("La edad no puede ser negativa, ingrese una edad válida. ")

        if edad > 90:
            raise ValueError("La edad debe estar entre 1-90, ingrese una edad válida. ")

        if edad > esperanza_vida:
            raise ValueError("La edad no puede ser mayor a la esperanza de vida. ")

        if esperanza_vida < 0:
            raise ValueError("La esperanza de vida debe ser mayor a 0. ")

        return 