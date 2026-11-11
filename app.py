def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = total / cantidad
    return promedio

if __name__ == "__main__":
    notas = [14, 16, 15, 18, 13]
    resultado = calcular_promedio(notas)
    
    print("Sistema de Evaluacion de Calidad Academica")
    print("Notas registradas:", notas)
    print("El promedio final es:", resultado)
    
    if resultado >= 13:
        print("Estado: Aprobado con calidad estandar.")
    else:
        print("Estado: Requiere revision de codigo.")