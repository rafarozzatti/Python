import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2026, 2, 17, 0)
tempo_para_evento = aniversario - data_hoje
print(tempo_para_evento)
print(f'Fatam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 3600} horas...')
print()

data_compra = data_hoje
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento = data_compra + regra_boleto
print(vencimento)
