import requests
import datetime
import pandas as pd

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

def getArtcilesByCategory(category, country):
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
        searchBy = input("Would you like to search by cateogory or country? \n").lower()
        if searchBy not in validSearchBy:
            print("Invalid input please enter \"cateogory\" or \"country\" \n")
        else:
            break
    
    if searchBy == "cateogory":
        while True:
            validCateogories = ("business", "entertainment", "general", "health", "science", "technology", "tech")
            category = input("What cateogory would you like? \n").lower()
            if category not in validCateogories:
                print("Invalid input please enter \"business\", \"entertainment\", \"general\", \"health\", \"science\", or \"technology\". \n")
            else:
                break
        
        if category == "tech":
            category = "technology"

        while True:
            validInputs = ("yes", "y", "no", "n")
            inputs = input("The default news region is U.S would you like to change it? \n")
            if inputs not in validInputs:
                print("Invalid input please enter \"yes\" or \"no\" \n")
            else:
                break
        if inputs == "y" or inputs == "yes":
            while True:
                region = input("What country would you like to focus on? \n")
                df = pd.read_excel("Country codes.xlsx")
                if region.lower() not in map(str.lower, df.values.flatten()):
                    print("Invalid input please enter a valid country code or country if you arent shure of the country code please use this chart https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing")
                    print("NOTE: Not all countries are supported please view the chart to check for the supported countries \n")
                else:
                    break
            print(f"Getting news for {category} in {region}...")
            print()
            getArtcilesByCategory(country=region, category=category)
            print()
            print(f"Successfully retrieved top {category} headlines in {region}")
        else:
            region = "us"
            print(f"Getting news for {category}...")
            print()
            getArtcilesByCategory(category=category, country=region)
            print()
            print(f"Successfully retrieved top {category} headlines")
    country = input("Enter your desired region for your news. \n")
    #print(f"Getting news for {category}...\n")
    #selection
    print(f"Successfully retrieved top {category} headlines")

    currenttime = datetime.datetime.now()
    date = currenttime.strftime("%m-%d")
    if date == "12-20":
        print("----------------------------------------------")
        print()
        print("Its 23rd of december!")
        print("Happy birthday!")
