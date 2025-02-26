"""Use um deque para armazenar o histórico de navegação de um navegador. Adicione algumas páginas visitadas e implemente a funcionalidade de voltar e avançar nas páginas."""

from collections import deque

historico = deque()
futuro = deque()

historico.append("google.com")
futuro.clear()
print(f"Acessando: {historico[-1]}")

historico.append("youtube.com")
futuro.clear()
print(f"Acessando: {historico[-1]}")

historico.append("github.com")
futuro.clear()
print(f"Acessando: {historico[-1]}")

if len(historico) > 1:
    futuro.appendleft(historico.pop()) 
    print(f"Voltando para: {historico[-1]}")
else:
    print("Não há páginas anteriores.")

if len(historico) > 1:
    futuro.appendleft(historico.pop())
    print(f"Voltando para: {historico[-1]}")
else:
    print("Não há páginas anteriores.")

if futuro:
    historico.append(futuro.popleft())
    print(f"Avançando para: {historico[-1]}")
else:
    print("Não há páginas no futuro.")

historico.append("stackoverflow.com")
futuro.clear()
print(f"Acessando: {historico[-1]}")

if futuro:
    historico.append(futuro.popleft())
    print(f"Avançando para: {historico[-1]}")
else:
    print("Não há páginas no futuro.")
