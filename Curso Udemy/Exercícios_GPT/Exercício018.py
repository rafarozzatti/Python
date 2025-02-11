"""Exercício: Crie um dicionário com nome e idade de cinco pessoas. Depois:
- Adicione um novo nome com idade.
- Atualize a idade de uma pessoa.
- Remova uma pessoa do dicionário."""

pessoas = {
    "Ana": 25,
    "Carlos": 30,
    "Beatriz": 22,
    "Pedro": 27,
    "Fernanda": 29
}

print("Dicionário original:", pessoas)
pessoas["Rafael"] = 26
pessoas.update({"Carlos": 31})
pessoas.pop("Fernanda")
print("Dicionário atualizado:", pessoas)
