
# Pandas

Pandas é uma biblioteca do Python utilizado para analise e tratamento de dados.


# Series e Dataframes




# Métodos de Dataframe

dados.info():
dados.shape():
dados.head(): 


## GroupBy

- Permite agrupar uma determinada serie/coluna de um dataframe, assimo como no sql tambem precisamos de um função de agregação (sum,mean(média))

- Podemos agrupar informações e trazer valores de multiplas colunas ou apenas uma especifica ['Valor'],['Quantidade'] por exemplo

```{python}

groupby('Animal').sum(numeric_Only=True) #usamos esse parametro no sum caso não especificarmos uma coluna numerica



```


```{python}

groupby('Animal')[['Quantidade]].sum() ## incluindo [[]] criamos um DF

            Qtd
Animal      
A            30
B            40
C            10
```




