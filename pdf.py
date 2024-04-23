import PyPDF2
import itertools

pdf_file_path = input("\nEnter PDF File Path : ")

combinations = ""

numconfirm = input("\nIs The Password Contains Numbers ? ( if dont know , enter 'yes') ( yes / no ) : ")

charconfirm = input("\nIs The Password Contains Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

specialcharconfirm = input("\nIs The Password Contains Special Characters ? ( if dont know , enter 'yes') ( yes / no ) : ")

if charconfirm.lower() == "yes" or charconfirm.lower() == "y":
    combinations += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if specialcharconfirm.lower() == "yes" or specialcharconfirm.lower() == "y":
    combinations += "!@#$%^&*()?/<>.,;':\"|\\"

if numconfirm.lower() == "yes" or numconfirm.lower() == "y":
    combinations += "0123456789"



password_length = input("\nEnter Maximun Guessed Password Length (eg . 6 numbers or 9 characters ) : ")

print(combinations)

password_found = False

for r in range(1, int(password_length)+1):
    if password_found:
        break  

    combination = itertools.product(combinations, repeat=r)
    for combo in combination:
        password = ''.join(combo)

        try:
           
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                print("Trying : " + password)
                if pdf_reader.is_encrypted:
                    if pdf_reader.decrypt(password) == 1:
                        print("Successfully decrypted the PDF file.")
                        print("Password Is : " + password)
                        password_found = True
                        break  
                    
        except FileNotFoundError:
            print("Error: File not found.")
            break  
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break 
    
    print(r , " Iteration Completed.. ")