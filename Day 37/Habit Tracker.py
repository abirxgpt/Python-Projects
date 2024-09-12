import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "cherryabir06092004"
USERNAME = "mizirah"


pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }

# response = requests.post(url=pixela_endpoint,json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPHID = "graph0"

graph_parameters = {
    "id": GRAPHID,
    "name": "Python Code",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN.encode('utf-8'),
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

what_to_do = input("What you want to do?\n1. Today's Tracker(Press T) \n2. Another Day Tracker(Press N)\n3. Update Tracker(Press U)\n4. Delete Tracker(Press D)\n: ")

if what_to_do == "T":
    pixl_endpoint = f"{graph_endpoint}/{GRAPHID}"

    Today = datetime.datetime.now()
    no_of_hours = input(f"Today's Date {Today.strftime('%Y/%m/%d')}\nEnter No of Hours: ")

    pixl_params = {
        "date": Today.strftime("%Y%m%d"),
        "quantity": no_of_hours,
    }

    response = requests.post(url=pixl_endpoint, json=pixl_params, headers=headers)
    print(response.text)

elif what_to_do == "N":
    pixl_endpoint = f"{graph_endpoint}/{GRAPHID}"

    date = ("").join(input("Enter Date to Add in YYYY/MM/DD Format: ").split("/"))
    no_of_hours = input(f"Enter No of Hours: ")

    pixl_params = {
        "date": date,
        "quantity": no_of_hours,
    }

    response = requests.post(url=pixl_endpoint, json=pixl_params, headers=headers)
    print(response.text)

elif what_to_do == "U":
    update_date = ("").join(input("Enter Date to Update in YYYY/MM/DD Format: ").split("/"))
    update_endpoint = f"{graph_endpoint}/{GRAPHID}/{update_date}"
    update_quantity = input("Enter Quantity to Update in Float: ")

    update_params = {
        "quantity": update_quantity
        }

    response = requests.put(url=update_endpoint, json=update_params, headers=headers)
    print(response.text)

elif what_to_do == "D":
    delete_date = ("").join(input("Enter Date to Delete in YYYY/MM/DD Format: ").split("/"))
    delete_endpoint = f"{graph_endpoint}/{GRAPHID}/{delete_date}"

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)
else :
    print("Enter a Correct Task to do !!")

