import matplotlib.pyplot as plt

# Dados da tabela
respostas = ['SIM', 'NÃO', 'INCOMPLETO', 'SIM', 'SIM', 'SIM', 'NÃO', 'SIM', 'INCOMPLETO', 'SIM', 'SIM', 'SIM', 'NÃO']

# Contagem das respostas
contagem_respostas = {
    'SIM': respostas.count('SIM'),
    'NÃO': respostas.count('NÃO'),
    'INCOMPLETO': respostas.count('INCOMPLETO')
}

# Dados para o gráfico de pizza
labels = contagem_respostas.keys()
sizes = contagem_respostas.values()
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)  # explode a fatia 'SIM'

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equaliza o gráfico de pizza

# Título do gráfico
plt.title('Distribuição das Respostas da Tabela')

# Exibindo o gráfico
plt.show()
