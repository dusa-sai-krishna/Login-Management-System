class Console:
    
    def __init__(self) -> None:
        self.data={}
        self.user=None
    
    def registration(self):
        name=input('Enter name: ')
        email=input('Enter email: ')
        rn=input('Enter roll no: ')
        psw=input('Enter psw: ')
        print('\n\n')
        if rn in self.data:
            print('Already Registered!!!')

        elif name and email and rn and psw:
            
            self.data[rn]={'name':name,'email':email,'psw':psw}
        else:
            print('Pls Enter valid data')
        print('\n\n')
        
    
    def login(self):
        rn=input('Enter roll no: ')
        psw=input('Enter psw: ')
        print('\n\n')
        if rn in (None,'') or psw in (None,''): 
            print('Enter Valid Data')
        else:
            if rn not in self.data:
                print('User not Found')
            elif self.data[rn]['psw']!=psw:
                print('Enter valid psw')
            elif self.user==rn:
                print('Already Logged in')
            else:
                self.user=rn
                print('Logged in successfully')
        print('\n\n')

    
    
    def display_profile(self):
        if self.user==None:
            print('User not logged in')
        else:
            rn=self.user
            print(f'\n\nRoll No: {rn}')
            print(f"Name: {self.data[rn]['name']}")
            print(f"Email id: {self.data[rn]['email']}\n\n")
        
    
    def process(self):
        while True:
            print('Welcome to Login Management Portal')
            print('Here are the options')
            print('1. Registration')
            print('2. Login')
            print('3. View profile')
            print('4. Logout and exit')
            
            try:
                op=int(input('Enter the option: '))
                if op==1:
                    self.registration()
                elif op==2:
                    self.login()
                elif op==3:
                    self.display_profile()
                elif op==4:
                    print('Logged out Sucessfully')
                    break
                else:
                    print('Enter valid option')
                
                
            except Exception as e:
                print(e)
                print('Enter valid option')
                
                
obj=Console()
obj.process()