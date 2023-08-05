# papysql

### if you download the folder the main functions are located in papysql.py file, you can import them in a script by directly importing that papysql.py.

This Library is an interface between Pandas and sqlite3. It gives the possibility to access sql databases.

After importing the library it have to read the database with the command
```
import papysql as pps

db = pps.read(PathToDb)

```

Following this we can access data in the db with functions list_tables and display_table e.g.


```
pps.display_tables(db)
#It lists all the tables in the database

pps.display_table(NameOfTheTable,db)
#It returns the specific table in format of a Pandas Dataframe Object

```
Finally the Function ExecuteScriptFromFile is work in progress and serves to execute a SQL script from a text file

Future implementation will be aimed at modify and creating tables
