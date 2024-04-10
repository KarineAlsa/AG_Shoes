import tkinter as tk
from tkinter import ttk
import AG
import matplotlib.pyplot as plt
from tkinter import messagebox


def submit():
    AG.preferencias_cliente = [tipo.get(), material.get(), color.get(), talla.get(), suela.get(), marca.get(), duracion.get()]
    AG.pesos = [0.2, 0.1, 0.1, 0.3, 0.1, 0.1, 0.1]
    history, best = AG.run(int(first_population.get()), float(mutation_probability.get()), float(mutation_individual_probability.get()), int(limit_population.get()))
    generate_graph(history)
    messagebox.showinfo("Mejor zapato", f"\n1. {best[0]}\n 2. {best[1]}\n 3. {best[2]}\n")

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