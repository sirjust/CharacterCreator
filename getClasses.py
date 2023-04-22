import requests

def main():
    response = requests.get('https://dnd5eapi.co/api/classes')
    # print(response.status_code)  # prints the status code of the response

    apiResponse = response.json()
    # print(response.json())  # prints the JSON content of the response

    return apiResponse['results']