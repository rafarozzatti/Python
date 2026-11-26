# **Diferentes cenários de execução**

### **1. O que são cenários de execução?**

Um cenário de execução representa uma possibilidade de comportamento do programa diante de determinada informação.

Imagine um sistema que verifica a aprovação de um aluno:

```python
nota = float(input('Digite sua nota: '))

if nota >= 7:    
    print('Aprovado')
else:    
    print('Reprovado')
```

Nesse exemplo, temos dois cenários:

- Nota igual ou superior a 7: aprovado.
- Nota inferior a 7: reprovado.

O programa escolhe automaticamente qual caminho executar.

### **2. Utilizando&#x20;**`if`**,&#x20;**`elif`**&#x20;e&#x20;**`else`**&#x20;para diferentes cenários**

Podemos trabalhar com mais de duas possibilidades utilizando `elif`.

Imagine uma classificação de desempenho:

- Nota igual ou superior a 9: excelente.
- Nota igual ou superior a 7: bom.
- Nota igual ou superior a 5: regular.
- Nota inferior a 5: insuficiente.

```python
nota = float(input('Digite sua nota: '))

if nota >= 9:    
    print('Excelente')
elif nota >= 7:    
    print('Bom')
elif nota >= 5:    
    print('Regular')
else:    
    print('Insuficiente')
```

Observe que as condições são verificadas de cima para baixo.

Quando uma condição é verdadeira, seu bloco é executado e as demais condições são ignoradas.

### **3. Criando cenários com diferentes variáveis**

Também podemos utilizar mais de uma informação para determinar o resultado.

Imagine uma análise de aprovação que considera nota e frequência:

- Nota igual ou superior a 7 e frequência igual ou superior a 75%: aprovado.
- Nota igual ou superior a 7, mas frequência inferior a 75%: reprovado por frequência.
- Nota inferior a 7: reprovado por nota.

```python
nota = float(input('Digite a nota: '))
frequencia = float(input('Digite a frequência: '))

if nota >= 7 and frequencia >= 75:    
    print('Aprovado')
elif nota >= 7 and frequencia < 75:    
    print('Reprovado por frequência')
else:    
    print('Reprovado por nota')
```

Aqui, o resultado depende da combinação de duas informações.

### **4. Cenários utilizando condições aninhadas**

Também podemos organizar os cenários utilizando condições dentro de outras condições.

Imagine um sistema que analisa a concessão de um benefício:

- Primeiro, verifica se o funcionário está ativo.
- Depois, verifica se seu salário é inferior a R$ 3.000.
- Se atender aos dois requisitos, recebe o benefício.

```python
funcionario_ativo = True
salario = 2500

if funcionario_ativo:    
    if salario < 3000:        
        print('Benefício concedido')    
    else:        
        print('Salário acima do limite')
else:    
    print('Funcionário inativo')
```

Nesse exemplo, o programa só verifica o salário se o funcionário estiver ativo.

Isso permite criar diferentes caminhos de execução de maneira organizada.

## **Resumo**

- Um cenário representa uma possibilidade de execução do programa.
- `if`, `elif` e `else` permitem criar diferentes caminhos.
- Podemos utilizar várias condições para determinar um resultado.
- Condições aninhadas permitem organizar verificações em etapas.
