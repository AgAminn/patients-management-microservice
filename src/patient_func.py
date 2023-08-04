'''
These classes are helpers for setters functions
Functions to edit :
 - Patient data entries
 - #doctors data (future addition)
 - ...
'''
import os.path
from tinydb import TinyDB, Query
from src.patient import Patient

#database initialisation
# load dataset TinyDB tbale
db = {}
if os.path.exists("src/patients_db.json"):
  db = TinyDB("src/patients_db.json")


def to_dic(obj):
  '''
    dic = {
            "ID": obj.id,
            "Name": obj.name,
            .
            .
            .
          }
  '''
  dic = obj.__dict__
  keysedit = [k[1:] for k in dic.keys()]
  return dict(zip(keysedit, list(dic.values())))

class patient_edit:
    '''setter for patient attributes'''
    def __init__(self, name=None,diagnosis=None,age=None, id=None):
        self._name = name
        self._diagnosis = diagnosis
        self._age = age
        self._id = id
    
    def set_age(self):
        #check default value if not none
        if self._age !=None:
            if isinstance(self._age, int):
                return self._age
        while True:
            try:
                age = int(input("Please enter patient Age: "))
                if  age<0:
                    #raise ValueError('system accepts only positve integers')
                    print('age should be positve integer, try again')
                    continue
            except ValueError:
                print("Sorry, Invalid Input")
                continue
            else:
                return age
                #break
    
    def set_id(self):
        patient_ids  = [p['id'] for p in db]
        if self._id !=None:
            if isinstance(self._id, int):
                return self._id
        while True:
            try:
                id = int(input("Please enter patient ID: "))
                if id in patient_ids and patient_ids!=[]:
                    print('ID already exist')
                    continue
            except ValueError:
                print("Sorry, Invalid Input or ID already exist")
                continue
            else:
                return id
    
    def set_name(self):
      if self._name !=None:
        if (self._name).isalpha()==True :
          return self._name
      while True:
        try:
          name = input("Please enter patient Name: ")
          if name.isalpha()==False:
            raise ValueError('please use a-z characters')
        except ValueError:
          print("Sorry, Invalid Input")
          continue
        else:
          return name.capitalize()
    
    def set_diagnosis(self):
      if self._diagnosis != None:
        return self._diagnosis
      while True:
        try:
          diagnosis = input("Please enter patient diagnosis: ")
          #if name.isalpha()==False:
          #  raise ValueError('please use a-z characters')
        except ValueError:
          print("Sorry, Invalid Input")
          continue
        else:
          return diagnosis.capitalize()

class patient_menu:
  def __init__(self,name=None,diagnosis=None,age=None, id=None):
     self.query = Query()
     self.patient_edit = patient_edit(name=name,diagnosis=diagnosis,age=age, id=id)
  
  def display_patient(self,id=None):
    '''
    display one patient data
    input : id
    output : print and return patient data (type tinydb table object)
    '''
    def query_id(id):
      q = db.get(self.query.id==id)
      print(q)
      return q

    patient_ids  = [p['id'] for p in db]
    if id !=None:
      if isinstance(id, int) and (id in patient_ids):
          return query_id(id)
      else:
        return 'Invalid ID request'
          
    while True:
      try:
          id = int(input("Please enter patient ID: "))
          if id not in patient_ids:
              print('ID does not exist')
              continue
      except ValueError:
          print("Sorry, Invalid Input or ID already exist")
          continue
      else:
          return query_id(id)
  
  def display_all_patients(self):
    '''
    Display the patients database
    input: none
    output: print all data and return list of patients dict
    '''
    #print(pd.DataFrame(self.patients))
    for p in db.all():
      print(p)
    #print(db.all())
    return db.all()

  def add_patient(self):
    '''
    add new patient data
    the inpput are queried one by one
    output: populated patient object
    '''
    patient = Patient()
    patient.id = self.patient_edit.set_id()
    patient.name=self.patient_edit.set_name()
    patient.diagnosis= self.patient_edit.set_diagnosis()
    patient.age = self.patient_edit.set_age()
    db.insert(to_dic(patient))
    return patient
  
  def edit_patient(self,id=None):
    '''
    edit data single data entry
    input : id
    output : diplayed edited data and return populated patient object
    '''
    patient_ids  = [p['id'] for p in db]
    if id !=None:
      if (isinstance(id, int) and (id in patient_ids)) == False:
        return 'Invalid ID request'
    print('data to be edited : ')
    patient = self.display_patient(id)
    id_db = patient.doc_id
    
    patient_ed = Patient()
    patient_ed.id = patient['id']
    patient_ed.name=self.patient_edit.set_name()
    patient_ed.diagnosis= self.patient_edit.set_diagnosis()
    patient_ed.age = self.patient_edit.set_age()
    
    db.update(to_dic(patient_ed), doc_ids=[id_db])
    print('edited data : ')
    print(patient)
    return patient_ed
  
  def remove_patient(self,id=None):
    #check the default id is valid or not
    patient_ids  = [p['id'] for p in db]
    if id !=None:
      if (isinstance(id, int) and (id in patient_ids)) == False:
        return 'Invalid ID request'
    
    print('data to be removed : ')
    q= self.display_patient(id)
    id_db = q.doc_id
    db.remove(doc_ids=[id_db])
    return "Successfully deleded patient with id {}  ".format(id)


def patients_menu():

  PatientL= patient_menu()
  choice= ''
  while True:
    print('')
    print("0- return to Main Menu ")
    print("1- Display patient's list ")
    print("2- Search for patient by ID ")
    print("3- Add patient ")
    print("4- Edit patient info ")
    print("5- remove patient ")

    choice= input("Enter option: ")
    choice=choice.strip()

    if choice=='1':
      PatientL.display_all_patients()
    elif choice=='2':
      PatientL.display_patient()
    elif choice=='3':
      PatientL.add_patient()
    elif choice=='4':
      PatientL.edit_patient()
    elif choice=='5':
      PatientL.remove_patient()
    elif choice=='0':
      break
    else:
      print('invalid choice, please try again')



if __name__=='__main__':
  PatientL= patient_menu()
  choice= ''
  while True:
    print('')
    print("0- return to Main Menu ")
    print("1- Display patient's list ")
    print("2- Search for patient by ID ")
    print("3- Add patient ")
    print("4- Edit patient info ")
    print("5- remove patient ")

    choice= input("Enter option: ")
    choice=choice.strip()

    if choice=='1':
      PatientL.display_all_patients()
    elif choice=='2':
      PatientL.display_patient()
    elif choice=='3':
      PatientL.add_patient()
    elif choice=='4':
      PatientL.edit_patient()
    elif choice=='5':
      PatientL.remove_patient()
    elif choice=='0':
      PatientL = None
      break
    else:
      print('invalid choice, please try again')