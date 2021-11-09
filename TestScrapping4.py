import urllib.request
import json
#import pandas as pd

with urllib.request.urlopen("https://api.watchmode.com/v1/list-titles/?apiKey=sNULUKwn6pkKlQ4qJmSxRblSdh7lZolOfpfTwVrY&source/starz&page=2") as url:  #  para cambiar de página sólo se cambia el número final del url
    data = json.loads(url.read().decode())

movies = json.dumps(data, indent=4)
print(movies)
file = open('movies.csv', 'a')
file.write(movies)
file.close()
