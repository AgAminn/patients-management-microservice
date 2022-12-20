print('starting app')
   
from patient_func import patients_menu

if __name__ == "__main__":
    choice= ''
    while True:
      print('')
      print("0- return to Main Menu ")
      print("1- Access patient's menu ")

      choice= input("Enter option: ")
      choice=choice.strip()

      if choice=='1':
        patients_menu()
      elif choice=='0':
        break
      else:
        print('invalid choice, please try again')

