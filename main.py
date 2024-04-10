import tkinter as tk
from tkinter import ttk
import AG
import matplotlib.pyplot as plt
from tkinter import messagebox
import csv

def write_document(best):
    with open('best.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['Modelo', 'Características'])
        
        for idx, modelo_caracteristicas in enumerate(best, start=1):
            modelo = modelo_caracteristicas[0]
            caracteristicas = modelo_caracteristicas[1:]
            tipo, material, color, talla, suela, marca, duracion = caracteristicas
            
            caracteristicas_str = (
                f"Características: Tipo {tipo}, Material {material}, Color {color}, "
                f"Talla {talla}, Suela {suela}, Marca {marca}, Duración {duracion}"
            )
            writer.writerow([f"{idx}. Modelo: {modelo}", caracteristicas_str])




def submit():
    AG.preferencias_cliente = [tipo.get(), material.get(), color.get(), talla.get(), suela.get(), marca.get(), duracion.get()]
    AG.pesos = [0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1]
    history, best = AG.run(int(first_population.get()), float(mutation_probability.get()), float(mutation_individual_probability.get()), int(limit_population.get()))
    generate_graph(history)
    first = best[0]
    second = best[1]
    third = best[2]
    message = (
    f"1. Modelo: {first[0]}\n"
    f"   Características: Tipo {first[1]}, Material {first[2]}, Color {first[3]}, "
    f"Talla {first[4]}, Suela {first[5]}, Marca {first[6]}, Duración {first[7]}\n\n"
    f"2. Modelo: {second[0]}\n"
    f"   Características: Tipo {second[1]}, Material {second[2]}, Color {second[3]}, "
    f"Talla {second[4]}, Suela {second[5]}, Marca {second[6]}, Duración {second[7]}\n\n"
    f"3. Modelo: {third[0]}\n"
    f"   Características: Tipo {third[1]}, Material {third[2]}, Color {third[3]}, "
    f"Talla {third[4]}, Suela {third[5]}, Marca {third[6]}, Duración {third[7]}"
    )
    messagebox.showinfo("Mejores zapatos", message)
    write_document(best)

def generate_graph(history):
    plt.plot(history)
    plt.xlabel('Generación')
    plt.ylabel('Fitness')
    print(len(history))
    if len(history) > 1:
        plt.xlim(0, len(history))
    else:
        plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig('fitness.png')
    plt.show()


root = tk.Tk()
root.geometry("500x700")

tk.Label(root, text="Tipo: ").pack()
tipo = ttk.Combobox(root, values=['deportivo', 'formal', 'casual'])
tipo.pack()

tk.Label(root, text="Material: ").pack()
material = ttk.Combobox(root, values=['cuero', 'tela', 'sintetico'])
material.pack()

tk.Label(root, text="Color: ").pack()
color = ttk.Combobox(root, values=['negro', 'azul', 'blanco', 'dorado', 'turquesa', 'amarillo', 'lavanda', 'rosado', 'gris', 'violeta'])
color.pack()

tk.Label(root, text="Talla: ").pack()
talla = ttk.Combobox(root, values=list(range(24, 30)))
talla.pack()

tk.Label(root, text="Suela: ").pack()
suela = ttk.Combobox(root, values=['goma', 'cuero', 'curva', 'plana', 'tacón'])
suela.pack()

tk.Label(root, text="Marca: ").pack()
marca = ttk.Combobox(root, values=['Nike', 'Prada', 'Adidas'])
marca.pack()

tk.Label(root, text="Duración: ").pack()
duracion = ttk.Combobox(root, values=['Alta', 'Media', 'Baja'])
duracion.pack()

tk.Label(root, text="First Population: ").pack()
first_population = tk.Entry(root)
first_population.pack()

tk.Label(root, text="Mutation Probability: ").pack()
mutation_probability = tk.Entry(root)
mutation_probability.pack()

tk.Label(root, text="Mutation Individual Probability: ").pack()
mutation_individual_probability = tk.Entry(root)
mutation_individual_probability.pack()

tk.Label(root, text="Limit Population: ").pack()
limit_population = tk.Entry(root)
limit_population.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()