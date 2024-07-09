def inserir_paciente(nome, cpf, cns, sexo, data_nascimento, endereco):
    """Insere um novo paciente no banco de dados."""
    try:
        cursor.execute(
            """
            INSERT INTO Paciente (Nome, CPF, CNS, Sexo, DataNascimento, Endereco)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (nome, cpf, cns, sexo, data_nascimento, endereco),
        )
        conn.commit()
        print("Paciente inserido com sucesso!")
    except pyodbc.Error as ex:
        print(f"Erro ao inserir paciente: {ex}")

def atualizar_paciente(id, nome, cpf, cns, sexo, data_nascimento, endereco):
    """Atualiza os dados de um paciente existente."""
    try:
        cursor.execute(
            """
            UPDATE Paciente
            SET Nome = ?, CPF = ?, CNS = ?, Sexo = ?, DataNascimento = ?, Endereco = ?
            WHERE id = ?
            """,
            (nome, cpf, cns, sexo, data_nascimento, endereco, id),
        )
        conn.commit()
        print("Paciente atualizado com sucesso!")
    except pyodbc.Error as ex:
        print(f"Erro ao atualizar paciente: {ex}")

def excluir_paciente(id):
    """Exclui um paciente do banco de dados."""
    try:
        cursor.execute(
            """
            DELETE FROM Paciente
            WHERE id = ?
            """,
            (id,),
        )
        conn.commit()
        print("Paciente excluído com sucesso!")
    except pyodbc.Error as ex:
        print(f"Erro ao excluir paciente: {ex}")

def buscar_pacientes():
    """Retorna todos os pacientes do banco de dados."""
    try:
        cursor.execute("SELECT * FROM Paciente")
        pacientes = cursor.fetchall()
        return pacientes
    except pyodbc.Error as ex:
        print(f"Erro ao buscar pacientes: {ex}")
        return None

def buscar_paciente_por_id(id):
    """Retorna um paciente específico pelo ID."""
    try:
        cursor.execute("SELECT * FROM Paciente WHERE id = ?", (id,))
        paciente = cursor.fetchone()
        return paciente
    except pyodbc.Error as ex:
        print(f"Erro ao buscar paciente por ID: {ex}")
        return None