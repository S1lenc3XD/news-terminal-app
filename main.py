import requests
import datetime
import pandas as pd

# API key for accessing NewsAPI
API_KEY = 'YOUR_API_KEY'
# Base URL for NewsAPI
URL = ('https://newsapi.org/v2/top-headlines?')

# Function to get articles by country
def getArtcilesByCountry(country):
    queryparams = {
        "category": "general",
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

# Function to get articles by category and country
def getArtcilesByCategory(category, country):
    queryparams = {
        "category": category,
        "sortBy": "top",
        "country": country,
        "apiKey": API_KEY
    }
    return getArticles(queryparams)

# Function to make the API request and print the articles
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

# Main function to interact with the user and fetch news
if __name__ == "__main__":
    while True:
        # Prompt user to choose search by category or country
        while True:
            validSearchBy = ("category", "country")
            searchBy = input("Would you like to search by category or country? \n").lower()
            if searchBy not in validSearchBy:
                print("Invalid input please enter \"category\" or \"country\" \n")
            else:
                break

        # Handle search by category
        if searchBy == "category":
            while True:
                validCategories = ("business", "entertainment", "general", "health", "science", "technology", "tech")
                category = input("What category would you like? \n").lower()
                if category not in validCategories:
                    print("Invalid input please enter \"business\", \"entertainment\", \"general\", \"health\", \"science\", or \"technology\". \n")
                else:
                    break
            
            # Handle alias "tech" for "technology"
            if category == "tech":
                category = "technology"

            while True:
                validInputs = ("yes", "y", "no", "n")
                inputs = input("The default news region is U.S. Would you like to change it? \n").lower()
                if inputs not in validInputs:
                    print("Invalid input please enter \"yes\" or \"no\" \n")
                else:
                    break

            # Change region if user opts to do so
            if inputs == "y" or inputs == "yes":
                while True:
                    region = input("Enter your desired region for your news. \n")
                    df = pd.read_excel("Country codes.xlsx")
                    firstColumnValues = df.iloc[:, 0].astype(str).str.lower()
                    if region.lower() not in firstColumnValues.values:
                        print("Invalid input. Please enter a valid country code. If you aren't sure of the country code, please use this chart: https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing")
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

        # Handle search by country
        if searchBy == "country":
            while True:
                region = input("Enter your desired region for your news. \n")
                df = pd.read_excel("Country codes.xlsx")
                firstColumnValues = df.iloc[:, 0].astype(str).str.lower()
                if region.lower() not in firstColumnValues.values:
                    print("Invalid input. Please enter a valid country code. If you aren't sure of the country code, please use this chart: https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing")
                    print("NOTE: Not all countries are supported. Please view the chart to check for the supported countries \n")
                else:
                    break
            print(f"Getting news for {region}...")
            print()
            getArtcilesByCountry(region)
            print()
            print(f"Successfully retrieved top {region} headlines")

        # Prompt to rerun the program
        while True:
            validAnswer = ("yes", "y", "no", "n")
            answer = input("Would you like to re-run the program? \n").lower()
            if answer not in validAnswer:
                print("Invalid response please enter yes or no. \n")
            else:
                break
        if answer == "yes" or "y":
            print()
            print("----------------------------------------------")
        else:
            print("Program is closed.")
            break
