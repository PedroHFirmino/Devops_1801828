import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import app  
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
def test_listar_alunos(client: FlaskClient):
    "GET"
    response = client.get('/alunos')
    assert response.status_code == 200
    assert isinstance(response.json, list)
def test_adicionar_aluno(client: FlaskClient):
    "POST"
    new_aluno = {
        "Nome": "Pedro",
        "Sobrenome": "Firmino",
        "Turma": "TADS",
        "Disciplinas": "Devops, Java, Projeto de Vida",
        "RA": "1801828"
    }
    response = client.post('/alunos', json=new_aluno)
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno adicionado com sucesso!'