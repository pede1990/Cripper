from os import walk
from datetime import datetime
import sys
import sqlite3
import xml.etree.ElementTree as ET

# extract the data from the config file
config_data = ET.parse("config.xml")
root = config_data.getroot()

# declare our base path and database file path variables
base_path = ""
database_file = ""

# from the root of the xml, get the setting values we need
for child in root:
  if child.tag == "base_dir":
    base_path = child.text
  elif child.tag == "database_file":
    database_file = child.text

# make sure the db file and base path were both found
if len(base_path) == 0 or len(database_file) == 0:
  sys.exit("Unable to load config file. Closing")

# connect to the database file
conn = sqlite3.connect(database_file)

# get cursor
c = conn.cursor()

# get the run_id we will be using
c.execute("select ifnull(max(run_id), 0) as count from run_history;")

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
c.execute("insert into run_history (run_id, run_date_time, base_path) values ({0}, '{1}', '{2}');".format(str(run_id), date_time, base_path))

for root, dirs, files in walk(base_path):
  for file in files:
    c.execute("insert into file (run_id, file_name, file_path) values ({0}, '{1}', '{2}');".format(run_id, str(file), str(root)))

conn.commit()
conn.close()