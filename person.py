import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

if mydb.is_connected():
    print("Connection successful!")
else:
    print("Connection failed.")

mycursor = mydb.cursor()

while True:
    id = input("Enter id (or type 'exit' to quit).... ")
    if id.lower() == 'exit':
        print("exiting the loop....")
        break

    name = input("Enter  name: ")
    score = input("Enter score: ")
    city = input("Enter city: ")

    mycursor.execute("insert into person (id, name, score, city) VALUES (%s, %s, %s, %s)", (id, name, score, city))
    mydb.commit()
    print(f"Name {name} with ID {id} inserted successfully.")

id_to_delete = input("Enter ID to delete: ")
mycursor.execute("delete from person where id = %s", (id_to_delete,))
mydb.commit()
print(f"person with ID {id_to_delete} deleted successfully.")

print("Update person details. Give ID and details to update.")
id_to_update = input("Enter ID to update: ")
name_to_update = input("Enter name: ")
score_to_update = input("Enter score: ")
city_to_update = input("Enter city: ")

mycursor.execute("update person set name = %s, score = %s, city = %s where id = %s", (name_to_update, score_to_update, city_to_update, id_to_update))
mydb.commit()
print(f"person with ID {id_to_update} updated successfully.")

mycursor.execute("select * from person")
result = mycursor.fetchall()
print("\nMembers:")
for row in result:
    print(row)

mycursor.execute("select * from person order by name ASC")
_sorted = mycursor.fetchall()
print("\nPersons sorted by name:")
for p in _sorted:
    print(p)

mycursor.execute("select * from person where score between 70 AND 90")
score_range = mycursor.fetchall()
print("\nPerson with score between 70 and 90:")
for a in score_range:
    print(a)

mycursor.execute("select * from person where city = 'Hyderabad'")
hyderabad = mycursor.fetchall()
print("\nPerson from Hyderabad:")
for b in hyderabad:
    print(b)
mydb.commit()

