import os
import datetime
import time
import math
import random
import uuid
import string
import importlib

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print("File created successfully!")
    except Exception as e:
        print(f"Error creating file: {e}")

def write_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print("Data written successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                print("\nFile Content:")
                print(f.read())
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Error: File does not exist.")

def append_file(filename, content):
    try:
        with open(filename, 'a') as f:
            f.write("\n" + content)
        print("Data appended successfully!")
    except Exception as e:
        print(f"Error appending to file: {e}")


def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            now = datetime.datetime.now()
            print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
          
        elif choice == '2':
            d1_str = input("Enter the first date (YYYY-MM-DD): ")
            d2_str = input("Enter the second date (YYYY-MM-DD): ")
            try:
                d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format! Use YYYY-MM-DD.")
          
        elif choice == '3':
            fmt = input("Enter format (e.g., %d-%m-%Y %H:%M): ")
            try:
                print("Formatted Date:", datetime.datetime.now().strftime(fmt))
            except Exception:
                print("Invalid format string.")
         
        elif choice == '4':
            input("Press Enter to start stopwatch...")
            start_time = time.time()
            input("Press Enter to stop stopwatch...")
            end_time = time.time()
            print(f"Elapsed Time: {round(end_time - start_time, 2)} seconds")
          
        elif choice == '5':
            try:
                sec = int(input("Enter countdown time in seconds: "))
                print("Starting countdown...")
                while sec > 0:
                    print(f"{sec}...", end=" ", flush=True)
                    time.sleep(1)
                    sec -= 1
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid number of seconds.")

        elif choice == '6':
            break
        else:
            print("Invalid choice! Try again.")

def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial: {math.factorial(num)}")
            except ValueError:
                print("Invalid input! Enter an integer.")
        
        elif choice == '2':
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                amount = p * ((1 + r / 100) ** t)
                print(f"Compound Interest: {round(amount, 2)}")
            except ValueError:
                print("Invalid numerical input.")
            
        elif choice == '3':
            try:
                deg = float(input("Enter angle in degrees: "))
                rad = math.radians(deg)
                print(f"sin({deg}) = {round(math.sin(rad), 4)}")
                print(f"cos({deg}) = {round(math.cos(rad), 4)}")
                print(f"tan({deg}) = {round(math.tan(rad), 4)}")
            except ValueError:
                print("Invalid input.")
            
        elif choice == '4':
            print("Select shape: 1. Circle  2. Rectangle")
            s_choice = input("Enter choice: ")
            if s_choice == '1':
                r = float(input("Enter radius: "))
                print(f"Area of Circle: {round(math.pi * r * r, 2)}")
            elif s_choice == '2':
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print(f"Area of Rectangle: {l * w}")
           
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

def random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            start = int(input("Enter lower bound: "))
            end = int(input("Enter upper bound: "))
            print(f"Random Number: {random.randint(start, end)}")
          
        elif choice == '2':
            size = int(input("Enter size of list: "))
            lst = [random.randint(1, 100) for _ in range(size)]
            print(f"Generated List: {lst}")
          
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"Generated Password: {password}")
       
        elif choice == '4':
            otp = random.randint(100000, 999999)
            print(f"Generated OTP: {otp}")
    
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

def file_operations_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            fname = input("Enter file name: ")
            create_file(fname)
        
        elif choice == '2':
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")
            write_file(fname, data)
           
        elif choice == '3':
            fname = input("Enter file name: ")
            read_file(fname)
    
        elif choice == '4':
            fname = input("Enter file name: ")
            data = input("Enter data to append: ")
            append_file(fname, data)
          
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

def explore_module():
    print("\nExplore Module Attributes:")
    mod_name = input("Enter module name to explore: ")
    try:
        mod = importlib.import_module(mod_name)
        attrs = dir(mod)
        print(f"Available Attributes in {mod_name} module:")
        print(attrs[:15], "... (and more)" if len(attrs) > 15 else "")
    except ModuleNotFoundError:
        print("Module not found!")
    
def main():
    while True:
      
        print("Welcome to Multi-Utility Toolkit")
        
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
     
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            datetime_operations()
        elif choice == '2':
            math_operations()
        elif choice == '3':
            random_operations()
        elif choice == '4':
            print("\nGenerate Unique Identifiers:")
            print(f"Generated UUID: {uuid.uuid4()}")
        
        elif choice == '5':
            file_operations_menu()
        elif choice == '6':
            explore_module()
        elif choice == '7':
         
            print("Thank you for using the Multi-Utility Toolkit!")
       
            break
        else:
            print("Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()