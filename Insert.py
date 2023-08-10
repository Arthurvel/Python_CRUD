#função insert

def insert (values, table, fields = None):

    #var global 

    global c, con

    query = "INSERT INTO" + table 

    #verifica se fields foi passado corretamente 

    values (...), (...),


    if (fields):

        query = query + "(" + fields + ")"

        query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

        c.execute(query)
        con.commit()

    values = [
        "DEFALUT, 'Arthur José', '2001-07-09, 'Rua Maria Batista da Costa, 151', 'São Gonçalo', 'RJ', '12345678911'"
        "DEFALUT, 'Ciro José', '2001-07-09, 'Rua Maria Batista da Costa, 151', 'São Gonçalo', 'RJ', '12345678912'"
        ]
    
    insert (values, "alunos" )
    print (select("*", "alunos"))
