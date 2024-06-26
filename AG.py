import random
import matplotlib.pyplot as plt
import csv

tipos = ['deportivo', 'formal', 'casual']
ocasiones = ['fiesta', 'diario', 'caminar']
colores = ['negro', 'azul', 'blanco', 'dorado', 'turquesa', 'amarillo', 'rosado', 'lavanda', 'rosado', 'gris', 'violeta']
tallas = ['24','25', '26','27','28','29']
suelas = ['goma', 'cuero', 'curva', 'plana', 'tacón']
marcas = ['Nike', 'Prada', 'Adidas']
temporadas = ['Primavera', 'Verano', 'Otoño', 'Invierno']

pesos = []

preferencias_cliente = []

def generar_zapato():
    tipo = random.choice(tipos)
    ocasion = random.choice(ocasiones)
    color = random.choice(colores)
    talla = random.choice(tallas)
    suela = random.choice(suelas)
    marca = random.choice(marcas)
    temporada = random.choice(temporadas)

    return [tipo, ocasion, color, talla, suela, marca, temporada]


def add_points_index(poblation):
    fitness_counter = []
    for i in poblation:
        fitness_counter.append(evaluation(i))
    return fitness_counter


def evaluation(genoma):
    points = 0
    for i, preference in enumerate(preferencias_cliente):
        if preference == genoma[i]:
            points += 1 * pesos[i]
    return points


def generate_poblation(num_initial):
    poblation = []
    for i in range(num_initial):
        poblation.append(generar_zapato())
    return poblation


def selection(poblation):
    fitness_counter = add_points_index(poblation)
    temp_list = zip(fitness_counter, poblation)
    sorted_list = sorted(temp_list, key=lambda x: x[0], reverse=True)
    final_sorted_list = [x for _, x in sorted_list]
    list_sorted = [x for _, x in sorted_list]
    list_slice = list_sorted[:len(list_sorted) // 2]
    return list_slice, final_sorted_list, fitness_counter, list_sorted[0]


def crossover(list_slice, sorted_list):
    index_to_crossover_to_sorted_list = random.randint(0, len(sorted_list) - 1)
    random_slice = random.randint(0, len(list_slice) - 1)
    if sorted_list[index_to_crossover_to_sorted_list] != list_slice:
        
        child1 = list_slice[:random_slice] + sorted_list[index_to_crossover_to_sorted_list][random_slice:]

   
        child2 = sorted_list[index_to_crossover_to_sorted_list][:random_slice] + list_slice[random_slice:]
    else:
        child1, child2 =crossover(list_slice, sorted_list)
    
    return child1,child2


def mutation(probability_gen, probability_individual, mutates):
    
    if random.random() < probability_individual:
        index_to_mutate = random.randint(0, len(mutates) - 1)
        for i in range(len(mutates[index_to_mutate])):
            if random.random() < probability_gen:
                if i == 0:  # tipo
                    mutates[index_to_mutate][i] = random.choice(tipos)
                elif i == 1:  # Ocasión
                    mutates[index_to_mutate][i] = random.choice(ocasiones)
                elif i == 2:  # color
                    mutates[index_to_mutate][i] = random.choice(colores)
                elif i == 3:  # talla
                    mutates[index_to_mutate][i] = random.choice(tallas)
                elif i == 4:  # suela
                    mutates[index_to_mutate][i] = random.choice(suelas)
                elif i == 5:  # marca
                    mutates[index_to_mutate][i] = random.choice(marcas)
                elif i == 6:  # Temporada
                    mutates[index_to_mutate][i] = random.choice(temporadas)
    return mutates


def pruning(sorted_list, limit_population):
    
    final_list = []
    
    sorted_list = eliminate_same(sorted_list)
    
    for i in range(len(sorted_list)):
        final_list.append(evaluation(sorted_list[i]))
    temp = zip(final_list, sorted_list)
    
    sorted_list = sorted(temp, key=lambda x: x[0], reverse=True)
   
    
    final_sorted_list = [x for _, x in sorted_list]
    best = final_sorted_list[0]
    
    while len(final_sorted_list) > limit_population:
        
        random_choice = random.randint(0, len(final_sorted_list) - 1)
        if final_sorted_list[random_choice] != best:
            final_sorted_list.pop(random_choice)
    return final_sorted_list


def eliminate_same(jau):
    lista_sin_duplicados = []
    
    for m in jau:
        if m not in lista_sin_duplicados:
            
            lista_sin_duplicados.append(m)
            
    return lista_sin_duplicados

def cargar_combinaciones(csv_filename):
    combinaciones = []
    with open(csv_filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader) 
        for row in csv_reader:
            combinaciones.append(row)
    return combinaciones


def obtener_nombres_mejores_resultados(mejores_resultados, combinaciones):
    nombres_mejores_resultados = []
    
    for resultado in mejores_resultados:
        for combinacion in combinaciones:
            if resultado == combinacion[1:]:
                nombres_mejores_resultados.append(combinacion)  
                break
    return nombres_mejores_resultados

def run( first_population, mutation_probability, mutation_individual_probability, limit_population):
    csv_filename = 'combinaciones_con_nombres.csv'
    combinaciones = cargar_combinaciones(csv_filename)
    history = []
    population = generate_poblation(first_population)
    iterator = 0
    fitness_final = []
    temp_final = []
    
    while True:
        if iterator == 150 and history[-1]>=0.9:
            
            break
        else:
            fitness_final = []
            
            list_slice, sorted_list, fitness, best = selection(population)
            
            for i in range(len(list_slice)):
                mutates =[]
                child1, child2 = crossover(list_slice[i], population)
                mutates.append(child1)
                mutates.append(child2)
                mutated_childs = mutation(mutation_probability, mutation_individual_probability, mutates)
                population.extend(mutated_childs)

            
            for i in range(len(population)):
                fitness_final.append(evaluation(population[i]))

           
            
            st = zip(fitness_final, population)
            temp_final = sorted(st, key=lambda x: x[0], reverse=True)
            temp_final_number = [x for x, _ in temp_final]
            
            history.append(temp_final_number[0])
            
            population = pruning(population, limit_population)

            
            iterator += 1
    temp_final = eliminate_same(temp_final)
    arreglos_caracteristicas = [tupla[1] for tupla in temp_final[:3]]
    
    nombres_mejores_resultados = obtener_nombres_mejores_resultados(arreglos_caracteristicas, combinaciones)
    print(nombres_mejores_resultados)
    return history, nombres_mejores_resultados

