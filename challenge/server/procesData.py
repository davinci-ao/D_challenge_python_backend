import json
LOCATION = "data/"

# schrijf order als JSON file in de map DATA.
def writeOrder(orderDict: dict):
    # check orderid, wordt gebruikt om bestand op te slaan.
    try:
        fileName = LOCATION + str(orderDict['orderId']) + '.json'
    except KeyError:
        raise ValueError('Key orderId not found in file.')
    try:
        with open(fileName, "x") as outfile:
            json.dump(orderDict, outfile)
    except FileExistsError:
        raise ValueError(f'File {fileName} already exists!') from None

# geef een JSON file terug op basis van een orderID.
def getOrder(orderId: str) -> dict:
    fileName = LOCATION + orderId + '.json'
    try:
        with open(fileName, "r") as readFile:
            return json.load(readFile)
    except FileNotFoundError:
        raise ValueError(f'File with name {fileName} does not exists!') from None


def generateInvoice(orderId: str) -> dict:
    invoice = {'orderId': orderId,
               'orderRegels': ['3 fris a 2.95 = 8.85', '2 bier a 3.15 = 6.30'],
               'totaalBedrag': 18.15,
               'totaalBTWBedrag': 2.63}
    # todo:
    # 1 haal order gebaseerd op id
    # 2 bereken de factuur en geef deze terug, zoals voorbeeld.
    return invoice



# deze code staat er alleen om de functies te testen en kun je eventueel gebruiken.
# dictionary ={
#     'orderId': 123456,
#     "bier" : 3,
#     "wijn" : 2,
#     'fris': 5,
#     "kortingsPercentage" : 10,
#     "BTW" : 9
# }
#
# writeOrder(dictionary)
# print(getOrder(str(123456)))