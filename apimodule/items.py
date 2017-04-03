import requests
def getItem(apiKey, itemId):
    requestUri = "https://eu.api.battle.net/wow/item/%s?locale=en_GB&apikey=%s" % (itemId, apiKey)
    r = requests.get(requestUri);
    jsonData = r.json()
    return jsonData
