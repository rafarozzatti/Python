## Cores no Terminal

#### Configuração básica:

```python
print('\033[S:T:B\033[m')
# onde S é o estilo, T é o texto e B é a cor de fundo
```
#### Exemplo: 

```python
print('\033[7:33:44Olá, Mundo!\033[m')
# A frase 'Olá, Mundo' terá a seguinte formatação: Inversão de cores, texto em amarelo e fundo azul.
```

#### Tabela Style:

| Número | Função |
|--------|-------------|
| 0 | Nada |
| 1 | Negrito |
| 4 | Sublinhado |
| 7 | Inverte as cores |

#### Tabela Text:

| Número | Função |
|--------|--------|
| 30 | Branco |
| 31 | Vermelho |
| 32 | Verde |
| 33 | Amarelo |
| 34 | Azul |
| 35 | Roxo |
| 36 | Azul claro |
| 37 | Cinza |

#### Tabela Back:

| Número | Função |
|--------|--------|
| 40 | Branco |
| 41 | Vermelho |
| 42 | Verde |
| 43 | Amarelo |
| 44 | Azul |
| 45 | Roxo |
| 46 | Azul claro |
| 47 | Cinza |