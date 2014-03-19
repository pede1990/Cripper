from os import walk
from datetime import datetime
import sqlite3

# We need to get a base directory to begin or search from.
# Since we are going to be using this in house we will always
# be using the same directory to begin and thus it is hard
# coded. In the future the program could be updated to handle
# tracking of multiple directories (each would need its own DB
# or a new key field in the run_history table to tell what
# starting directory was used for splitting the data set
# during comparisons).

# Should be converted to use a config file for the path and DB

# Base directory for our home use
base_path = "\\FREENAS\NAS"

# open a connection to our database file
conn = sqlite3.connect("data\cripper.db")

# get cursor
c = conn.cursor()

# get the run_id we will be using
c.execute("select ifnull(count(run_id), 0) as count from run_history;")

# last used run id
run_id = c.fetchone()

# increment run_id to the next available
if run_id[0] == 0:
  run_id = 1
else:
  run_id = run_id[0] + 1

# get the date time string formatted for this entry
date_time = datetime.now()

# insert a record in the run history table
c.execute("insert into run_history (run_id, run_date_time) values ({0}, '{1}');".format(str(run_id), date_time))

for root, dirs, files in walk(base_path):
  for file in files:
    c.execute("insert into file (run_id, file_name, file_path) values ({0}, '{1}', '{2}');".format(run_id, str(file), str(root)))

conn.commit()
conn.close()