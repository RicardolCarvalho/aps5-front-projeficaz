import streamlit as st
import requests as rq

URL = "http://127.0.0.1:5000"

def tela_inicial():
    st.title("Tela inicial")

def minhas_bikes():
    r = rq.get(URL)
    status = r.status_code
    if status == 200:
        st.table(r.json())

def meus_usuarios():
    r = rq.get(URL)
    status = r.status_code
    if status == 200:
        st.table(r.json())

def meus_emprestimos():
    r = rq.get(URL)
    status = r.status_code
    if status == 200:
        st.table(r.json())

def nova_bike():
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano_publicacao = st.text_input("Ano de Publicação")
    genero = st.text_input("Gênero")
    if st.button('Cadastrar'):
        r = rq.post(URL, json={'Livro': {"titulo": titulo, "autor": autor, "ano_publicacao": ano_publicacao, "genero": genero}})
        if r.status_code == 201:
            st.success('Livro cadastrado com sucesso')

def novo_usuario():
    cpf = st.text_input("CPF")
    email = st.text_input("Email")
    nome = st.text_input("Nome")

    if st.button('Cadastrar'):
        r = rq.post(URL, json={'Usuario': {"cpf": cpf, "email": email, "nome": nome}})
        if r.status_code == 201:
            st.success('Usuário cadastrado com sucesso')

def novo_emprestimo():
    id_usuario = st.text_input('Id do usuario')
    id_bike = st.text_input('Id da bike')
    if st.button('Buscar Usuario'):
        r = rq.get(f'{URL}/usuarios/{id_usuario}')
        if r.status_code != 200:
            st.error('Usuário não encontrado')
    if st.button('Buscar Bike'):
        q = rq.get(f'{URL}/bikes/{id_bike}')
        if q.status_code != 200:
            st.error('Bike não encontrada')
    if st.button("Cadastrar"):
        r = rq.post(f'{URL}/emprestimos', json={'Emprestimo': {'id_usuario': id_usuario, 'id_bike': id_bike}})
        if r.status_code == 201:
            st.success("Empréstimo cadastrado com sucesso")

def dados_usuario():
    id = st.text_input('Id do usuario')
    if st.button('Buscar Usuario'):
        r = rq.get(f'{URL}/{id}')
        st.session_state['Usuario'] = r.json()
    if 'Usuario' in st.session_state:
        c = st.text_input("cpf")
        e = st.text_input("data")
        n = st.text_input("nome")
        if st.button('Atualizar Usuario'):
            rq.put(f'{URL}/{st.session_state["Usuario"]["id"]}', json={'Usuario': {"cpf": c, "email": e, "nome": n}})
        if st.button('Apagar Usuario'):
            rq.delete(f'{URL}/{st.session_state["Usuario"]["id"]}')

def dados_bike():
    id = st.text_input('Id da bike')
    if st.button('Buscar Bike'):
        r = rq.get(f'{URL}/{id}')
        st.session_state['Bike'] = r.json()
    if 'Bike' in st.session_state:
        t = st.text_input("titulo")
        a = st.text_input("autor")
        ap = st.text_input("ano de publicacao")
        g = st.text_input("genero")
        if st.button('Atualizar Bike'):
            rq.put(f'{URL}/{st.session_state["Bike"]["id"]}', json={'Bike': {"titulo": t, "autor": a, "ano_publicacao": ap, "genero": g}})
        if st.button('Apagar Bike'):
            rq.delete(f'{URL}/{st.session_state["Bike"]["id"]}')

def dados_emprestimo():
    id = st.text_input('Id do emprestimo')
    id_usuario = st.text_input('Id do usuario')
    id_bike = st.text_input('Id da bike')
    if st.button('Buscar Usuario'):
        r = rq.get(f'{URL}/usuarios/{id_usuario}')
        if r.status_code != 200:
            st.error('Usuário não encontrado')
    if st.button('Buscar Bike'):
        q = rq.get(f'{URL}/bikes/{id_bike}')
        if q.status_code != 200:
            st.error('Bike não encontrada')
    if st.button('Buscar Emprestimo'):
        r = rq.get(f'{URL}/{id}')
        st.session_state['Emprestimo'] = r.json()
    if 'Emprestimo' in st.session_state:
        id_usuario = st.text_input("Id do usuario")
        id_bike = st.text_input("Id da bike")
        if st.button('Atualizar Emprestimo'):
            rq.put(f'{URL}/{st.session_state["Emprestimo"]["id"]}', json={'Emprestimo': {"id_usuario": id_usuario, "id_bike": id_bike}})
        if st.button('Apagar Emprestimo'):
            rq.delete(f'{URL}/{st.session_state["Emprestimo"]["id"]}')

if __name__ == "__main__":
    tela_inicial()
    st.sidebar.subheader("Menu")
    opcao = st.sidebar.radio("", ["Minhas Bikes", "Meus Usuários", "Meus Empréstimos", "Nova Bike", "Novo Usuário", "Novo Empréstimo"])
    
    if opcao == "Minhas Bikes":
        minhas_bikes()
    elif opcao == "Meus Usuários":
        meus_usuarios()
    elif opcao == "Meus Empréstimos":
        meus_emprestimos()
    elif opcao == "Nova Bike":
        nova_bike()
    elif opcao == "Novo Usuário":
        novo_usuario()
    elif opcao == "Novo Empréstimo":
        novo_emprestimo()
