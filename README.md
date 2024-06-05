# News Terminal CLI App

This is a Python script to fetch the latest news headlines based on country or category using the NewsAPI.

## Features

- Fetch top news headlines by country
- Fetch top news headlines by category
- User interaction through command line input
- Supports dynamic region selection based on country codes
- Default region set to the United States (US)
- Handles invalid inputs and provides guidance

## Requirements

- Python 3.x
- `requests` library
- `pandas` library
- NewsAPI API Key
- Country codes Excel file

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/S1lenc3XD/news-terminal-app.git
    cd news-fetcher
    ```

2. Install the required libraries:
    ```sh
    pip install requests pandas
    ```

3. Download the country codes Excel file and place it in the same directory as the script. You can find the file [here](https://drive.google.com/file/d/10pvX9LGwFeEPzCF11TSX0FOH5K3TbtX9/view?usp=sharing).

## Usage

1. Open the script file and replace `API_KEY` with your NewsAPI key:
    ```python
    API_KEY = 'your_api_key_here'
    ```

2. Run the script:
    ```sh
    python news_fetcher.py
    ```

3. Follow the on-screen prompts to search for news by category or country.

## Example

```sh
$ python news_fetcher.py
Would you like to search by category or country?
category
What category would you like?
technology
The default news region is U.S would you like to change it?
yes
Enter your desired region for your news.
gb
Getting news for technology in gb...

Successfully retrieved top technology headlines in gb
