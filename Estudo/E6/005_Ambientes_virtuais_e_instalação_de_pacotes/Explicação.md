# ** O que são pacotes e bibliotecas externas?**

Até agora, estudamos bibliotecas que já acompanham o Python, como:

- `math`
- `random`
- `datetime`

Essas bibliotecas fazem parte da biblioteca padrão do Python, portanto não precisamos instalá-las separadamente.

Porém, existem muitas outras bibliotecas desenvolvidas pela comunidade que precisamos instalar antes de utilizar.

Alguns exemplos:

| Biblioteca     | Utilização                        |
| -------------- | --------------------------------- |
| `pandas`       | Manipulação e análise de dados    |
| `numpy`        | Operações matemáticas e numéricas |
| `matplotlib`   | Criação de gráficos               |
| `requests`     | Requisições HTTP                  |
| `scikit-learn` | Aprendizado de máquina            |

Por exemplo, para utilizar o Pandas:

```
import pandas as pd
```

Mas, antes disso, precisamos instalar a biblioteca no ambiente Python utilizado.

# **2. O que é o pip?**

O `pip` é o gerenciador de pacotes do Python.

Ele permite instalar, atualizar e desinstalar bibliotecas externas.

Os principais comandos são:

### **Instalar uma biblioteca**

```
pip install pandas
```

Esse comando instala o Pandas.

### **Instalar uma versão específica**

```
pip install pandas==2.2.3
```

O `==` indica que queremos instalar exatamente aquela versão.

### **Atualizar uma biblioteca**

```
pip install --upgrade pandas
```

O `--upgrade` solicita a atualização para uma versão mais recente compatível com o ambiente.

### **Desinstalar uma biblioteca**

```
pip uninstall pandas
```

Remove o pacote instalado.

### **Consultar os pacotes instalados**

```
pip list
```

Exibe uma lista dos pacotes instalados no ambiente Python ativo.

### **Consultar informações de um pacote**

```
pip show pandas
```

Exibe informações como versão, localização e dependências do pacote.

**Importante:** os comandos do `pip` são executados no terminal, não dentro de um arquivo `.py`.

# **3. O que são ambientes virtuais?**

Um ambiente virtual é um espaço isolado que possui seu próprio conjunto de pacotes Python instalados.

Imagine que você tenha dois projetos:

- Projeto A utiliza Pandas na versão 2.2.
- Projeto B utiliza Pandas na versão 3.0.

Se os dois utilizarem exatamente o mesmo ambiente Python, poderá haver conflitos entre as versões necessárias.

O ambiente virtual resolve esse problema, permitindo que cada projeto tenha suas próprias dependências.

**Exemplo de isolamento de ambientes**

**Projeto A**

Ambiente A

Bibliotecas instaladas

- Pandas 2.2
- NumPy 1.26
- Matplotlib 3.8

**Projeto B**

Ambiente B

Bibliotecas instaladas

- Pandas 3.0
- NumPy 2.0
- Requests

As dependências de cada ambiente são independentes.

Assim, instalar ou atualizar um pacote em um ambiente não altera automaticamente o pacote instalado no outro.

# **4. O que é o venv?**

O `venv` é um módulo nativo do Python utilizado para criar ambientes virtuais.

Não precisamos instalar uma biblioteca externa para utilizá-lo.

O comando para criar um ambiente virtual é:

```
python -m venv nome_do_ambiente
```

Vamos entender:

| Parte              | Significado                                     |
| ------------------ | ----------------------------------------------- |
| `python`           | Executa o interpretador Python                  |
| `-m`               | Executa um módulo como programa                 |
| `venv`             | Módulo responsável por criar ambientes virtuais |
| `nome_do_ambiente` | Nome da pasta do ambiente                       |

Por exemplo:

```
python -m venv venv
```

Esse comando cria uma pasta chamada `venv` contendo os arquivos necessários para o ambiente virtual.

# **5. Como ativar um ambiente virtual?**

Depois de criar o ambiente, precisamos ativá-lo para que os comandos Python e `pip` utilizem aquele ambiente.

O comando depende do sistema operacional e do terminal.

**Windows — Prompt de Comando (CMD):**

```
venv\Scripts\activate
```

**Windows — PowerShell:**

```
.\venv\Scripts\Activate.ps1
```

**Linux e macOS:**

```
source venv/bin/activate
```

Quando o ambiente estiver ativado, normalmente aparece o nome dele no início da linha do terminal.

Exemplo:

```
(venv) C:\projetos\meu_projeto>
```

Isso indica que o ambiente virtual está ativo.

# **6. Instalando bibliotecas dentro do ambiente virtual**

Com o ambiente ativado, podemos instalar bibliotecas normalmente:

```
pip install pandas
```

Nesse caso, o Pandas será instalado no ambiente virtual ativo, e não no ambiente global do Python.

Para conferir os pacotes instalados:

```
pip list
```

**Atenção:** sempre verifique se o ambiente virtual correto está ativado antes de instalar ou atualizar pacotes.

# **7. Como desativar um ambiente virtual?**

Quando terminarmos de trabalhar no ambiente, podemos desativá-lo utilizando:

```
deactivate
```

Depois disso, o terminal volta a utilizar o Python que estava disponível fora daquele ambiente.

Desativar não apaga o ambiente virtual nem desinstala seus pacotes.

# **8. O que é o requirements.txt?**

O `requirements.txt` é um arquivo utilizado para registrar as dependências de um projeto.

Imagine que seu projeto utiliza:

- Pandas 2.2.3
- NumPy 1.26.4
- Matplotlib 3.8.2

Podemos registrar essas dependências em um arquivo chamado `requirements.txt`:

```
pandas==2.2.3
numpy==1.26.4
matplotlib==3.8.2
```

Assim, outra pessoa pode instalar as mesmas versões utilizando:

```
pip install -r requirements.txt
```

O parâmetro `-r` indica que o pip deve ler os pacotes a partir de um arquivo.

Também podemos gerar automaticamente esse arquivo com:

```
pip freeze > requirements.txt
```

O `pip freeze` lista os pacotes instalados e suas versões. O símbolo `>` direciona essa lista para o arquivo `requirements.txt`.

Isso facilita compartilhar projetos e reproduzir seus ambientes.

# **Resumo geral**

| Conceito           | Função                             |
| ------------------ | ---------------------------------- |
| `pip`              | Gerenciador de pacotes             |
| `pip install`      | Instala bibliotecas                |
| `pip uninstall`    | Remove bibliotecas                 |
| `pip list`         | Lista pacotes instalados           |
| `pip show`         | Exibe informações de um pacote     |
| `venv`             | Cria ambientes virtuais            |
| `activate`         | Ativa um ambiente virtual          |
| `deactivate`       | Desativa um ambiente virtual       |
| `requirements.txt` | Registra as dependências           |
| `pip freeze`       | Lista pacotes e versões instaladas |
