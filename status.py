#User's online status

from requests import Session

session = Session()

query = str


session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0"
session.headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInVzZXJfaWQiOjI0NDY0MjJ9.eyJpc3MiOiJldmVyc2tpZXMuY29tIiwiYXVkIjoiYXV0aCIsImp0aSI6IlFaWGpQSkVtLUFPa3BtajFYaG5xZEE0Wk1ZbGtGXzhvIiwiaWF0IjoxNjQ3MTgxNTUzLjAxMjk5NCwibmJmIjoxNjQ3MTgxMjUzLjAxMjk5NywiZXhwIjoxNjQ3MjY3OTUzfQ.2ZSoYhCXTkh3-R8O2DeLIf-Vb0fZWQC99OYt8T-2J0k"


def func1(session:Session, query:str) -> dict:
  results = session.get(f"https://api.everskies.com/search?query={query}").json()
  return results

def func2(session:Session, query:str) -> dict:
  results = func1(session, query)
  for i in results["users"]:
    if i["alias"] == query:
      return i
#func2(session, "")


def func3(session:Session, query:str) -> int:
    
    results = func2(session, query)["presence"]