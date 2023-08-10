#select 

def select (fields, tables, where = None):

    #essa variavel indica que o c é a veriavél que está lá fora, ou seja uma var global 
    global c

    query = "SELECT" + fields + "FROM" + tables 

    if(where):
        query = query + "WHERE" + where 

    c.execute(query)
    #pega todos os resultados dessa execução anterior e retorna nessa função 

    return c.fetchall()

result = (select("nome","curso"))

print(result)