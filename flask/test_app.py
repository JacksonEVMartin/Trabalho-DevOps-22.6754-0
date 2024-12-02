import pytest
from app import app, db, Aluno

@pytest.fixture
def client():
    # Configura o Flask para o modo de teste
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria tabelas no banco em memória
        yield client
        with app.app_context():
            db.drop_all()  # Remove tabelas após o teste

def test_adicionar_aluno(client):
    # Dados do aluno a serem enviados
    novo_aluno = {
        "nome": "Jackson",
        "sobrenome": "Martin",
        "turma": "4 Período",
        "disciplinas": "TADS",
        "ra": "22.6754-0"
    }
    
    # Chamada ao endpoint POST /alunos
    response = client.post('/alunos', json=novo_aluno)
    
    # Verifica se o status HTTP é 201 (Criado)
    assert response.status_code == 201
    assert response.get_json() == {"message": "Aluno adicionado com sucesso!"}

    # Verifica se o aluno foi adicionado ao banco
    with app.app_context():
        aluno = Aluno.query.filter_by(ra="123456").first()
        assert aluno is not None
        assert aluno.nome == "Jackson"
        assert aluno.sobrenome == "Martin"
        assert aluno.turma == "4 Período"
        assert aluno.disciplinas == "TADS"