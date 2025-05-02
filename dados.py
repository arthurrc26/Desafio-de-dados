import pandas as pd
from datetime import datetime

df = pd.read_excel("C:/Users/arthu/VS codes/citi/desafio dados/Base_despadronizada.xlsx")

def padronizar_sexo(valor):
    valor = str(valor) # garante que é lido como string
    if valor != 'Masculino' and (valor[0]=='m' or valor[0]=='M'):
        return 'Masculino'
    elif valor != 'Feminino' and (valor[0]=='f' or valor[0]=='F'):
        return 'Feminino'
    return valor

def padronizar_nota(valor):
    # se for datetime, faz no formato dia,mes
    if isinstance(valor, datetime):
        dia = valor.day
        mes = valor.month
        return f"{dia},{mes}"
    
    # nota já formatada
    if isinstance(valor, str) and ',' in valor:
        return valor
    
    # string x.x ou string x
    if isinstance(valor, str):
        if '.' in valor:
            return valor.replace('.', ',')
        else:
            valor = valor + ',' + '0'
            return valor
    
    # float x.x ou um inteiro x
    # float x.x nem seria necessario ja que essa conversao é feita automaticamente
    if isinstance(valor, (float, int)):
        return f"{valor:.1f}".replace('.', ',')
    

def converter_para_float(valor):
    if isinstance(valor, str):
        return float(valor.replace(',', '.'))
    return float(valor)

def aprovado(valor):
    if valor >= 7:
        return "Sim"
    else:
        return 'Não'

#padronizações
df['sexo'] = df['sexo'].apply(padronizar_sexo)
df['nota_matematica'] = df['nota_matematica'].apply(padronizar_nota)
df['nota_portugues'] = df['nota_portugues'].apply(padronizar_nota)

#cria colunas temporarias em tipo float para calculo de media e aprovacao
df['nota_matematica_float'] = df['nota_matematica'].apply(converter_para_float)
df['nota_portugues_float'] = df['nota_portugues'].apply(converter_para_float)

# calculo da media e sua padronizacao
df['Media'] = (df['nota_matematica_float'] + df['nota_portugues_float'] + (df['frequencia'] / 10)) / 3
df['Media'] = df['Media'].apply(padronizar_nota)

# cria coluna temporaria media em tipo float
df['Media_float'] = df['Media'].apply(converter_para_float)

#coluna de aprovado de acordo com a media
df['aprovado'] = df['Media_float'].apply(aprovado)

#exclui colunas temporarias
df = df.drop(['nota_matematica_float', 'nota_portugues_float', 'Media_float'], axis=1)

#output do arquivo final padronizado de acordo com o pedido no desafio
df.to_excel('Base_padronizada.xlsx')

print('fim')