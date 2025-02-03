def data_por_extenso(data_str):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    dia, mes, ano = data_str.split("/")
    mes_extenso = meses[int(mes) - 1]
    
    print(f"{int(dia)} de {mes_extenso} de {ano}")


data_por_extenso("17/02/2025")
