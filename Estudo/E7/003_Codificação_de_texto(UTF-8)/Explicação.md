## **1. O que é codificação de texto?**

A codificação determina como os caracteres são representados em bytes para que o computador consiga armazenar e interpretar textos.

Por exemplo, considere:

```
São Paulo
Análise de Dados
Informação
```

Essas palavras possuem caracteres especiais, como `ã`, `á` e `ç`.

Para que esses caracteres sejam interpretados corretamente, precisamos utilizar uma codificação compatível.

## **2. O que é UTF-8?**

UTF-8 é uma codificação de caracteres amplamente utilizada na programação e na internet.

Ela permite representar:

- Letras do alfabeto.
- Números.
- Caracteres especiais.
- Acentos.
- Símbolos de diferentes idiomas.

Por isso, é uma boa prática utilizá-la ao trabalhar com arquivos de texto, CSV e JSON.

## **3. Como utilizar UTF-8 no Python?**

Você já conhece a sintaxe:

```
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:    
    conteudo = arquivo.read()
```

O parâmetro:

```
encoding='utf-8'
```

informa ao Python qual codificação deve utilizar para interpretar o conteúdo do arquivo.

Também podemos utilizá-lo ao escrever:

```
with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:    
    arquivo.write('Análise de Dados')
```

## **4. O que acontece quando utilizamos uma codificação incorreta?**

Imagine que um arquivo foi salvo em uma codificação e tentamos abri-lo utilizando outra incompatível.

Podemos encontrar caracteres incorretos, como:

Texto esperado

**Informação, São Paulo**

Texto interpretado incorretamente

**InformaÃ§Ã£o, SÃ£o Paulo**

Esse problema é conhecido como *mojibake*: caracteres são interpretados incorretamente devido a uma incompatibilidade de codificação.

## **5. UTF-8 em CSV e JSON**

Nos arquivos CSV, utilizamos:

```
with open('dados.csv', 'r', encoding='utf-8') as arquivo:    ...
```

Nos arquivos JSON:

```
with open('dados.json', 'r', encoding='utf-8') as arquivo:    
    dados = json.load(arquivo)
```

E ao salvar JSON, também podemos combinar:

```
with open('dados.json', 'w', encoding='utf-8') as arquivo:    
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
```

Lembre-se: `encoding='utf-8'` controla a codificação do arquivo, enquanto `ensure_ascii=False` permite que os caracteres especiais sejam escritos diretamente no JSON.

## **Resumo do tópico**

| Conceito             | Finalidade                                         |
| -------------------- | -------------------------------------------------- |
| Codificação          | Representar caracteres em bytes                    |
| UTF-8                | Codificação amplamente utilizada                   |
| `encoding='utf-8'`   | Informar a codificação ao abrir arquivos           |
| `ensure_ascii=False` | Preservar caracteres especiais diretamente no JSON |
