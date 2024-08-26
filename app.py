import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar o arquivo CSV
def carregar_arquivo():
    filepath = filedialog.askopenfilename()
    if filepath:
        global df
        df = pd.read_csv(filepath)
        label_status.config(text=f"Arquivo carregado: {filepath}")
        button_visualizar.config(state=tk.NORMAL)
    else:
        label_status.config(text="Nenhum arquivo selecionado.")

# Função para visualizar os dados
def visualizar_dados():
    if 'df' in globals():
        df.head()  # Exibe as primeiras linhas dos dados no console
        mostrar_graficos()
    else:
        label_status.config(text="Carregue um arquivo primeiro.")

# Função para mostrar gráficos
def mostrar_graficos():
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    df.plot(kind='bar', x=df.columns[0], y=df.columns[1], legend=False, color='skyblue')
    plt.title('Gráfico de Barras')
    
    plt.subplot(1, 2, 2)
    df.plot(kind='line', x=df.columns[0], y=df.columns[1], legend=False, color='green')
    plt.title('Gráfico de Linhas')
    
    plt.tight_layout()
    plt.show()

# Criação da interface gráfica
root = tk.Tk()
root.title("Plataforma de Análise de Dados")

# Botões e Labels
button_carregar = tk.Button(root, text="Carregar Arquivo CSV", command=carregar_arquivo)
button_carregar.pack(pady=10)

label_status = tk.Label(root, text="Nenhum arquivo carregado.")
label_status.pack(pady=10)

button_visualizar = tk.Button(root, text="Visualizar Dados", command=visualizar_dados, state=tk.DISABLED)
button_visualizar.pack(pady=10)

# Execução da interface gráfica
root.mainloop()
