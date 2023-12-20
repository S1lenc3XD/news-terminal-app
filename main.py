import requests
import datetime
import pandas

API_KEY = '80996256c1fb47b98033a5ec76b2b377'
URL = ('https://newsapi.org/v2/top-headlines?')

def getArtcilesByCountry(country):
    queryparams = {
        "category": "general",
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArtcilesByCategory(category):
    queryparams = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArtcilesByQuery(query):
    queryparams = {
        "q": query,
        "sortBy": "top",
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArticles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

if __name__ == "__main__":
    import requests
import datetime

API_KEY = '80996256c1fb47b98033a5ec76b2b377'
URL = ('https://newsapi.org/v2/top-headlines?')

def getArtcilesByCountry(country):
    queryparams = {
        "category": "general",
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArtcilesByCategory(category):
    queryparams = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArtcilesByQuery(query):
    queryparams = {
        "q": query,
        "sortBy": "top",
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

def getArticles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

if __name__ == "__main__":
    while True:
        validSearchBy = ("cateogory", "country")
        searchBy = input("Would you like to search by cateogory or country? ").lower()
        if searchBy not in validSearchBy:
            print("Invalid input please enter \"cateogory\" or \"country\". \n")
        else:
            break
    
    country = input("Enter your desired region for your news. \n")
    if searchBy == "cateogory":
        while True:
            validCateogories = ("business", "entertainment", "general", "health", "science", "technology")
            category = input("What cateogory would you like? \n").lower()
            if category not in validCateogories:
                print("Invalid input please enter \"business\", \"entertainment\", \"general\", \"health\", \"science\", or \"technology\". \n")
            else:
                break
        if category == "tech":
            category = "technology"
        while True:
            validInputs = ("yes", "y", "no", "n")
            inputs = input("The default news region is U.S would you like to change it?")
            if inputs not in validInputs:
                print("Invalid input please enter \"yes\" or \"no\"")
            else:
                break
        getArtcilesByCategory(category)
    #print(f"Getting news for {category}...\n")
    #selection
        print(f"Successfully retrieved top {category} headlines")

    currenttime = datetime.datetime.now()
    date = currenttime.strftime("%m-%d")
    if(date == "12-15"):
        print("Hello")
    country = input("Enter your desired region for your news. \n")
    category = input("What cateogory would you like? \n")
    getArtcilesByCategory(category)
    #print(f"Getting news for {category}...\n")
    #selection
    #print(f"Successfully retrieved top {category} headlines")

    currenttime = datetime.datetime.now()
    date = currenttime.strftime("%m-%d")
    if(date == "12-15"):
        print("Hello")
