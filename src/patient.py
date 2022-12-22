'''
patient object
'''
    
class Patient:
    def __init__(self,ID=None,name=None,diagnosis=None,age=None):
      self._id = ID
      self._name = name
      self._diagnosis = diagnosis
      self._age = age
    
    @property
    def id(self):
      return self._id
    
    @property
    def name(self):
      return self._name
    
    @property
    def diagnosis(self):
      return self._diagnosis

    @property
    def age(self):
      #print('patient age :')
      return self._age

    @id.setter
    def id(self,ID):
      self._id = ID
    
    @name.setter
    def name(self,namo):
      self._name = namo
    
    @diagnosis.setter
    def diagnosis(self,diagnosis):
      self._diagnosis = diagnosis
    
    @age.setter
    def age(self,age):
      self._age = age
    