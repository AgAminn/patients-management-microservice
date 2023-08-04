print('starting app')

import os
cwd = os.getcwd()
# Change the current working directory
#os.chdir('./src')
print(os.getcwd())
from flask import Flask, jsonify, request
from src.patient_func import patient_menu, db

app = Flask(__name__)

@app.route("/")
def present_data():
  #data = open('src/patients_db.json')
  return db.all() #json.load(data)

@app.route('/create_patient/', methods=['POST'])
def create_patient():
    # Get the patient's name and age from the request body
    print('getting request / json object with opulated args')
    req = request.get_json()
    id = req['id']
    name = req['name']
    diagnosis = req['diagnosis']
    age = req['age']
    PatientL = patient_menu(id=id,name=name,diagnosis=diagnosis,age=age) 
    PatientL.add_patient()
    return "Successfully created patient with name {} and age {} and id {} and diagnosis {} ".format(name, age, id, diagnosis)

@app.route('/update_patient/<int:id>', methods=['POST'])
def update_patient(id):
  print(' updateing patient: getting id and args in body')
  print('id ',id)
  req = request.get_json()
  name = req['name']
  print('name ', name)
  diagnosis = req['diagnosis']
  print(diagnosis)
  age = req['age']
  print(id, name, age, diagnosis)
  PatientL = patient_menu(id=id,name=name,diagnosis=diagnosis,age=age) 
  result = PatientL.edit_patient(id=id)
  if result == 'Invalid ID request':
    return result
  return "Successfully updateded patient with id {} , name {} , age {} and diagnosis {} ".format(name, age, id, diagnosis)

@app.route('/delete_patient/<int:id>', methods=['DELETE'])
def delete_patient(id):
  PatientL = patient_menu() 
  result = PatientL.remove_patient(id=id)
  return result

@app.route('/get_patient/<int:id>', methods=['GET'])
def get_patient(id):
  PatientL = patient_menu() 
  p= PatientL.display_patient(id=id)
  return p #json.load(data)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)




'''
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

'''
