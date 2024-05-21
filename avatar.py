#Will send a PNG(image) of a player's current avatar

from requests import Session
import base64
import json


session = Session()
session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0"
session.headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInVzZXJfaWQiOjI2Nzg1NTl9.eyJpc3MiOiJldmVyc2tpZXMuY29tIiwiYXVkIjoiYXV0aCIsImp0aSI6IkQ4V1F5MWNfd0pVcnItUWJFQU1Oc1RJbndpc2JPb053IiwiaWF0IjoxNjQ4Mjk3MDM4Ljg0OTU4NiwibmJmIjoxNjQ4Mjk2NzM4Ljg0OTU4OSwiZXhwIjoxNjQ4MzgzNDM4fQ.-CVdcM-eUPx3qkrEP4NfA4SoPqqIjVbYujna4cWc4jw"

#Query being the user input
query = str
render = "https://cdn.everskies.com/render/"


def func4(session:Session, query:str):
  results = session.get(f"https://api.everskies.com/search?query={query}").json()
  return results

#Function to search for usernames
def func5(session:Session, query:str):
  results = func4(session, query)
  for i in results["users"]:
    if i["alias"] == query:
      return i


def func6(session:Session, query:str):
  results = func5(session, query)["outfit"]