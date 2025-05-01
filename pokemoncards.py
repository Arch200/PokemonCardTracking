import sqlite3 #sql library to allow for SQL analysis

#connecting to database or creating file for it
conn = sqlite3.connect('pokemonCardCollection.db')
cursor = conn.cursor()

#creates database if doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cards (
    Card_ID INTEGER PRIMARY KEY,
    Card_Name TEXT,
    Language TEXT,
    Card_Type TEXT,
    Value REAL
)
''')

#Added two new columns to track the database better, will allow to track sets and pokemon
#cursor.execute('''ALTER TABLE Cards ADD COLUMN PokedexNo REAL''')
#cursor.execute('''ALTER TABLE Cards ADD COLUMN CardNo REAL''')

#function to update database with new card info
def insertCard(Card_Name, Language, Card_Type, Value, DexNo,CardNo):
    cursor.execute('''INSERT INTO Cards (Card_Name, Language, Card_Type,Value,PokedexNo,CardNo) 
                    VALUES(?,?,?,?,?,?); ''',(Card_Name,Language,Card_Type,Value,DexNo,CardNo))
    conn.commit()

insertCard('Meowscarada', 'ENG', 'Grass', 7.99,908,271193)
insertCard('Giacomo', 'ENG', 'Trainer', 2.13,None,252193)
insertCard('Cyllene', 'ENG', 'Trainer', 4.00,None,183189)
insertCard('Furisode Girl', 'ENG', 'Trainer', 5.50,None,190195)
insertCard('Iono', 'ENG', 'Trainer', 17.75,None,254193)
insertCard('Iron Thorns EX', 'ENG', 'Electric', 4.18,995,196167)
insertCard('Kirlia', 'ENG', 'Psychic', 24.69,281,212198)
insertCard('Noivern EX', 'ENG', 'Dragon', 2.10,715,246193)
insertCard('Pidgeot EX', 'ENG', 'Normal', 13.24,18,225197)
insertCard('Judge', 'ENG', 'Trainer', 1.71,None,228091)
insertCard('Palafin', 'ENG', 'Water', 2.25,964,225091)
insertCard('Gardevoir EX', 'ENG', 'Psychic', 5.87,282,217091)
insertCard('Grotle', 'ENG', 'Grass', 10.44, 388,164162)
insertCard('Arcanine EX','ENG','Fire',2.17,59,32198)
insertCard('Garchomp EX','ENG','Water',37.35,445,245182)
insertCard('Comfey','ENG','Psychic',1.31,764,1470)
insertCard('Gengar EX','ENG','Dark',4.67,94,104162)
insertCard('Glimmora EX','ENG','Fighting',1.85,970,213197)
insertCard('Mew EX','ENG','Psychic',16.90,151,193165)
insertCard('Gengar EX','ENG','Dark',21.43,94,193162)
insertCard('Wiglett','ENG','Water',6.50,960,206198)
insertCard('Greninja EX','ENG','Fighting',3.95,658,106167)
insertCard('Alakazam EX','ENG','Psychic',4.50,65,215091)
insertCard('Lapras EX','ENG','Water',2.50,131,32142)
insertCard('Fezandipiti EX','ENG','Dark',9.73,1016,38064)
insertCard('Lugia VMAX','ENG','Normal',3.43,249,139195)
insertCard('Quaxly','ENG','Water',9.99,912,206193)
insertCard('Paldean Student','ENG','Trainer',1.79,None,230091)
insertCard('Reshiram & Zekrom GX','ENG','Dragon',60.95,None,157236)
insertCard('Maushold','ENG','Normal',27.25,925,226193)
insertCard('Roaring Moon EX','ENG','Dark',2.53,1005,124182)
insertCard('Noivern EX','ENG','Dragon',2.47,715,220091)
insertCard('Altaria EX','ENG','Dragon',4.18,334,232182)
insertCard('Heatflame mask Ogerpon','ENG','Fire',1.60,1017,40167)
insertCard('Lairon','ENG','Steel',5.74,305,184167)
insertCard('Geeta','ENG','Trainer',2.71,None,218197)
insertCard('Slither Wing','ENG','Fighting',7.48,988,203182)
insertCard('Koreidon EX','ENG','Fighting',10.55,1007,245091)
insertCard('Nemona','ENG','Trainer',8.62,None,238091)
insertCard('Tulip','ENG','Trainer',4.50,None,244182)
insertCard('Pawmi','ENG','Electric',2.00,921,226091)
insertCard('Lilligant V','ENG','Grass',3.99,549,162189)
insertCard('Flygon EX','ENG','Fighting',4.93,330,222191)
insertCard('Clobbopus','ENG','Fighting',6.99,852,207191)
insertCard('Stunfisk','ENG','Electric',2.72,618,202191)
insertCard('Greavard','ENG','Psychic',11.98,971,214198)
insertCard('Charizard EX','ENG','Dark',21.99,6,228197)

insertCard('Hisuian Electrode V','JPN','Grass',1.62,101,5172)
insertCard('Blastoise EX','JPN','Water',2.03,9,9165)
insertCard('Mew V','JPN','Psychic',2.07,151,53172)
insertCard('Hisuian Voltorb','JPN','Grass',2.39,100,173172)
insertCard('Hisuian Goodra','JPN','Dragon',2.99,706,196172)
insertCard('Miltank','JPN','Normal',3.33,241,199172)
insertCard('Simisear V','JPN','Fire',1.58,514,20172)
insertCard('Arceus Vstar','JPN','Normal',2.07,493,127172)
insertCard('Deoxys','JPN','Psychic',5.25,386,185172)
insertCard('Zamazenta V','JPN','Steel',8.99,889,232172)
insertCard('Salamence EX','JPN','Dragon',40.92,373,129100)
insertCard('Zoroark','JPN','Dark',1.63,571,91172)
insertCard('Keldeo','JPN','Water',0.60,647,32172)
insertCard('Deoxys','JPN','Psychic',1.14,386,60172)
insertCard('Toxel','JPN','Electric',1.23,848,43172)
insertCard('Lapras','JPN','Water',1.70,131,23172)
insertCard('Miltank','JPN','Normal',3.33,241,199172)
insertCard('Radiant Gardevoir','JPN','Psychic',1.97,282,55172)



cursor.execute('SELECT * FROM Cards;')
cards = cursor.fetchall()

for card in cards:
    print(card)


def dropDuplicates():
    cursor.execute('''
        DELETE FROM Cards
        WHERE Card_ID NOT IN (
        SELECT MIN(Card_ID)
        FROM Cards
        GROUP BY Card_Name
        )   
    ''')
    

dropDuplicates()

conn.commit()
conn.close()