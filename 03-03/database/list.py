# try:
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="khamditika26")

# except Exception as e:
    # print(e)

curs = conn.cursor()
query = f"select * from siswa"
curs.execute(query)
data = curs.fetchall()

for d in data:
    print("name:", d[0], "umur:", d[1])