import requests
def getDumpFile(apiKey):
    requestUri = "https://eu.api.battle.net/wow/auction/data/azjol-nerub?locale=en_US&apikey=%s" % apiKey
    r = requests.get(requestUri);
    jsonData = r.json()
    try:
        fileData = jsonData["files"][0]
        return fileData
    except:
        return None
    return jsonData
