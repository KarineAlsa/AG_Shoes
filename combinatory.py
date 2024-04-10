import random
import csv

tipos = ['deportivo', 'formal', 'casual']
materiales = ['cuero', 'tela', 'sintetico']
colores = ['negro', 'azul', 'blanco', 'dorado', 'turquesa', 'amarillo', 'lavanda', 'rosado', 'gris', 'violeta']
tallas = list(range(24, 30))
suelas = ['goma', 'cuero', 'curva', 'plana', 'tacón']
marcas = ['Nike', 'Prada', 'Adidas']
duration = ['Alta', 'Media', 'Baja']

num_combinaciones = len(tipos) * len(materiales) * len(colores) * len(tallas) * len(suelas) * len(marcas) * len(duration)

nombres_unicos = random.sample(range(100000, 999999), num_combinaciones)

nombre_archivo = 'combinaciones_con_nombres.csv'

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    
    writer.writerow(['NombreUnico','Tipo', 'Material', 'Color', 'Talla', 'Suela', 'Marca', 'Duracion'])
    
    for tipo in tipos:
        for material in materiales:
            for color in colores:
                for talla in tallas:
                    for suela in suelas:
                        for marca in marcas:
                            for duracion in duration:
                                nombre_unico = nombres_unicos.pop(0)
                                writer.writerow([nombre_unico, tipo, material, color, talla, suela, marca, duracion])

print(f"Se han generado y guardado todas las combinaciones con nombres únicos en '{nombre_archivo}'.")
