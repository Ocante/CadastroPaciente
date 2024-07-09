def buscar_Paciente():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACER\\MSSQLSERVER3;DATABASE=PacienteDB;UID=sa;PWD=adm123')
    cursor = conn.cursor()
    cursor.execute("SELECT Nome, CPF, CNS, Sexo, DataNascimento, Endereco FROM Paciente")
    Paciente = cursor.fetchall()
    conn.close()
    return Paciente

def salvar_dados():
    # ... (restante do código permanece igual)
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACER\\MSSQLSERVER3;DATABASE=PacienteDB;UID=sa;PWD=adm123')
    # ... (restante do código permanece igual)

def excluir_paciente():
    # ... (restante do código permanece igual)
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=ACER\\MSSQLSERVER3;DATABASE=PacienteDB;UID=sa;PWD=adm123')
    # ... (restante do código permanece igual)
