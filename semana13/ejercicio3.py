from datetime import datetime

class User:
    
    def __init__(self, date_birth):
        self.date_birth = datetime.strptime(date_birth, '%Y-%m-%d')
    
    @property
    def age(self):
        today = datetime.now()
        age = today.year - self.date_birth.year - ((today.month, today.day) < (self.date_birth.month, self.date_birth.day))
        return age


def user_review(func):
    def wrapper(user):
        return func(user)
    return wrapper

@user_review
def age_checker(user):
    if user.age < 18:
        raise ValueError(f'Eres menor de edad, no puedes ingresar.')
    else:
        print("BIENVENIDO!")
        


Amy = User('1997-10-22')
age_checker(Amy)

Joey = User('2000-04-27')
age_checker(Joey)

Sam = User('2012-08-30')
age_checker(Sam)