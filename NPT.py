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