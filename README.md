# CadastroPaciente
 Criar um banco de dados para contemplar os dados do cadastro de pacientes

 # Documentação do Sistema de Cadastro de Pacientes

Por: Ocante António

## Sumário

1. [Configuração do SQL Server](#configuracao-sql-server)
2. [Criação do Banco de Dados e Tabelas](#criacao-banco-tabelas)
3. [Configuração da Conexão Python com SQL Server](#configuracao-conexao-python)
4. [Interface Gráfica com Tkinter](#interface-grafica-tkinter)
5. [Geração de Relatórios](#geracao-relatorios)
6. [Referências](#referencias)

---

## 1. Configuração do SQL Server <a name="configuracao-sql-server"></a>

Para configurar o SQL Server na máquina, segui os passos abaixo:

1. **Instalação do SQL Server:**
   - Baixei e instalei o Microsoft SQL Server.
   - Durante a instalação, configurei a instância do SQL Server conforme necessário.

2. **Configuração do SQL Server Management Studio (SSMS):**
   - Baixei e instalei o SQL Server Management Studio (SSMS).

3. **Criando um Novo Banco de Dados:**
   - Abri o SSMS e estabeleci a conexão ao servidor.
   - Criei um novo banco de dados para armazenar os dados dos pacientes.

---

## 2. Criação do Banco de Dados e Tabelas <a name="criacao-banco-tabelas"></a>

Para criar a tabela `Paciente` no banco de dados `PacienteDB`, defini os campos obrigatórios e configurei as restrições de unicidade para `CPF` e `CNS` para evitar duplicidade.

---

## 3. Configuração da Conexão Python com SQL Server <a name="configuracao-conexao-python"></a>

Para conectar sua aplicação Python ao SQL Server, utilizei a biblioteca `pyodbc`.

1. **Instalação do `pyodbc`:**
   - Instalei o `pyodbc` utilizando o gerenciador de pacotes pip.

2. **Configuração da Conexão:**
   - Estabeleci a conexão com o banco de dados `PacienteDB` utilizando a string de conexão apropriada.

---

## 4. Interface Gráfica com Tkinter <a name="interface-grafica-tkinter"></a>

A interface gráfica utiliza a biblioteca `tkinter` para criar a janela de cadastro de pacientes.

1. **Campos de Entrada:**
   - Criei campos de entrada para nome, CPF, CNS, sexo, data de nascimento e endereço.

2. **Botões:**
   - Adicionei botões para salvar os dados e limpar os campos de entrada.

3. **Validação e Verificação de Duplicidade:**
   - Validei os campos obrigatórios e verifiquei a duplicidade por CPF ou CNS antes de inserir os dados no banco de dados.

---

## 5. Geração de Relatórios <a name="geracao-relatorios"></a>

Para a geração de relatórios, utilizei o Report Builder do SQL Server.

1. **Instalação do Report Builder:**
   - Baixei e instalei o Microsoft Report Builder.

2. **Criando um Relatório:**
   - Conectei ao banco de dados `PacienteDB` e criei um novo relatório.
   - Adicionei uma consulta que selecione os dados dos pacientes e formatei o relatório.

---

## 6. Referências <a name="referencias"></a>

- **Python:**
  - Documentação: [Python Docs](https://docs.python.org/3/)
  - Biblioteca `pyodbc`: [Pyodbc Documentation](https://github.com/mkleehammer/pyodbc)

- **Tkinter:**
  - Documentação: [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)

- **SQL Server:**
  - Download e Instalação: [SQL Server Downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
  - Documentação: [SQL Server Documentation](https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15)

- **Microsoft Report Builder:**
  - Download e Instalação: [Microsoft Report Builder](https://www.microsoft.com/en-us/download/details.aspx?id=53613)
  - Documentação: [Report Builder Docs](https://docs.microsoft.com/en-us/sql/reporting-services/report-builder/report-builder-in-sql-server-reporting-services)

