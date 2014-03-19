import sqlite3

# create a connection to the sqlite3 database file
conn = sqlite3.connect("cripper.db")

# script string to create the run history table
createRunTableString = "CREATE TABLE run_history (run_id integer, run_date_time text, base_path text)"

# script string to create the file table
createFileTableString = "CREATE TABLE file (run_id integer, file_name text, file_path text)"

# create a cursor object from the conn connection
c = conn.cursor()

# execute the table creation strings
c.execute(createRunTableString)
c.execute(createFileTableString)

# commit changes
conn.commit()

# close connection string
conn.close