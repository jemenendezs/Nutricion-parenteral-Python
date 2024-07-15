# Autor: Jorge Menéndez S.
# Licencia: MIT License
#
# Copyright (c) 2024 Jorge Menéndez S.
#
# Por la presente se concede permiso, sin cargo, a cualquier persona que obtenga una copia
# de este software y los archivos de documentación asociados (el "Software"), para tratar
# en el Software sin restricciones, incluyendo sin limitación los derechos
# para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y para permitir a las personas a quienes se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas
# las copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
# INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O
# LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD,
# YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE,
# FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
# SOFTWARE.

def calcular_nutricion_parenteral(peso, requerimiento_calorico, requerimiento_proteinas):
    # Calcular requerimientos totales
    requerimiento_calorico_total = requerimiento_calorico * peso  # kcal
    requerimiento_proteinas_total = requerimiento_proteinas * peso  # g

    # Volumen y velocidad de infusión para cada componente
    volumen_total = 0
    velocidad_dextrosa = 0
    velocidad_lipidos = 0
    velocidad_aminoacidos = 0

    # Calcular para dextrosa al 50% (4 kcal/g y 0.5 g/mL)
    cal_dextrosa = 4  # kcal/g
    concentracion_dextrosa = 0.5  # g/mL
    requerimiento_calorico_dextrosa = requerimiento_calorico_total * 0.5  # 50% del requerimiento calórico total
    volumen_dextrosa = requerimiento_calorico_dextrosa / (cal_dextrosa * concentracion_dextrosa)  # mL
    velocidad_dextrosa = volumen_dextrosa / 24  # mL/h (suponiendo 24 horas de infusión)
    volumen_total += volumen_dextrosa

    # Calcular para lípidos al 20% (9 kcal/g y 0.2 g/mL)
    cal_lipidos = 9  # kcal/g
    concentracion_lipidos = 0.2  # g/mL
    requerimiento_calorico_lipidos = requerimiento_calorico_total * 0.3  # 30% del requerimiento calórico total
    volumen_lipidos = requerimiento_calorico_lipidos / (cal_lipidos * concentracion_lipidos)  # mL
    velocidad_lipidos = volumen_lipidos / 24  # mL/h (suponiendo 24 horas de infusión)
    volumen_total += volumen_lipidos

    # Calcular para aminoácidos al 15% (4 kcal/g y 0.15 g/mL)
    g_aminoacidos = 0.15  # g/mL
    cal_aminoacidos = 4  # kcal/g
    requerimiento_calorico_aminoacidos = requerimiento_proteinas_total * cal_aminoacidos  # kcal
    volumen_aminoacidos = requerimiento_proteinas_total / g_aminoacidos  # mL
    velocidad_aminoacidos = volumen_aminoacidos / 24  # mL/h (suponiendo 24 horas de infusión)
    volumen_total += volumen_aminoacidos

    # Mostrar resultados individuales
    print("Detalles de la nutrición parenteral:")
    print(f"----------------------------------")
    print(f"* Dextrosa al 50%: Volumen: {volumen_dextrosa:.2f} mL, Velocidad de infusión: {velocidad_dextrosa:.2f} mL/h")
    print(f"* Lípidos al 20%: Volumen: {volumen_lipidos:.2f} mL, Velocidad de infusión: {velocidad_lipidos:.2f} mL/h")
    print(f"* Aminoácidos al 15%: Volumen: {volumen_aminoacidos:.2f} mL, Velocidad de infusión: {velocidad_aminoacidos:.2f} mL/h")
    print(f"----------------------------------")
    print(f"Volumen total requerido: {volumen_total:.2f} mL")

# Ejemplo de uso
while True:
    try:
        peso_paciente = float(input("Ingrese el peso del paciente en kg: "))
        if peso_paciente <= 0:
            raise ValueError("El peso del paciente debe ser mayor que cero.")
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        requerimiento_calorico = float(input("Ingrese el requerimiento calórico diario en kcal/kg/día (debe estar entre 25 y 30 kcal/kg/día): "))
        if requerimiento_calorico < 25 or requerimiento_calorico > 30:
            raise ValueError("El requerimiento calórico debe estar entre 25 y 30 kcal/kg/día.")
        break
    except ValueError as e:
        print(f"Error: {e}")

while True:
    try:
        requerimiento_proteinas = float(input("Ingrese el requerimiento de proteínas diario en g/kg/día (debe estar entre 0.8 y 1.2 g/kg/día): "))
        if requerimiento_proteinas < 0.8 or requerimiento_proteinas > 1.2:
            raise ValueError("El requerimiento de proteínas debe estar entre 0.8 y 1.2 g/kg/día.")
        break
    except ValueError as e:
        print(f"Error: {e}")

calcular_nutricion_parenteral(peso_paciente, requerimiento_calorico, requerimiento_proteinas)
