import requests
url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"starz","type":"series","genre":"18","page":"2","output_language":"en","language":"en"}

headers = {
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
    'x-rapidapi-key': "fafc23384amshdc1968c8fc5c789p1b4fc2jsnd415379c9973"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
file = open('series.txt')
file.write(response.text)  # No logré que me agregara los resultados al mismo archivo sin sobreescribirlo
file.close()
