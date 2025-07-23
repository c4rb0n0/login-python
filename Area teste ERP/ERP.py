import customtkinter as ctk
from usuario_do_erp import entrar_login1

from usuario_do_erp import inserir_usuarios

app = ctk.CTk()

app.geometry("700x500")
app.title("ERP_BIG_LARICA")
app._set_appearance_mode("system")

#login
def entrar_login():
    nome_login1 = nome_usuario.get()
    senha_login1 = senha_usuario.get()
    # Aqui você pode adicionar a lógica para verificar o login
    entrar_login1(nome_login1, senha_login1)

nome_usuario = ctk.CTkEntry(app, placeholder_text="digite seu nome")
nome_usuario.pack(pady=10)
senha_usuario = ctk.CTkEntry(app, placeholder_text="digite sua senha", show="*")
senha_usuario.pack(pady=10)

enviar = ctk.CTkButton(app, text="Enviar", command=entrar_login)
enviar.pack()

# importe o argumento que retornou a senha em hash
from hash_senha import gerar_hash_senha

#cadastro
def cadastrar():
    janela_cadastro = ctk.CTkToplevel(app,)
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("400x300")


    nome_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Nome login")
    nome_cadastro.pack(pady=10)
    
    senha_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Senha login", show="*")
    senha_cadastro.pack(pady=10)


#montar função que ira salvar o cadastro e com .get() pegar os valores dos campos e assim fazer um argumento para a função que ira gerar a hash      
    def salvar_cadastro():
        nome = nome_cadastro.get()
        senha = senha_cadastro.get()
        senha_hash = gerar_hash_senha(nome, senha) 

        resultado = inserir_usuarios(nome, senha_hash)
        ctk.CTkLabel(janela_cadastro, text="").pack()
            
            

        if resultado == "sucesso":
            mensagem.configure(text="Cadastro realizado com sucesso", text_color="green")
        elif resultado == "usuario_existe":
            mensagem.configure(text=f"Usuário já cadastrado", text_color="blue")
        else:
            mensagem.configure(text=f"Erro: {resultado}", text_color="red")
        

    mensagem = ctk.CTkLabel(janela_cadastro, text="") #caixa de mensagem que ira mostar erros de castro
    mensagem.pack(padx=30) 

    btn_cadastrar_usuario = ctk.CTkButton(janela_cadastro, text="salvar", command=salvar_cadastro)
    btn_cadastrar_usuario.pack(pady=10)


btn_cadastrar = ctk.CTkButton(master=app, text="Fazer cadastro", command=cadastrar)
btn_cadastrar.pack(pady=20)
app.mainloop()