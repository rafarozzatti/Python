### Documentação do Código do Projeto de Mercado

#### **mercado.py**
Este é o arquivo principal do sistema, responsável pelo fluxo do programa e interação com o usuário.

**Principais funcionalidades:**
- Menu principal para navegar entre as opções.
- Cadastro de produtos.
- Listagem de produtos cadastrados.
- Adição de produtos ao carrinho.
- Visualização do carrinho.
- Fechamento do pedido.

##### **Explicação das Funções:**
- `menu()`: Exibe as opções para o usuário.
- `cadastrar_produto()`: Solicita nome e preço do produto e o adiciona à lista de produtos.
- `listar_produto()`: Exibe todos os produtos cadastrados.
- `comprar_produto()`: Adiciona um produto ao carrinho com base no código.
- `visualizar_carrinho()`: Mostra os produtos que estão no carrinho.
- `fechar_pedido()`: Calcula o total do pedido e finaliza a compra.
- `pega_produto_por_codigo()`: Retorna um produto com base no código informado.

##### **Saída esperada:**
```
==============================
======== Bem-Vindo(a) ========
======= Rozzatti Shop ========
==============================
Selecione uma opção abaixo:
1 - Cadastrar protuto
2 - Listar protuto
3 - Comprar protuto
4 - Visualizar carrinho
5 - Fechar pedido
6 - Sair do sistema
```

---

#### **teste.py**

Este arquivo cria duas instâncias da classe `Produto` e imprime suas representações.

##### **Saída esperada:**
```
Código: 1
Nome: PlayStation 5
Preço: R$ 3499.99
Código: 2
Nome: Cadeira Gamer
Preço: R$ 2499.99
```

---

#### **models/produto.py**

Este módulo define a classe `Produto`, que representa um produto cadastrado.

##### **Principais atributos e métodos:**
- `codigo`: Identificador único do produto.
- `nome`: Nome do produto.
- `preco`: Preço do produto.
- `__str__()`: Retorna uma representação textual do produto.

---

#### **utils/helper.py**

Este módulo define funções auxiliares para o sistema.

##### **Funções:**
- `formata_float_str_moeda(valor: float) -> str`: Formata um número float para o formato monetário brasileiro.

##### **Saída esperada:**
```python
formata_float_str_moeda(10.5) # Retorna "R$ 10.50"
```

---

### **Resumo Final**
O projeto implementa um sistema simples de mercado com cadastro de produtos, carrinho de compras e fechamento de pedido. As funções são bem distribuídas entre os arquivos para garantir modularização e reutilização de código.
