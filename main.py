import sqlite3
import pandas as pd
from pathlib import Path
import shutil


db = sqlite3.connect("assets/64/assets.db")
df = pd.read_sql_query("SELECT * from assets", db)
#breakpoint()

a = df.to_dict('records')
#cnt = 0
for i in a:
    Path("new_assets/" + "/".join(i['logic'].split("/")[:-1])).mkdir(parents=True, exist_ok=True)
    if(Path("new_assets/" + i['logic']).is_file()):
        print(i['logic'])
    shutil.copyfile("assets/" + i['real'], "new_assets/" + i['logic'])