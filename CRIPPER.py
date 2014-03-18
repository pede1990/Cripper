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

# Base directory for our home use
base_path = "//FREE-NAS/NAS/"

# open a connection to our database file
conn = sqlite3.connect("data/example.db")

# get cursor
c = conn.cursor()

# get the run_id we will be using
c.execute("SELECT * FROM run_history")

# last used run id
run_id = c.rowcount()

# increment run_id to the next available
if run_id = -1
run_id = run_id + 1

# get the date time string formatted for this entry
date_time = datetime.now()

# insert a record in the run history table
c.execute("INSERT INTO run_history (run_id, run_date_time) VALUES (%d, %s)" % run_id, date_time)

for root, dirs, files in walk(base_dir):
  for file in files:
    c.execute("INSERT INTO files (run_id, file_name, file_path) VALUES (%d, '%s', '%s')" % run_id, file, root)