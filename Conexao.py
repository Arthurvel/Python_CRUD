#criando uma conexão entre o banco e o python
import MySQLdb
from turtle import update


host = "localhost"
user = "aplicacao"
password = "1234"
db = "escola_curso"
port = 3306

#variavél que vai receber um objeto de conexão 
con = MySQLdb.connect(host, user, password, db, port)

#iniciando o crud 

#Registros
 
c = con.cursor()