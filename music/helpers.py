from django.core.mail import send_mail
from account.models import User



def send_spam(new_song):
    users_email = [x for x in User.objects.all()]
    message = f"""
Артист {new_song.artist} выпустил новую песню {new_song.title}    
"""
    send_mail("Новинка", message, "email", users_email)