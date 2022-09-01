try:
    
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="khamditika26")

    curs = conn.cursor()

    nama = "angge"
    umur = 22
    query = f"insert into siswa(nama, umur) values('{nama}', {umur})"
    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print(e)
