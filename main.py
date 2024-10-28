meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROLF":"Una respuesta a una broma",
            "SHEESH":"Ligera desaprobacion",
            "CREEPY":"Aterrador, siniestro",
            "AGGRO":"Ponerse agresivo o enojado"
            }


word = input("Escribe una palabra que no entiendas").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No conozco esa palabra")
