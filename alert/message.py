import requests
# import pandas as pd
from twilio.rest import Client
# from pprint import pprint

def message(lat,long,alert,desc):
    # # Getting users location
    # response = requests.get('https://ipinfo.io')
    # data = response.json()
    # location = data['loc']
    # locations = location.split(",")

    # User info
    USER_NUMBER = '+13603398754'
    USER_LOCATION = {
        "long": float(lat),
        "lat": float(long),
    }
    account_sid = "AC7befda2a371151927345c3a878d639a4"
    auth_token = "863eb3737a9e0b7cf7419d1fb394ea0c"

    
    # For Real Case Sceneriao, the scripts searches for the nearest service provider and send the alert along with the description and google map location
    # services_contacts = []
    # service_provider = None

    # if alert == "accident":
    #     data_file1 = pd.read_csv(r"C:\Users\raseek\Desktop\folder\hack\report\alert\hospital_list.csv")
    #     data_file2 = pd.read_csv("police_list.csv")
    #     service_provider1 = data_file1.to_dict(orient="records")
    #     service_provider2 = data_file2.to_dict(orient="records")
    #     service_provider = service_provider1 + service_provider2

    # elif alert == "crime":
    #     data_file = pd.read_csv(r"C:\Users\raseek\Desktop\folder\hack\report\alert\police_list.csv")
    #     service_provider = data_file.to_dict(orient="records")

    # print(service_provider)
    # # Searching and saving all the available service providers
    # for available in service_provider:
    #     if abs(USER_LOCATION["long"] - available["Longitude"]) < 0.05 and \
    #             abs(USER_LOCATION["lat"] - available["Latitude"]) < 0.05:
    #         services_contacts.append(str(available["Phone no."]))

    # pprint(services_contacts)

    client = Client(account_sid, auth_token)
    map = f"https://www.google.com/maps/@{lat},{long},15z?entry=ttu"
    message = client.messages.create(
            body=f'Hello there is {alert} emergency at long:{USER_LOCATION["long"]}, '
                 f'lat:{USER_LOCATION["lat"]} Description: {desc} .Location:{map}please send all the required help.',
            from_=USER_NUMBER,
            to=f"+9779861437533"  # Since we are using free api we are only sending email to one registered contact for demo
        )  #

    # # Calling the service providers
    # for contact in services_contacts:
    #     message = client.messages.create(
    #         body=f'Hello there is emergency {alert} in long:{USER_LOCATION["long"]}, '
    #              f'lat:{USER_LOCATION["lat"]} please send all the required help.',
    #         from_=USER_NUMBER,
    #         to=f"+9779842554249"  # Since we are using free api we are only sending email to one registered contact for demo
    #     )  # if subscription is bought in twilio api code->  to=f"+977{contact}" which can notify any contact
    
    # print("message send")


# authid = "AC7befda2a371151927345c3a878d639a4"
# authToken = "863eb3737a9e0b7cf7419d1fb394ea0c"
# message(24.564556,84.563569,authid,authToken)