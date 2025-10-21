import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para conectar e criar a tabela no banco de dados
def inicializar_banco():
    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# Função para salvar os dados no banco
def salvar_cliente():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not nome or not email or not telefone:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos antes de salvar.")
        return

    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)', (nome, email, telefone))
    conexao.commit()
    conexao.close()

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    limpar_formulario()

# Função para limpar os campos do formulário
def limpar_formulario():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# Função para visualizar os clientes cadastrados
def visualizar_clientes():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Clientes Cadastrados")
    nova_janela.geometry("400x300")

    lista = tk.Listbox(nova_janela, width=60)
    lista.pack(pady=10)

    conexao = sqlite3.connect('clientes.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, email, telefone FROM clientes')
    clientes = cursor.fetchall()
    conexao.close()

    if clientes:
        for cliente in clientes:
            lista.insert(tk.END, f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")
    else:
        lista.insert(tk.END, "Nenhum cliente cadastrado.")

# Inicializa o banco de dados
inicializar_banco()
https://programiz.pro/ide/python/S9GXIND0UC?utm_medium=playground&utm_source=python-shared-project-link
# Criação da interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("300x300")

# Labels e campos de entrada
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="E-mail:").pack(pady=5)
entry_email = tk.Entry(janela, width=40)
entry_email.pack()

tk.Label(janela, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack()

# Botões
tk.Button(janela, text="Salvar", command=salvar_cliente, bg="green", fg="white").pack(pady=10)
tk.Button(janela, text="Limpar", command=limpar_formulario, bg="gray", fg="white").pack(pady=5)
tk.Button(janela, text="Visualizar Clientes", command=visualizar_clientes, bg="blue", fg="white").pack(pady=5)

# Executa a janela
janela.mainloop()
