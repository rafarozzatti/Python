def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Modelo válido, pois modelo, ano e marca não podem receber parametro
criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

# Modelo inválido, pois modelo, ano e marca não podem receber parametro
criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')
