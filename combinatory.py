import random
import csv

tipos = ['deportivo', 'formal', 'casual']
ocasiones = ['fiesta', 'diario', 'caminar']
colores = ['negro', 'azul', 'blanco', 'dorado', 'turquesa', 'amarillo', 'lavanda', 'rosado', 'gris', 'violeta']
tallas = list(range(24, 30))
suelas = ['goma', 'cuero', 'curva', 'plana', 'tacón']
marcas = ['Nike', 'Prada', 'Adidas']
temporadas = ['Primavera', 'Verano', 'Otoño', 'Invierno']

num_combinaciones = len(tipos) * len(ocasiones) * len(colores) * len(tallas) * len(suelas) * len(marcas) * len(temporadas)

nombres_unicos = random.sample(range(100000, 999999), num_combinaciones)

nombre_archivo = 'combinaciones_con_nombres.csv'

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    writer.writerow(['NombreUnico','Tipo', 'Ocasión', 'Color', 'Talla', 'Suela', 'Marca', 'Temporadas'])
    
    for tipo in tipos:
        for ocasion in ocasiones:
            for color in colores:
                for talla in tallas:
                    for suela in suelas:
                        for marca in marcas:
                            for temporada in temporadas:
                                nombre_unico = nombres_unicos.pop(0)
                                writer.writerow([nombre_unico, tipo, ocasion, color, talla, suela, marca, temporada])

print(f"Se han generado y guardado todas las combinaciones con nombres únicos en '{nombre_archivo}'.")
