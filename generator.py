import random
import string

class Generate_password:
    def __init__(self, letters_valu, digits_value, special_characters_value, pass_length): 
        self.letters_valu = letters_valu
        self.digits_value = digits_value
        self.special_characters_value = special_characters_value
        self.pass_length = pass_length
    
    
    def generate(self):
        #Letters
        if letters_value is True and digits_value is False and special_characters_value is False:
            generated_password = string.ascii_letters
        #Digits
        elif letters_value is False and digits_value is True and special_characters_value is False:
            generated_password = string.digits
        #Special Characters
        elif letters_value is False and digits_value is False and special_characters_value is True:
            generated_password = string.punctuation
         
        #Letters and digits
        elif letters_value is True and digits_value is True and special_characters_value is False:
            generated_password = string.ascii_letters + string.digits
         
        #Letters and special characters
        elif letters_value is True and digits_value is False and special_characters_value is True:
            generated_password = string.ascii_letters + string.punctuation
         
        #Digits and special charakters
        elif letters_value is False and digits_value is True and special_characters_value is True:
            generated_password = string.digits + string.punctuation
            
        #Letters, digits and special charakters
        elif letters_value is True and digits_value is True and special_characters_value is True:
            generated_password = string.ascii_letters + string.digits + string.punctuation
         
        elif letters_value is False and digits_value is False and special_characters_value is False:
            generated_password = "You have to choose at least one type"
            return generated_password
        
        return "".join(random.choice(generated_password) for i in range(pass_length))

    

if __name__ == "__main__":
    #letters, digits, special characters, letters_digits, letters_special_charakters, digits_special_charakters, letters_digits_special_charakters
    
    letters_value = True 
    digits_value = True
    special_characters_value = True
    pass_length = 10
    
    password = Generate_password(letters_value, digits_value, special_characters_value, pass_length)
    generated_password = password.generate()
    print(generated_password)

