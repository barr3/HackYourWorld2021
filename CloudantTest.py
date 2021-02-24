from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix",
                      "R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13", connect=True)
client.connect()
databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

testData = [["BigMac", 1000, "Beskrivnings test"],
            ["Sallad", 200, "Coolare än BigMac"]]

# skriv in datan i json och skicka till databasen
for data in testData:
    jsonDoc = {
        "namn": data[0],
        "co2": data[1],
        "beskrivning": data[2]
    }
    newDoc = myDatabaseDemo.create_document(jsonDoc)

if (newDoc.exists()):
    print('new doc created')

# hämta data från alla document
result = Result(myDatabaseDemo.all_docs, include_docs=True)
print(format(result[0]))
