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
query = f"select * from siswa where nama='angga'"
curs.execute(query)
data = curs.fetchone()
if not data:
    print("gak ada")
else:
    print("nama:", d[0], "umur:", d[1])