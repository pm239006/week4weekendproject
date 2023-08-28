
print("--------Welcome to the Rental income ROI calculation project by Priscilla Mendez --------")
print("--------This application will allow you to enter your investment property details. After all details are in the system, the application will calculate a Return on your Investment--------")

print("""            
        What would you like to do? Please type in your response here: 
        Create - Welcome, Create new account     
        Login - login to your profile
        Logout - logout of your profile                       
        View - view property list
        Add - add property to list
        Remove - remove property from list
        Quit - close the application           
        
        """)
        
# User class 
class User():
    def __init__(self,username,password,email):
        self.username = username
        self.password = password 
        self.email = email
        # self.properties = []
        self.property_list = []

    
    def check_password(self, password_guess):
        return self.password == password_guess[::-2]
    
        #CREATE A USER ACCT
def add_user(self):
    print("To begin your journey with us, create your own username ID and password. Make sure to keep this information handy and private.")
    username = input("Please create a username: ")
    
    if username in {u.username for u in self.users}:
        print("User with that name already exists. Please try again!") # 409 Error, conflict in request
    else:
        password = input("Please enter your password: ")
        user = User(username, password)
        self.users.add(user)
        print(f"Perfect! {user} has been created")     

    self.login_user()

    #LOG IN TO ACCT
def login_user(self):
    "---- Please login to continue ---- "
    username = input("What is your username? ")
    password = input("What is your password? ")

    for user in self.users:
        if user.username == username and user.check_password(password):
            self.current_user = user
            print(f"{user} has logged in")
            break
    else:
        print("Username and/or password is incorrect")

        #LOG OUT OF ACCT 
def logout(self):
    self.current_user = None
    print("You have succesfully been logged out!")

    
            # ADD NEW PROPERTY TO LIST 
def add_property(self,property):
    print("/n Okay, we will now collect all data needed to proceed...")
    property_address = input("What is the address of the home?")
    price = input("What is the price of the home? ")
    sq_feet = input("How many square feet is the home?  ")
    apt_units = input("How many apartment units does the home have?  ")
    bathrooms = input("How many bathrooms does the home have?  ")
    bedrooms = input("How many bedrooms does the home have?  ")

    self.current_user.property_list.append(property)

    print(f"Your property at {property_address.title} is now in your property list")

def view_property_list(self):
    for properties in self.current_user.property_list:
        return(f"{self.property_address} was purchased for ${self.price}, it is {self.sq_feet} square feet and contains {self.apt_units} units. There are {self.bedrooms} bedrooms and {self.bathrooms} baths.")

        # REMOVE PROPERTY FROM LIST 
def remove_property(self,property):
    print("Your current property list: ")
    self.view_property_list()

    reply = input("What property would you like to remove? ")
    for properties in self.property_list:
        if reply.lower() == self.current_user.property_address.lower.title():
            self.current_user.property_list.remove(property)
        print(f"{reply.title()} has been removed from your property list!")
        break
    else:
        print("This property is not in your list! ") #404 not found
        


def display_properties(self):
        print("PROPERTY DETAILS")
        print("_________________")
        print("square footage: {}"(self.square_feet))
        print("bedrooms: {}"(self.bedrooms))
        print("bathrooms: {}"(self.bathrooms))
        print()

# property class
class Property():
    def __init__():
        expenses = {}
        income = {}
        roi = None
       
    def collect_big_expenses(self):
        print(" This section pertains to the one time expenses for the home (Such as closing fees, down payment, etc .. ) ")
        closing_cost = float(input("Enter your closing cost on the home ($USD): "))
        down_payment = float(input("Enter your down payment on the home ($USD): "))
        misc_fees = float(input("Enter any additional one-time expenses housing expenses ($USD): "))

        one_time_expenses = closing_cost + down_payment + misc_fees
        return one_time_expenses

    def collect_expenses(self):
        print(" When it comes to finances and purchasing a big home, the small things add up. Please include all monthly expenses here: " )
        total_monthly_expenses = mortgage + utilities + taxes + repair + insurance + misc

        mortgage = float(input("Enter your monthly housing expense ($USD): "))
        utilities = float(input("Enter your monthly utilities expense ($USD): "))
        taxes = float(input("Enter your monthly tax expenses ($USD): "))
        repair = float(input("Enter your monthly repair expense ($USD): "))
        insurance = float(input("Enter your monthly insurance expense ($USD): "))
        misc  = float(input("Enter any additional housing expenses ($USD): "))
        return total_monthly_expenses 
        
    # def total_investment(self):
    #     overall_expenses = self.one_time_expenses + self.total_montly_expenses

    #     return f" Your total investment on this property is ${overall_expenses}"


    def collect_income(self):
        while True:
            incometype = input("What kind of income do you have? ")
            income = float(input("Enter your monthly income ($USD): "))  
            additional = input("Do you have any other sources of income? y/n ")
            if next.lower() == "y":
                continue
            else:
                break
        self.income[income] = income + additional
        return self.income
    
    def calc_roi(self,income,expenses):

        monthly_cash_flow = float(income - self.total_monthly_expenses)
        annual_cash_flow =  (monthly_cash_flow) * 12 
        roi = annual_cash_flow / self.one_time_expenses
        roi_percent = roi * 100
        return roi_percent 


# runner code 

class Runner():
    def __init__(self):
        self.users = []
        self.current_user = None

    def run(self):

        if self.users:
            self.choose_user()
        else:
            self.add_user()            

            print("""            
                        What would you like to do? Please type in your response here: 
                        Create - Welcome, Create new account     
                        Login - login to your profile
                        Logout - logout of your profile                       
                        View - view property list
                        Add - add property to list
                        Remove - remove property from list
                        Quit - close the application           
                        
                        """)
        
    while True:
                response = input("What would you like to do? (create, login, logout, view, add, remove, quit) ")
                
                if response.lower() == "add":
                    add_property()
                elif response.lower() == "remove":
                    remove_property()
                elif response.lower() == "create":
                    add_user()
                elif response.lower() == "view":
                    display_properties()
                elif response.lower() == "logout":
                    logout()

                    new_response = input("What would you like to do next? login, add, quit")
                    if new_response.lower() == 'add':
                        add_user()
                    elif new_response.lower() == 'login':
                        login_user()
                    elif new_response.lower() == 'quit':
                        print("We hope to see you again soon!")
                        break
                    else:
                        print("Please enter a valid response and try again!")
                elif response.lower() == 'login':
                    login_user()
                elif response.lower() == "view":
                    view_property_list()
                elif response.lower() == "remove":
                    remove_property()
                elif response.lower() == "quit":
                    print(f"Thanks for using our calculator! We hope to see you soon again!")
                    break
                else:
                    print("Invalid Input: please choose from the list!")
            


roi_project = Property()

roi_project.run()

    # input log in or sign up? 
    # if sign up create an instance of the user class
    # if log in - give user name and pw and 
    # run a for loop over users, if email == email and pw == pw set them as current user 
    # create an attr of current user 
    # give them the option add property,delete,view properties(display), <-- methods of user class

    # tracks the users 
