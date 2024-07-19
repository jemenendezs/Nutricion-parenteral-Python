# Nutricion-parenteral
Este código realiza cálculos para determinar los volúmenes y las velocidades de infusión necesarias para una nutrición parenteral basada en los requerimientos calóricos y de proteínas de un paciente. Calcula y muestra cómo se deben preparar y administrar soluciones de dextrosa, lípidos y aminoácidos para satisfacer las necesidades nutricionales diarias de un paciente basado en su peso y requerimientos específicos. Aquí está una descripción detallada de lo que hace:

1. **Importación y Definiciones Iniciales**:
   - **Definición de la Función `calcular_nutricion_parenteral`**: La función toma tres parámetros:
     - `peso`: Peso del paciente en kilogramos.
     - `requerimiento_calorico`: Requerimiento calórico diario en kcal/kg/día.
     - `requerimiento_proteinas`: Requerimiento de proteínas diario en g/kg/día.

2. **Cálculo de Requerimientos Totales**:
   - Calcula el requerimiento calórico total y el requerimiento de proteínas total para el paciente multiplicando el peso por los requerimientos diarios.

3. **Cálculo de Componentes**:
   - **Dextrosa al 50%**:
     - Se calcula el volumen necesario para suministrar el 50% del requerimiento calórico total.
     - Se determina la velocidad de infusión dividiendo el volumen por 24 horas.
   - **Lípidos al 20%**:
     - Se calcula el volumen necesario para suministrar el 30% del requerimiento calórico total.
     - Se determina la velocidad de infusión dividiendo el volumen por 24 horas.
   - **Aminoácidos al 15%**:
     - Se calcula el volumen necesario para suministrar el requerimiento de proteínas total convertido a calorías.
     - Se determina la velocidad de infusión dividiendo el volumen por 24 horas.

4. **Resultados**:
   - Imprime los detalles de la nutrición parenteral, incluyendo el volumen y la velocidad de infusión para cada componente (dextrosa, lípidos y aminoácidos).
   - Muestra el volumen total requerido para la infusión.

5. **Entradas del Usuario**:
   - **Peso del Paciente**: Se solicita al usuario ingresar el peso del paciente, asegurándose de que sea un valor positivo.
   - **Requerimiento Calórico**: Se solicita al usuario ingresar el requerimiento calórico diario, validando que esté dentro del rango permitido (25-30 kcal/kg/día).
   - **Requerimiento de Proteínas**: Se solicita al usuario ingresar el requerimiento de proteínas diario, validando que esté dentro del rango permitido (0.8-1.2 g/kg/día).

6. **Ejemplo de Uso**:
   - Después de recibir y validar las entradas del usuario, llama a la función `calcular_nutricion_parenteral` con los datos proporcionados para calcular y mostrar la nutrición parenteral adecuada.
