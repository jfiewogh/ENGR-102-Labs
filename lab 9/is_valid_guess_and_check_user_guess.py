def is_valid_guess(valid_letters, user_guess) :
        letters = []
        for letter in user_guess :
            if letter in valid_letters and letter not in letters : 
                letters.append(letter)
            else: 
                return False
        return len(letters) == 10
def check_user_guess(dividend, quotient, divisor, remainder) : 
     if dividend == quotient * divisor + remainder : 
        return True 
     else : 
         return False
