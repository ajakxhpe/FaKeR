from faker import Faker
import os
from rich.panel import Panel
from rich import print


def fake():

#===================theme===============================
        numberzz = print(Panel(f"""[yellow]
1 --> name fake                                    
[red]2 --> address fake                                
[green]3 --> email fake                                     
[blue]4 --> text fake                                      
        """,style="white"))
        number = input("-->")

        from rich.console import Console
        console = Console()

#====================name==================================
        if number == "1":       
                os.system("clear" or "cls")
                ranges = console.input("Number --> ")
                Languages = console.input("Language -->")
                os.system("clear" or "cls")

                fake = Faker(Languages)

                
                for x in range(int(ranges)):
                        namefake = fake.name()
                        print(Panel (namefake))

#====================address==================================
        
        if number == "2":       
                os.system("clear" or "cls")
                ranges = input("Number --> ")
                Languages = input("Language -->")
                os.system("clear" or "cls")

                fake = Faker(Languages)

                
                for x in range(int(ranges)):
                        addressfake = fake.address()
                        print(Panel (addressfake))


#====================email==================================
                        
        if number == "3":       
                os.system("clear" or "cls")
                ranges = input("Number --> ")
                Languages = input("Language -->")
                os.system("clear" or "cls")

                fake = Faker(Languages)

                
                for x in range(int(ranges)):
                        emailfake = fake.email()
                        print(Panel (emailfake))
                        
#====================text==================================

        if number == "4":       
                os.system("clear" or "cls")
                ranges = input("Number --> ")
                Languages = input("Language -->")
                os.system("clear" or "cls")

                fake = Faker(Languages)

                
                for x in range(int(ranges)):
                        textfake = fake.text()
                        print(Panel (textfake))