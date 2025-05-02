Desafio de dados

função para padronizar o sexo: 
Ao invés de utilizar uma lista (por exemplo, if valor in [“m”, “masc”, “masculino”]), quis ser o mais abrangente possível, trocando por Masculino quando a palavra começar com m, seja maiúsculo ou minúsculo, o mesmo para Feminino.

função para padronizar nota:
Aqui, analisando os tipos de dados da planilha, encontrei 4 casos possíveis:

tipo datetime: número é lido no formato dia, mês. Apenas atribui os respectivos as variáveis dia e mês e retornar a string final no formato dia,mês. Ex: 8.1 -> 8,1

tipo string já no formato desejado: retorna a própria string, não muda nada

tipo string no formato “número.número” ou apenas “número”: caso “.” esteja na string, significa que é o formato x.x, então é apenas dar replace no “.” por “,”. Caso contrário, é o formato x, então é apenas adicionar “,” e 0 ao seu final

tipo float x.x ou inteiro sozinho: insere limite de uma casa decimal, dá replace no “.” por “,” e transforma em string


Aplicação das funções de padronização acima na coluna de sexo e nas 2 de nota

Para criar a coluna de média, primeiro criei duas colunas temporárias das notas em tipo float com ajuda de uma função de converter string em float (simplesmente muda , por . e muda o tipo). Com o valor em tipo float, é possível realizar operações matemáticas e calcular a média de acordo com a fórmula dada, criando uma nova coluna e atribuindo os respectivos resultados.

Para a coluna de aprovado, apliquei a mesma função de conversão para float na coluna média, criando uma coluna Media_float temporária, e sobre ela aplicar que se estiver maior ou igual a 7 retorna um sim, caso contrário retorna um não e colocar os respectivos resultados em uma nova coluna “aprovado”.

No final, apagar todas as colunas temporárias criadas e retornar o arquivo excel com as alterações feitas
