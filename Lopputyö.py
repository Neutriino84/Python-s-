import sqlite3
import requests
import json 
from datetime import datetime



  
# Avain säätietoihin.
#api_key = "a34c30675f9e0b419a228892d1242a6f"
  
# Hakee säätiedon
#base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Annetaan kaupungin nimi
#kaupungin_nimi = input("Anna Kaupungin nimi: ") 
  
# lukee url-osoitteen
#complete_url = base_url + "appid=" + api_key + "&q=" + kaupungin_nimi

# pyynnöt
#response = requests.get(complete_url) 
  

#x = response.json() 
  

#if x["cod"] != "404": 
  
    
    #y = x["main"] 
  
    
    #current_temperature = y["temp"] - 273.15 
    
   # z = x["weather"] 
  
    #weather_description = z[0]["description"] 
  
    
    #print(" Temperature (in celsius unit) = " +
                   # str(current_temperature)[:4] +
 
         
          #"\n description = " +
               #     str(weather_description)) 
  
#Tietokanta osuus.

conn = sqlite3.connect('Paikkakunnat.db')
#Tässä luodaan tietokanta.

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Paikkakunnat (Paikka text)') # Luodaan taulukko.
conn.commit()
kysymys = input ("Haluatko muokata hakua? K=(Kyllä) Tai E=(Ei)")
muutos = True
if kysymys == "K": 
    cur.execute('DELETE FROM Paikkakunnat')
    #conn.commit()
elif kysymys == "E":
    muutos = False


    
while muutos == True:
    paikkakunta = input("Anna paikkakunta (X-Lopettaa) : ")
    if paikkakunta != "X":
        sql = f'INSERT INTO Paikkakunnat VALUES ("{paikkakunta}")'
        cur.execute(sql)
       # conn.commit()
        print("Paikkakunta tallennettu.")
        print()
    elif paikkakunta == "X":
         print()
         muutos == False
         break
       
#kysymys = input ('poistetaanko vanha tieto tietokannasta?') 
#if kysymys == "E":
 # for kaupunki in cur.execute('SELECT * Paikka from Paikkakunnat'):
  #  print(kaupunki)


#def delete(con):
 #  cursorObj = con.cursor()
  # cursorObj.execute('DELETE * FROM Paikkakunnat')
    #rows = cursorObj.fetchall()
   #     for row in rows:
    #    print(row)
#delete(conn)    
#while paikkakunta == True:
 #   kysymys = input ('Haluutko tulostaa tiedon?')
#sql = f'INSERT INTO Paikkakunnat VALUES ("{paikkakunta}")'
#conn.commit()
#cur.execute(sql)
#paikkakunta == False



#conn.close()




kysymys = input('Haetaanko tallennetuille paikkakunnille lämpötilat?  K=(Kyllä)')

if kysymys == "K":
    
    for kaupunki in cur.execute ('SELECT * From Paikkakunnat'):
            
           print(kaupunki)   
           api_key = "a34c30675f9e0b419a228892d1242a6f"
           base_url = "http://api.openweathermap.org/data/2.5/weather?"
           complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"
           response = requests.get(complete_url) 
           x = response.json() 
         
    
                   
    kysymys = input ("Haluatko katsoa lämpötiloja ilmatieteenlaitokselta? K =(Kyllä)")
   # paikkakunta = input("Anna Kaupunki: ")
    if kysymys == "K":
        while paikkakunta != "X":
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"
                response = requests.get(complete_url) 
                x = response.json()
                if x["cod"] != "404":
                  y = x["main"]
                current_temperature = y["temp"] - 273.15  # Muutetaan celsiukseiksi
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                print(" Kaupunki: " +
                  str(kaupunki) +
                  "\n Lämpötila = " +
                  str(current_temperature)[:4] + "°C" +
                  "\n ilmanpaine = " +
                  str(current_pressure) + "hPa" +
                  "\n kosteus = " +
                  str(current_humidiy) + "%" +
                  "\n")
                
    conn.close() 

def kirjoita_lokiin(viesti):  
    aika = datetime.now()                                      
    tiedosto = open("a")
    rivi = str(aika) + " " 
    tiedosto.write(rivi + "\r")
    tiedosto.close()

    tiedosto = open("lampo_parametri.txt", "a")           
    rivi = str(aika) + " " 


    print("Ohjelma loppuu!")
               
    print("Valmis!")
        