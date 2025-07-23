import sqlite3 as con
import bcrypt
#criar tabela de usuarios no banco de dados

sql_usuarios = '''
    CREATE TABLE IF NOT EXISTS usuarios (
    Nome_login TEXT UNIQUE NOT NULL,
    Senha_login TEXT UNIQUE NOT NULL
    );
'''

#conectar com o arquivo do banco de dados
try:
    conexao = con.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute(sql_usuarios)

    conexao.commit()

except con.Error as erro:
    print("Erro ao criar tabela:", erro)

finally:
    if conexao:
        conexao.close()
        #print("conexao com o banco de dados concluida com sucesso")

conexao = con.connect("usuarios.db")
cursor = conexao.cursor()
res = cursor.execute("SELECT * FROM usuarios")
print(res.fetchall())

def inserir_usuarios(nome, senha_hash): #aqui estamos pegando os argumentos que sairam do entry e irão entrar para o banco de dados
    try:
        conexao = con.connect("usuarios.db") #fazer a conexão com o banco de dados
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (Nome_login, senha_login) VALUES (?, ?)",
        (nome, senha_hash))

        conexao.commit() #commitando as adições ao banco de dados
        
    except con.IntegrityError:
        return "Usuario já cadastrado"
    
    except con.Error as erro:
        return str(erro)

    
    finally:
        if conexao:
            conexao.close()
def verificar_senhas(senha_login1, senha_hash):
    return bcrypt.checkpw(senha_login1.encode('utf-8'), senha_hash)

def entrar_login1(nome_login1, senha_login1):
    try: 
        conexao = con.connect("usuarios.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT Senha_login FROM usuarios WHERE Nome_login = ?", (nome_login1,))
        resultado = cursor.fetchone()

        if resultado:
            senha_hash = resultado[0]

            # Garante que está em bytes
            if isinstance(senha_hash, str):
                senha_hash = senha_hash.decode('utf-8')

            if verificar_senhas(senha_login1, senha_hash):
                print("✅ Login bem-sucedido!")
                return "Login bem-sucedido"
            else:
                print("❌ Senha incorreta.")
                return "Senha incorreta"
        else:
            print("❌ Usuário não encontrado.")
            return "Usuário não encontrado"
        
    finally:
        conexao.close()

#conexao = con.connect("usuarios.db")
#cursor = conexao.cursor()
#res = cursor.execute("SELECT * FROM usuarios")
#print(res.fetchall())
#conexao.close()