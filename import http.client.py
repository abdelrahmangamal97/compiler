import http.client

conn = http.client.HTTPSConnection("food-ingredients-by-pti.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "food-ingredients-by-pti.p.rapidapi.com",
    'x-rapidapi-key': "f1dbcc9311msh3db24262fb0a1cdp171ad4jsnca34670c7b6a"
    }

conn.request("GET", "/api/1.0/FoodIngredients/GetCommonIngredients", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))