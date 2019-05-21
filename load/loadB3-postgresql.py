import psycopg2
conn = psycopg2.connect("host=127.0.0.1 dbname=projetotcc user=postgres password=123456")
cur = conn.cursor()
cur.execute("truncate dadosb3;")
with open('/twitter/tccbi17/load/bmf_load.csv', 'r') as f:
# Notice that we don't need the `csv` module.
    #next(f) # Skip the header row.
    cur.copy_from(f, 'dadosb3', sep=',')
conn.commit()