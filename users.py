import time #توقيف الكود وقت محدد
import os #تنظيف الشاشة ومسح ما قبل 

class User:
	def __init__(self,name,lastname, email, password, condition='inactive'):
		self.name=name
		self.lastname=lastname 
		self.email=email
		self.password=password
		
	def show (self):
		print(f'first name : {self.name}')
		print (f'last name : {self.lastname}')
		print(f'email : {self.email}')
		print (f'password : {self.password}')
		print ('_'*20,'\n')
		
def creat_user() :
    name=input ('enter your first name : ')
    lastname =input ('enter your lastname: ')
    email=input ('enter your email: ')
    password=input('enter your password') 
    return User(name, lastname, email, password)
    print ('user added success !!')

def clean ():
	os.system('cls'if os.name=='nt'else 'clear')#تنظيف الشاشة 

show_all_user= [] #قائمة فارغ  للتخزين
		
while True :
	print ('\nchose to action\n')
	print('1. add new user\n2. see all user\n3. Exit')
	choice = input ('enter your choice : ')	
	if choice == '1':
		show_all_user.append(creat_user())		
		time.sleep(2)#التوقف لثانيتين
	elif choice =='2':
		clean()
		#التاكد من ان القائمة  ليست فارغة
		if show_all_user:
			print ('show all users...')
			time.sleep(1)#التوقف لثانية
			for i in show_all_user:
				i.show()
		else :
			print ('sorry , didnt find any users !')
			continue 
						
	elif choice =='3':
		print ('\nexit...')
		break
	else :
		print ('\n***** eror , try again *****')
		continue 		