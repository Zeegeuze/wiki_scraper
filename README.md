# Wikipedia Scraper
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Create a scraper that builds a JSON file with the political leaders of each country you get from this API.

Include in this file the first paragraph of the Wikipedia page of these leaders (you'll retrieve the Wikipedia page URL from the API, which you then have to scrape yourself).



## 📦 Repo structure

```
.
├── src/
│   └── scraper.py
├── .gitignore
├── main.py
├── leaders_data.json
├── requirements.txt
├── wikipedia_scraper.ipynb
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The script reads the API, will extract the urls from the leaders, after which we'll scrape the first paragraph of every leading from Wikipedia. Later on it will be saved to an "leaders_data.json" file in your root directory.

```python
input = [API](https://country-leaders.onrender.com)
output_filename = "leaders_data.json"

```
## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org.

Connect with me on [LinkedIn](https://www.linkedin.com/in/wouterverhaeghe/).
