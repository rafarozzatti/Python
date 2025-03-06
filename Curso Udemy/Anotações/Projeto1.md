# Documentação do Código

## Arquivo: `game.py`

```python
from models.calcular import Calcular  # Importa a classe Calcular do módulo calcular

# Função principal que inicia o jogo
def main() -> None:
    pontos: int = 0  # Inicializa a pontuação como zero
    jogar(pontos)  # Chama a função jogar passando os pontos

# Função que executa o jogo
def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))  # Solicita o nível de dificuldade ao usuário

    calc: Calcular = Calcular(dificuldade)  # Cria um objeto da classe Calcular

    print('Informe o resultado para seguir a operação:')
    calc.mostrar_operacao()  # Exibe a operação matemática gerada

    resultado: int = int(input())  # Captura a resposta do usuário

    if calc.checar_resultado(resultado):  # Verifica se a resposta está correta
        pontos += 1  # Incrementa a pontuação se a resposta estiver correta
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))  # Pergunta se o usuário quer continuar

    if continuar:
        jogar(pontos)  # Chama a função jogar novamente
    else:
        print(f'''Você finalizou com {pontos} ponto(s).
Até a próxima!''')  # Finaliza o jogo

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    main()
```

### Possíveis saídas do `game.py`:
```
Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: 2
Informe o resultado para seguir a operação:
12 + 8 = ?
20
Resposta correta!
Você tem 1 ponto(s).
Deseja continuar no jogo? [1 - sim, 0 - não] 0
Você finalizou com 1 ponto(s).
Até a próxima!
```

---

## Arquivo: `teste.py`

```python
from models.calcular import Calcular  # Importa a classe Calcular do módulo calcular

calc: Calcular = Calcular(1)  # Cria um objeto da classe Calcular com dificuldade 1
print(calc)  # Exibe os valores gerados aleatoriamente
```

### Possíveis saídas do `teste.py`:
```
Valor 1: 3
Valor 2: 7
Dificuldade: 1
Operação: Somar
```

---

## Arquivo: `calcular.py`

```python
from random import randint  # Importa a função randint para gerar números aleatórios

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor  # Gera o primeiro valor
        self.__valor2: int = self._gerar_valor  # Gera o segundo valor
        self.__operacao: int = randint(1, 3)  # Define a operação matemática aleatória
        self.__resultado: int = self._gerar_resultado  # Calcula o resultado correto

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'
    
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
        
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Respota correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
```

### Possíveis saídas de um objeto `Calcular`:
```
Valor 1: 15
Valor 2: 7
Dificuldade: 2
Operação: Diminuir
```

---
