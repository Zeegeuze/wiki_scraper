from src.scraper import *

# Part 1: API
# 1. Identify the root of the API
root = "https://country-leaders.onrender.com"
print("Root set")

# 2. We initiate the scraping object
scrape = Scraping()
print("Scraping object initiated")

# 2. Check status API
valid_or_error = scrape.check_status_valid(root)

if valid_or_error != True:
    print(valid_or_error)
    quit()
else:
    print("Session valid")

# 3. Get a list of the leadres with their url
leaders = scrape.get_leaders(root)
print("Leaders collected")

# 3. Get a list of all the leaders with the first paragraph
leaders_per_country = scrape.get_first_paragraph(leaders)
print("All paragraphs collected")

# 4. Save the leaders into a json file
scrape.save(leaders_per_country)
print("Json saved")

# 5. Save file as csv file
scrape.save_as_csv(leaders_per_country)
print("Csv saved")
