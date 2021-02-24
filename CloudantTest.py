from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix", "R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13", connect=True)
client.connect()
databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))