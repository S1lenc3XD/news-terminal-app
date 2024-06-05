import requests
import datetime
import pandas as pd

API_KEY = 'YOUR_API_KEY'
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
                inputs = input("The default news region is U.S would you like to change it? \n").lower()
                if inputs not in validInputs:
                    print("Invalid input please enter \"yes\" or \"no\" \n")
                else:
                    break
            if inputs == "y" or inputs == "yes":
                while True:
                    region = input("Enter your desired region for your news. \n")
                    df = pd.read_excel("Country codes.xlsx")
                    firstColumnValues = df.iloc[:, 0].astype(str).str.lower()
                    if region.lower() not in firstColumnValues.values:
                        print("Invalid input please enter a valid country code if you aren't sure of the country code. Please use this chart https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing")
                        print("NOTE: Not all countries are supported. Please view the chart to check for the supported countries \n")
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
        if searchBy == "country":
            while True:
                region = input("Enter your desired region for your news. \n")
                df = pd.read_excel("Country codes.xlsx")
                firstColumnValues = df.iloc[:, 0].astype(str).str.lower()
                if region.lower() not in firstColumnValues.values:
                    print("Invalid input please enter a valid country code if you aren't sure of the country code. Please use this chart https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing")
                    print("NOTE: Not all countries are supported. Please view the chart to check for the supported countries \n")
                else:
                    break
            print(f"Getting news for {region}...")
            print()
            getArtcilesByCountry(region)
            print()
            print(f"Successfully retrieved top {region} headlines")

        currenttime = datetime.datetime.now()
        date = currenttime.strftime("%m-%d")
        if date == "12-23":
            print("----------------------------------------------")
            print()
            print("Its 23rd of december!")
            print("Happy birthday!")
        while True:
            validAnswer = ("yes", "y", "no", "n")
            answer = input("Would you like to re-run the pogram? \n").lower()
            if answer not in validAnswer:
                print("Invalid response please enter yes or no. \n")
            else:
                break
        if answer == "yes" or "y":
            print()
            print("----------------------------------------------")
        else:
            print("Pogram is closed.")
            break
