try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="khamditika26")

    curs = conn.cursor()

    namaLama = "angga"
    
    namaBaru= "anggang"
    umurBaru= 24
    query = f"update siswa set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)
