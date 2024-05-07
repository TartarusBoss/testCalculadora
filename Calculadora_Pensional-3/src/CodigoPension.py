class CalculadoraPensional:

    def calculo_ahorro_pensional(self, edad, salario, semanas_laboradas, rentabilidad_fondo, tasa_administracion):
        aportes_mensuales = salario * 0.12
        ahorro_pensional_esperado = aportes_mensuales * semanas_laboradas * rentabilidad_fondo * (1 - tasa_administracion)

        return ahorro_pensional_esperado
    
    def calculo_pension(self, edad, ahorro_pensional_esperado, sexo, estado_civil, esperanza_vida):
        factor_sexo = 0
        
        if sexo == 'masculino':
            if estado_civil == 'soltero':
                factor_sexo = 0.06
            elif estado_civil == 'casado':
                factor_sexo = 0.08
        elif sexo == 'femenino':
            if estado_civil == 'soltero':
                factor_sexo = 0.07
            elif estado_civil == 'casado':
                factor_sexo = 0.09

        pension_esperada = ahorro_pensional_esperado * (1 + factor_sexo) * (edad / (esperanza_vida - edad)) 

        return pension_esperada
