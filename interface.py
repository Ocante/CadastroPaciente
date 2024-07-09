import tkinter as tk
from tkinter import messagebox
import pyodbc

# Conexão com o banco de dados
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACER\\MSSQLSERVER3;DATABASE=PacienteDB;UID=sa;PWD=adm123')
cursor = conn.cursor()

# Função para salvar os dados no banco de dados
def salvar_dados():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    cns = entry_cns.get()
    sexo = entry_sexo.get()
    data_nascimento = entry_data_nascimento.get()
    endereco = entry_endereco.get()

    # Validar campos obrigatórios
    if not nome or not cpf or not cns or not sexo or not data_nascimento:
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    # Remover caracteres não numéricos de CPF e CNS
    cpf = ''.join(filter(str.isdigit, cpf))
    cns = ''.join(filter(str.isdigit, cns))

    # Verificar duplicidade por CPF ou CNS
    cursor.execute("SELECT COUNT(*) FROM Paciente WHERE CPF = ? OR CNS = ?", (cpf, cns))
    count = cursor.fetchone()[0]
    if count > 0:
        messagebox.showerror("Erro", "Já existe um paciente cadastrado com este CPF ou CNS.")
        return

    # Inserir dados no banco de dados
    try:
        cursor.execute("INSERT INTO Paciente (Nome, CPF, CNS, Sexo, DataNascimento, Endereco) VALUES (?, ?, ?, ?, ?, ?)",
                       (nome, cpf, cns, sexo, data_nascimento, endereco))
        conn.commit()
        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
        limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar paciente: {e}")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_cns.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_data_nascimento.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Paciente")

# Labels e campos de entrada
tk.Label(root, text="Nome*:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="CPF*:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="CNS*:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_cns = tk.Entry(root)
entry_cns.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Sexo*:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_sexo = tk.Entry(root)
entry_sexo.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Data de Nascimento*:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
entry_data_nascimento = tk.Entry(root)
entry_data_nascimento.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Endereço:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=5, column=1, padx=5, pady=5)

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.grid(row=6, column=0, columnspan=2, pady=10)

tk.Button(frame_botoes, text="Salvar", command=salvar_dados).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Limpar", command=limpar_campos).grid(row=0, column=1, padx=5)

# Executar a aplicação
root.mainloop()
