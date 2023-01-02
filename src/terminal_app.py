print('starting app')
   
from flask import Flask, jsonify
from patient_func import patients_menu, db

app = Flask(__name__)

@app.route("/")
def present_data():
  #data = open('src/patients_db.json')
  return db.all() #json.load(data)

if __name__ == "__main__":
    choice= ''
    while True:
      print('')
      print("0- return to Main Menu ")
      print("1- Access patient's menu ")
      print("2- Run flask app on local host ")

      choice= input("Enter option: ")
      choice=choice.strip()
    
      if choice=='1':
        patients_menu()
      if choice=='2':
        app.run(host='0.0.0.0')
      elif choice=='0':
        break
      else:
        print('invalid choice, please try again')

from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="password",
  database="patient_db"
)

@app.route('/create_patient', methods=['POST'])
def create_patient():
  # Get the patient's name and age from the request body
  name = request.form['name']
  age = request.form['age']

  # Create a cursor object
  cursor = mydb.cursor()

  # Insert the patient into the database
  query = "INSERT INTO patients (name, age) VALUES (%s, %s)"
  values = (name, age)
  cursor.execute(query, values)

  # Commit the changes to the database
  mydb.commit()

  # Close the cursor and connection
  cursor.close()
  mydb.close()

  return "Successfully created patient with name {} and age {}".format(name, age)

@app.route('/get_patient/<int:id>', methods=['GET'])
def get_patient(id):
  # Create a cursor object
  cursor = mydb.cursor()

  # Retrieve the patient from the database
  query = "SELECT * FROM patients WHERE id = %s"
  values = (id,)
  cursor.execute(query, values)
  patient = cursor.fetchone()

  # Close the cursor and connection
  cursor.close()
  mydb.close()

  # Return the patient's information as a JSON object
  return {
    "id": patient[0],
    "name": patient[1],
    "age": patient[2]
  }

@app.route('/update_patient/<int:id>', methods=['POST'])
def update_patient(id):
  # Get the patient's name and age from the request body
  name = request.form['name']
  age = request.form['age']

  # Create a cursor object
  cursor = mydb.cursor()

  # Update the patient's information in the database
  query = "UPDATE patients SET name = %s, age = %s WHERE id = %s"
  values = (name, age, id)
  cursor.execute(query, values)

  # Commit the changes to the database
  mydb.commit()

  # Close the cursor and connection
  cursor.close()
  mydb.close()

  return "Successfully updated patient with ID {}".format(id)

@app.route('/delete_patient/<int:id>', methods=['DELETE'])
def delete_patient(id):
  # Create a cursor object
  cursor = mydb.cursor()

  # Delete the patient from the database
  query = "DELETE FROM patients WHERE id = %s"
  values = (id,)
  cursor.execute(query, values)

  # Commit the changes to the database
  mydb.commit()

