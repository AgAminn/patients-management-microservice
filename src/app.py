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

