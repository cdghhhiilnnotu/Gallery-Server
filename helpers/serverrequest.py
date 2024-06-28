import requests, json

api_json = requests.get("https://cdghhhiilnnotu.github.io/Gallery-Server/api.json")

json_object = json.dumps(api_json.json(), indent=4)
 
# Writing to sample.json
with open("api1.json", "w") as outfile:
    outfile.write(json_object)

# print(api_json.json())


