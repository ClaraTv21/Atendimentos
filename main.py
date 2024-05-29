import pandas as pd
import numpy as np


#fhfnfj
#TABELA REPETIÇÃO
#lê a planilha do excel e inicializa ela como data frame
df = pd.read_excel("relatorio8.xlsx")

#conta quantas vezes o mesmo nome aparece na coluna Login
contagem = df["Login"].value_counts()

#cria um outro df com as informações de login, técnico e fechamento da tabela inicial, caso a contagem seja maior que 1
nomes_repetidos = contagem[contagem > 1].index.tolist()
df_tabela_repeticao = df[df['Login'].isin(nomes_repetidos)][['ID', 'Login', 'Colaborador', 'Fechamento', 'Diagnóstico']]

# adiciona uma coluna com o índice referente a cada login em ordem crescente
df_tabela_repeticao['Índice'] = df_tabela_repeticao.groupby('Login')['Fechamento'].rank(method='first', ascending=False)

#ordena as células de login por ordem alfabética e fechamento por data
df_tabela_repeticao.sort_values(by=['Login', 'Fechamento'], inplace=True)

# Reverte a ordem das linhas
df_tabela_repeticao = df_tabela_repeticao[::-1]

# reseta os índices em ordem decrescente
df_tabela_repeticao.reset_index(drop=True, inplace=True)

#ordena as células de login por ordem alfabética e fechamento por data
df_tabela_repeticao.sort_values(by=['Login', 'Fechamento'], inplace=True)
#ACIMA FUNCIONA

# filtra os registros com índice maior que 1 (não são os primeiros atendimentos)
df_nao_primeiros_atendimentos = df_tabela_repeticao.query('Índice > 1')

# conta a frequência de cada colaborador nos registros filtrados (indices maiores que 1)
contagem_colaboradores = df_nao_primeiros_atendimentos["Colaborador"].value_counts()

#cria um data frame com uma coluna para os técnicos e uma para a quantidade de vezes que eles aparecem
df_tecnicos_repetidos = pd.DataFrame({'Colaborador': contagem_colaboradores.index, 'Frequência': contagem_colaboradores.values})


#exporta as dfs para um novo arquivo excel
df_tabela_repeticao.to_excel("atendimentos_repetidos.xlsx", index=False)
df_tecnicos_repetidos.to_excel("tecnicos_repetidos.xlsx", index=False)


























#indice_tecnico = df_tabela_repeticao['Índice']
#tecnicos_repetidos = indice_tecnico[indice_tecnico>1].index.tolist()
#df_tecnicos_repetidos = df_tabela_repeticao[df_tabela_repeticao['Índice'].isin(indice_tecnico)][['Colaborador']]
#df_tecnicos_repetidos = pd.DataFrame({'Colaborador': indice_tecnico.index, 'Frequência': indice_tecnico.values})

# Filtra os registros com índice diferente do maior (não são os últimos atendimentos)
#if ['Login'].Índice < ['Login'].Índice.max():
    #df_nao_ultimos_atendimentos = df_tabela_repeticao['Login', 'Colaborador']

# Conta a frequência de cada técnico nos registros filtrados
#contagem_tecnicos = df_nao_ultimos_atendimentos["Colaborador"].value_counts()
#df_tecnicos_repetidos = pd.DataFrame({'Colaborador': contagem_tecnicos.index, 'Frequência': contagem_tecnicos.values})


#ordena o df criado por ordem de Login e data de fechamento, nessa ordem
#df_tabela_repeticao.sort_values(by=['Login', 'Fechamento'], inplace=True)

#TABELA TÉCNICOS

#exporta as dfs para um novo arquivo excel

#teste
#indices_ultimos_atendimentos = df_tabela_repeticao.groupby('Login').tail(1).index
#df_tecnicos_repetidos = df_tabela_repeticao[~df_tabela_repeticao.index.isin(indices_ultimos_atendimentos)]
#teste

#teste - os tecnicos responsaveis pelo primeiro atendimento
#df_primeiros_atendimentos = df_tabela_repeticao.query('Índice != Índice.max()')
#teste

#teste - os tecnicos responsaveis pelo primeiro atendimento
#ERRO: precisa ser dinamico, ou seja, armazenar o de todos que não são o último
#df_primeiros_atendimentos = df_tabela_repeticao.query('Índice == 1')
#teste

#conta quantas vezes o mesmo tecnico aparece na nova tabela de tecnicos repetidos
#contagem_tecnicos = df_nao_ultimos_atendimentos["Colaborador"].value_counts()

#adiciona na tabela uma coluna com a quantidade de vezes que o mesmo colaborador aparece 
#df_tecnicos_repetidos = pd.DataFrame({'Colaborador': contagem_tecnicos.index, 'Frequência': contagem_tecnicos.values})

#TESTE
# Remove os registros em que o técnico é o último a atender o cliente
#indices_ultimos_atendimentos = df_tabela_repeticao.groupby('Login').tail(1).index
#df_nao_ultimos_atendimentos = df_tabela_repeticao[~df_tabela_repeticao.index.isin(indices_ultimos_atendimentos)]

# Agrupa por login e coleta todos os colaboradores exceto o último em cada grupo
#df_tecnicos_repetidos = df_nao_ultimos_atendimentos.groupby('Login')['Colaborador'].apply(list).reset_index()
#df_tecnicos_repetidos.columns = ['Login', 'Colaboradores']
#TESTE