#função update 

update table 

set fields = value, field = value
    
where 

def update (sets, table, where = None):

        global c, con

        query = "UPDATE " + table
        query = query + "SET " + ",".join([fields + "=" for fields, value in sets.items()])

        if(where):
            query = query + "WHERE " + where

        c.execute(query)
        con.commit()
      
update({"nome":"Arthur José","cidade": "São Gonçalo"}, "alunos")
