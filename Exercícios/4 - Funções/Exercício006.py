"""Crie uma função chamada pedido que receba um nome de cliente (parâmetro posicional obrigatório), uma lista de itens do pedido (*args) e informações adicionais do pedido (**kwargs)."""

def pedido(nome, *args, **kwargs):
    print(f'Cliente: {nome}')
    if args:
        print(f'Itens do pedido: {", ".join(args)}')
    
    if kwargs:
        detalhes = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(f'Detalhes adicionais: {detalhes}')

pedido("Rafael", "Pizza", "Refrigerante", "Sobremesa", entrega="Sim", pagamento="Cartão")
