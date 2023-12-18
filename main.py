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
    searchBy = input("Would you like to search articles by country, category, or query")
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