import requests
from datetime import datetime

ELEVATOR_SERIAL = 111222333444555
SERVER_URL = "https://pupperupper.pockethost.io/api/"

def PostWeight(weight):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    weightobject = {"weight": weight, "when": date_time}
    weightreturn = requests.post(SERVER_URL + "collections/weightrecord/records", json = weightobject)
    # print(weightreturn)
    # print(weightreturn.json())
    newWeightID = weightreturn.json()["id"]
    AppendWeight(newWeightID)

def AppendWeight(weightID):
    elevatorreturn = requests.get(SERVER_URL + "collections/elevators/records/" + str(ELEVATOR_SERIAL))
    # print(elevatorreturn)
    # print(elevatorreturn.json())

    newweights = elevatorreturn.json()["weights"]
    # print(newweights)
    newweights.append(weightID)
    # print(newweights)
    newweightobject = {"weights": newweights}

    patchreturn = requests.patch(SERVER_URL + "collections/elevators/records/" + str(ELEVATOR_SERIAL), json=newweightobject)
    # print(patchreturn)
    # print(patchreturn.json())

    
    