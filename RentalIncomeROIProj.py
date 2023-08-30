
print("--------Welcome to the Rental income ROI calculation project by Priscilla Mendez --------")
print("--------This application will allow you to enter your investment property details. After all details are in the system, the application will calculate a Return on your Investment--------")

print("""            
         ---------- MAIN MENU ----------
        Create - create new account     
        Login - login to your profile
        Logout - logout of your profile                       
        View - view property list
        Add - add property to list
        Remove - remove property from list
        Calculate - reveal return on investment
        Quit - close the application           
        
        """)
# User class 
class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password 
        self.property_list = []

    
    def check_password(self, password_guess):
        return self.password == password_guess[::-2]
    
    def view_property_list(self):
        for property in self.property_list:
            return(f"{property.property_address} was purchased for ${property.price}, it is {property.sq_feet} square feet and contains {property.apt_units} units. There are {property.bedrooms} bedrooms and {property.bathrooms} baths.")

              # REMOVE PROPERTY FROM LIST 
    def remove_property(self,property):
        print("Your current property list: ")
        self.view_property_list()

        reply = input("What property would you like to remove? ")
        for property in self.property_list:
            if reply.lower() == property.property_address.lower():
                self.property_list.remove(property)
            print(f"{reply.title()} has been removed from your property list!")
            break
        else:
            print("This property is not in your list! ") #404 not found

                    # ADD NEW PROPERTY TO LIST 
    def add_property(self):
        print("Okay, we will now collect all data needed to proceed...")
        property_address = input("What is the address of the home?")
        price = input("What is the price of the home? ")
        sq_feet = input("How many square feet is the home?  ")
        apt_units = input("How many apartment units does the home have?  ")
        bathrooms = input("How many bathrooms does the home have?  ")
        bedrooms = input("How many bedrooms does the home have?  ")

        prop = Property(price, property_address, sq_feet, apt_units, bedrooms, bathrooms)
        self.property_list.append(prop)

        print(f"Your property at {property_address.title()} is now in your property list")
    def disp_props(self):
        for p in self.property_list:
            p.display_property()
   

# property class
class Property():
    def __init__(self, price, property_address, sq_feet, apt_units, bedrooms, bathrooms):
        self.price = price
        self.property_address = property_address
        self.sq_feet = sq_feet
        self.apt_units = apt_units 
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        roi = None

                # ADD NEW PROPERTY TO LIST 
    def add_property(self):
        print("/n Okay, we will now collect all data needed to proceed...")
        property_address = input("What is the address of the home?")
        price = input("What is the price of the home? ")
        sq_feet = input("How many square feet is the home?  ")
        apt_units = input("How many apartment units does the home have?  ")
        bathrooms = input("How many bathrooms does the home have?  ")
        bedrooms = input("How many bedrooms does the home have?  ")

        self.price = price
        self.property_address = property_address
        self.sq_feet = sq_feet
        self.apt_units = apt_units 
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms


        print(f"Your property at {property_address.title()} is now in your property list")

        while True:
            def collect_big_expenses(self):
                print(" This section pertains to the one time expenses for the home (Such as closing fees, down payment, etc .. ) ")
            closing_cost = float(input("Enter your closing cost on the home ($USD): "))
            down_payment = float(input("Enter your down payment on the home ($USD): "))
            misc_fees = float(input("Enter any additional one-time expenses housing expenses ($USD): "))

            one_time_expenses = closing_cost + down_payment + misc_fees
            self.one_time_expenses = one_time_expenses
                
    def display_property(self):
            print("PROPERTY DETAILS")
            print("_________________")
            print(f"adress: {self.property_address}")
            print(f"square footage: {self.sq_feet}")
            print(f"bedrooms: {self.bedrooms}")
            print(f"bathrooms: {self.bathrooms}")

    def collect_big_expenses(self):
        print(" This section pertains to the one time expenses for the home (Such as closing fees, down payment, etc .. ) ")
        closing_cost = float(input("Enter your closing cost on the home ($USD): "))
        down_payment = float(input("Enter your down payment on the home ($USD): "))
        misc_fees = float(input("Enter any additional one-time expenses housing expenses ($USD): "))

        one_time_expenses = closing_cost + down_payment + misc_fees
        self.one_time_expenses = one_time_expenses

    def collect_expenses(self):
        print(" When it comes to finances and purchasing a big home, the small things add up. Please include all monthly expenses here: " )
        total_monthly_expenses = mortgage + utilities + taxes + repair + insurance + misc

        mortgage = float(input("Enter your monthly housing expense ($USD): "))
        utilities = float(input("Enter your monthly utilities expense ($USD): "))
        taxes = float(input("Enter your monthly tax expenses ($USD): "))
        repair = float(input("Enter your monthly repair expense ($USD): "))
        insurance = float(input("Enter your monthly insurance expense ($USD): "))
        misc  = float(input("Enter any additional housing expenses ($USD): "))
        self.total_monthly_expenses = total_monthly_expenses
    
    def collect_income(self):
        while True:
        # incometype = input("What kind of income do you have? ")
            income = float(input("Enter your monthly income ($USD): "))  
            additional = input("Do you have any other sources of income? y/n ")
            if additional.lower() == "y":
                while True:
                    add_income = (input("How much income do you want to add? "))
                    additonal2 = input("Do you have any other sources of income? y/n ")

                    income += add_income

            else:
                print(f"Your total income is ${income}.00")

    def calc_roi(self,income):

        monthly_cash_flow = float(income - self.total_monthly_expenses)
        annual_cash_flow =  (monthly_cash_flow) * 12 
        roi = annual_cash_flow / self.one_time_expenses
        roi_percent = roi * 100
        return f"Your return on investment is {roi_percent}%"
    
    def calculation(self):
        for i in self.property_list:
            i.calc_roi()


# runner code 

class Runner():
    def __init__(self):
        self.users = []
        self.current_user = None
    def create_user(self):
        print("To begin your journey with us, create your own username ID and password. Make sure to keep this information handy and private.")
        username = input("Please create a username: ")
        
        if username in {u.username for u in self.users}:
            print("User with that name already exists. Please try again!") # 409 Error, conflict in request
        else:
            password = input("Please enter your password: ")
            user = User(username, password)
            self.users.append(user)
            print(f"Perfect! {user} has been created")   
            # user_class = User(username, password) 
            # property = Property()  

            self.current_user = user
        
        #LOG IN TO ACCT
    def login_user(self):
        "---- Please login to continue ---- "
        username = input("What is your username? ")
        password = input("What is your password? ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"{user} has logged in")
                break
        else:
            print("Username and/or password is incorrect")

    def logout(self):
        self.current_user = None
        print("You have succesfully been logged out!")


    def run(self):

        while True:
            print("--------Welcome to the Rental income ROI calculation project by Priscilla Mendez --------")
            print("--------This application will allow you to enter your investment property details. After all details are in the system, the application will calculate a Return on your Investment--------")

            print("""            
                    ---------- MAIN MENU ----------
                    Create - create new account     
                    Login - login to your profile
                    Logout - logout of your profile                       
                    View - view property list
                    Add - add property to list
                    Remove - remove property from listcreate
                    Calculate - reveal return on investment
                    Quit - close the application           
                    
                    """)  
            to_do = input("What would you like to do?" )

            if to_do.lower() == "create":
                self.create_user()
            elif to_do.lower() == "login":
                self.login_user()
            elif to_do.lower() == "logout":
                self.logout()
            elif to_do.lower() == "view":
                if self.current_user:
                    self.current_user.disp_props()
                else:
                    print("Please log in. You are not currently signed in")

            elif to_do.lower() == "add":
                if self.current_user:
                    self.current_user.add_property()
                else: 
                    print("Please log in. You are not currently signed in")
            elif to_do.lower() == "remove":
                if self.current_user:
                    self.current_user.remove_property()
                else: 
                    print("Please log in. You are not currently signed in")
            elif to_do.lower() == "calculate":
                if self.current_user:
                    self.current_user.calc_roi()
                else: 
                    print("Please log in. You are not currently signed in")
            else:
                to_do.lower() == "quit"
                self.logout()
                print(f"Thanks for using our calculator! We hope to see you soon again!")
                break
x = Runner()
x.run()