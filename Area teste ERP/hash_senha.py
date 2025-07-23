import bcrypt as bc

def gerar_hash_senha(nome, senha):
    senha_hash = bc.hashpw(senha.encode('utf-8'), bc.gensalt())
    print(f"Nome: {nome}, Senha Hash: {senha_hash.decode()}")
    return senha_hash