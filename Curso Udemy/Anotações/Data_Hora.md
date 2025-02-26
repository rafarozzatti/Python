# Manipulação de Data e Hora em Python

Python oferece módulos poderosos para lidar com datas e horas, como `datetime`, `time` e `calendar`. Vamos explorar como utilizá-los de forma eficiente.

---

## **1. Obtendo a Data e Hora Atual**

Podemos usar o módulo `datetime` para obter a data e a hora atual:

```python
from datetime import datetime

# Obtendo a data e hora atual
agora = datetime.now()
print("Data e hora atual:", agora)
```

### **Saída:**
```
Data e hora atual: 2025-02-19 14:30:45.123456  # Exemplo de saída
```

---

## **2. Formatando Datas e Horas**

Podemos formatar a data e hora usando `strftime()`:

```python
# Formatando a data e hora
formatado = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", formatado)
```

### **Saída:**
```
Data formatada: 19/02/2025 14:30:45
```

Principais especificadores:
- `%d` -> Dia do mês
- `%m` -> Mês
- `%Y` -> Ano com 4 dígitos
- `%H` -> Hora (24h)
- `%M` -> Minutos
- `%S` -> Segundos

---

## **3. Convertendo String para Data**

Podemos converter uma string para um objeto `datetime` com `strptime()`:

```python
# Convertendo string para datetime
data_str = "25/12/2025 18:00:00"
data_obj = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
print("Objeto datetime:", data_obj)
```

### **Saída:**
```
Objeto datetime: 2025-12-25 18:00:00
```

---

## **4. Trabalhando com Diferença de Tempo**

Podemos calcular diferenças entre datas usando `timedelta`:

```python
from datetime import timedelta

# Criando um intervalo de 7 dias
delta = timedelta(days=7)

# Somando e subtraindo datas
nova_data = agora + delta
print("Daqui a 7 dias:", nova_data)

data_passada = agora - delta
print("7 dias atrás:", data_passada)
```

### **Saída:**
```
Daqui a 7 dias: 2025-02-26 14:30:45
7 dias atrás: 2025-02-12 14:30:45
```

---

## **5. Trabalhando com Fusos Horários**

O módulo `pytz` permite lidar com fusos horários:

```python
import pytz

# Definindo um fuso horário
fuso_br = pytz.timezone("America/Sao_Paulo")

# Obtendo a data e hora no fuso horário especificado
data_fuso = datetime.now(fuso_br)
print("Hora em São Paulo:", data_fuso.strftime("%d/%m/%Y %H:%M:%S"))
```

### **Saída:**
```
Hora em São Paulo: 19/02/2025 11:30:45  # Exemplo considerando UTC-3
```

---

## **6. Obtendo Dia da Semana**

Podemos determinar o dia da semana com `weekday()` (0 = segunda, 6 = domingo):

```python
# Obtendo o dia da semana
numero_dia = agora.weekday()
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
print("Hoje é:", dias[numero_dia])
```

### **Saída:**
```
Hoje é: Quarta  # Exemplo de saída
```

---

## **7. Trabalhando com o Calendário**

O módulo `calendar` permite verificar anos bissextos e exibir calendários completos:

```python
import calendar

# Verificando se um ano é bissexto
ano = 2024
print(f"O ano {ano} é bissexto?", calendar.isleap(ano))

# Exibindo um mês do calendário
print(calendar.month(2025, 2))
```

### **Saída:**
```
O ano 2024 é bissexto? True
   Fevereiro 2025
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28
```

---

## **Conclusão**

Manipular datas e horas em Python é essencial para qualquer aplicação que lide com registros, logs e agendamentos. O uso correto das bibliotecas `datetime`, `time`, `calendar` e `pytz` facilita o trabalho com fusos horários, formatações e cálculos de tempo.
