import random
import string

class Generate_password:
    def __init__(self, letters_value, digits_value, special_characters_value, pass_length): 
        if letters_value == "True":
            letters_value = True
        if digits_value == "True":
            digits_value = True
        if special_characters_value == "True":
            special_characters_value = True
        
        self.letters_value = letters_value
        self.digits_value = digits_value
        self.special_characters_value = special_characters_value
        self.pass_length = pass_length

    def generate(self):
        #Letters
        if self.letters_value is True and self.digits_value is False and self.special_characters_value is False:
            generated_password = string.ascii_letters
        #Digits
        elif self.letters_value is False and self.digits_value is True and self.special_characters_value is False:
            generated_password = string.digits
        #Special Characters
        elif self.letters_value is False and self.digits_value is False and self.special_characters_value is True:
            generated_password = string.punctuation
         
        #Letters and digits
        elif self.letters_value is True and self.digits_value is True and self.special_characters_value is False:
            generated_password = string.ascii_letters + string.digits
         
        #Letters and special characters
        elif self.letters_value is True and self.digits_value is False and self.special_characters_value is True:
            generated_password = string.ascii_letters + string.punctuation
         
        #Digits and special charakters
        elif self.letters_value is False and self.digits_value is True and self.special_characters_value is True:
            generated_password = string.digits + string.punctuation
            
        #Letters, digits and special charakters
        elif self.letters_value is True and self.digits_value is True and self.special_characters_value is True:
            generated_password = string.ascii_letters + string.digits + string.punctuation         
        #None length
        elif self.pass_length == 0:
            generated_password = "You have to choose password length"
            return generated_password
        #None type
        elif self.letters_value is False and self.digits_value is False and self.special_characters_value is False:
            generated_password = "You have to choose at least one type"
            return generated_password
        
        
        self.generated_password = "".join(random.choice(generated_password) for i in range(self.pass_length))
        return self.generated_password
