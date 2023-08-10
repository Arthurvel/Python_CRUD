#função delete 

def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + "WHERE " + where

    c.execute(query)
    con.commit()