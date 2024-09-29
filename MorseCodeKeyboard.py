from gpiozero import Button, LED  # Importă clasele Button și LED din biblioteca gpiozero
from time import sleep  # Importă funcția sleep din biblioteca time
import I2C_LCD_driver  # Importă driverul pentru LCD folosind I2C

# Definirea pinilor pentru butoane și LED-uri
pctBtnPin = 2
pctLedPin = 17
lnBtnPin = 3
lnLedPin = 27
DLBtnPin = 4
DLLedPin = 22
DCBtnPin = 5
DCLedPin = 10

# Codul Morse pentru litere și cifre
codMorse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."
]

# Lista caracterelor corespunzătoare codului Morse
codMorseInLitereCifre = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Variabile globale pentru stocarea codului Morse, textului și propoziției
litera = ""
tastatura = ""
propozitie = ""

# Funcție care găsește litera corespunzătoare unui cod Morse
def gasesteLitera(morseCode):
    if (morseCode in codMorse):
        return codMorseInLitereCifre[codMorse.index(morseCode)]
    return ' '  # Returnează spațiu dacă codul Morse nu este găsit

# Funcție apelată când butonul punct este apăsat
def pctBtnPressed():
    global tastatura
    pctLed.on()  # Aprinde LED-ul pentru punct
    tastatura += '.'  # Adaugă un punct la codul Morse curent
    lcd.lcd_clear()  # Curăță afișajul LCD
    lcd.lcd_display_string(tastatura, 1)  # Afișează codul Morse curent pe LCD
    sleep(0.5)  # Așteaptă 0.5 secunde
    pctLed.off()  # Stinge LED-ul pentru punct

# Funcție apelată când butonul linie este apăsat
def lnBtnPressed():
    global tastatura
    lnLed.on()  # Aprinde LED-ul pentru linie
    tastatura += '-'  # Adaugă o linie la codul Morse curent
    lcd.lcd_clear()  # Curăță afișajul LCD
    lcd.lcd_display_string(tastatura, 1)  # Afișează codul Morse curent pe LCD
    sleep(0.5)  # Așteaptă 0.5 secunde
    lnLed.off()  # Stinge LED-ul pentru linie

# Funcție apelată când butonul de delimitare litere este apăsat
def DLBtnPressed():
    global tastatura, propozitie
    DLLed.on()  # Aprinde LED-ul pentru delimitarea literelor
    litera = gasesteLitera(tastatura)  # Găsește litera corespunzătoare codului Morse curent
    propozitie += litera  # Adaugă litera la propoziția curentă
    lcd.lcd_clear()  # Curăță afișajul LCD
    lcd.lcd_display_string(propozitie, 1)  # Afișează propoziția curentă pe LCD
    sleep(0.5)  # Așteaptă 0.5 secunde
    DLLed.off()  # Stinge LED-ul pentru delimitarea literelor
    tastatura = ""  # Resetează codul Morse curent

# Funcție apelată când butonul de delimitare cuvinte este apăsat
def DCBtnPressed():
    global tastatura, propozitie
    DCLed.on()  # Aprinde LED-ul pentru delimitarea cuvintelor
    propozitie += " "  # Adaugă un spațiu la propoziția curentă
    lcd.lcd_clear()  # Curăță afișajul LCD
    lcd.lcd_display_string(propozitie, 1)  # Afișează propoziția curentă pe LCD
    sleep(0.5)  # Așteaptă 0.5 secunde
    DCLed.off()  # Stinge LED-ul pentru delimitarea cuvintelor
    tastatura = ""  # Resetează codul Morse curent

# Funcție de configurare a componentelor hardware
def setup():
    global lcd, pctBtn, pctLed, lnBtn, lnLed, DLBtn, DLLed, DCBtn, DCLed

    lcd = I2C_LCD_driver.lcd()  # Inițializează LCD-ul

    pctBtn = Button(pctBtnPin)  # Inițializează butonul pentru punct
    pctLed = LED(pctLedPin)  # Inițializează LED-ul pentru punct
    lnBtn = Button(lnBtnPin)  # Inițializează butonul pentru linie
    lnLed = LED(lnLedPin)  # Inițializează LED-ul pentru linie
    DLBtn = Button(DLBtnPin)  # Inițializează butonul pentru delimitarea literelor
    DLLed = LED(DLLedPin)  # Inițializează LED-ul pentru delimitarea literelor
    DCBtn = Button(DCBtnPin)  # Inițializează butonul pentru delimitarea cuvintelor
    DCLed = LED(DCLedPin)  # Inițializează LED-ul pentru delimitarea cuvintelor

    # Setează funcțiile care vor fi apelate când butoanele sunt apăsate
    pctBtn.when_pressed = pctBtnPressed
    lnBtn.when_pressed = lnBtnPressed
    DLBtn.when_pressed = DLBtnPressed
    DCBtn.when_pressed = DCBtnPressed

# Funcția principală de buclă
def loop():
    try:
        while True:  # Rulează bucla infinită
            sleep(0.1)  # Așteaptă 0.1 secunde între iterații
    except KeyboardInterrupt:  # Dacă programul este oprit de utilizator
        print("Program oprit de utilizator.")  # Afișează mesajul

# Apelarea funcțiilor de configurare și buclă
setup()
loop()
