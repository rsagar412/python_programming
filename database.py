import sqlite3

#connect to the database
# conn = sqlite3.connect('customer.db')

#create a cursor object that will actually interact with the database. It will query our DB.
# c = conn.cursor()

# c.execute("""
# 	CREATE table Family(
# 		first_name text,
# 		last_name text,
# 		addr text)
# 	""")
# c.execute("INSERT into Family values ('Sagar', 'Rathod', 'Boisar')")
# c.execute("INSERT into Family values ('Ankita', 'Rathod', 'Boisar')")
# c.execute("INSERT into Family values ('Mom', 'Rathod', 'Boisar')")
# c.execute("INSERT into Family values ('Dad', 'Rathod', 'Boisar')")


#display all the records in a table
def show_all():
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
# c.execute("DELETE from Family where rowid = 2")
	c.execute("SELECT rowid, * from Family")
	for valuesvar in c.fetchall():
		print(valuesvar)
	conn.commit()
	conn.close()


#add a new record to the table
def add_newrecord(fname, lname, addr):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT into Family values (?, ?, ?)", (fname, lname, addr))
	conn.commit()
	conn.close()


#delete a record from the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM Family WHERE rowid = (?)", id)
    conn.commit()
    conn.close()


#create a table. I am creating it using a docstring triple quote which helps
#me to write code in multiple lines. The single/double quotes allows us to
#write the code only in a single line

# c.execute("""        
# CREATE TABLE customers(
# first_name text,
# last_name text,
# email text)
# 	""")

#inserting values in the above table
# c.execute("INSERT INTO customers VALUES ('Samantha', 'Prabhu', 'sam.prabhu23@yahoo.com')")
# #commiting/saving the connection with the above program


#adding many customers at the same time
# many_customers = [  
# 					('Wes', 'Brown', 'abc@gmail.com'), 
# 					('Sam', 'Mike', 'sbm@gmail.com'),
# 					('Love', 'Preet', 'lpu@gmail.com')
# 				]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#updating the records
# c.execute("""
# UPDATE customers SET first_name = 'Bob' 
# WHERE last_name = 'Mike'
# 	""")

#deleting the records


#drop the table/basicall it will delete the table
# c.execute("DROP table customers")
# conn.commit()

#retrieve the records from the DB, this step is important in order to pull
#the table into the memory before we run the SELECT query.  
# c.execute("SELECT rowid, * from customers")   
# c.execute("SELECT rowid, * from customers ORDER BY last_name DESC limit 4")   
# c.execute("SELECT * from customers where email like '%@yahoo.com' or first_name = 'Sagar'")    #AND, like 
# print(c.fetchone()[1])
# c.fetchmany(3)



# print("command executed successfully...\n")

# items = c.fetchall()
# for item in items:
# 	print(item)
# 	# print(item[0] + " " + item[1] + "\t" + item[2])



# #close our connection
# conn.close()