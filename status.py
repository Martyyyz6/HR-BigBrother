#User's online status

from requests import Session

session = Session()

query = str


session.headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 Firefox/91.0"
session.headers["Authorization"] = "Bearer

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
