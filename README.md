
# Cars24-ScrapeAndAnalyze

This project involves scraping used car listings from the Cars24 website using Selenium, and converting the scraped data into a structured DataFrame for further analysis or data processing.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

The **Cars24 Used Cars Scraper** automates the process of collecting data on used cars listed on the Cars24 website. This includes scraping essential details such as:

- Car Make and Model
- Price
- Year of Manufacture
- Kilometers Driven
- Fuel Type
- Transmission
- Location

After scraping, the data is stored in a Pandas DataFrame for easy manipulation and analysis.

## Technologies Used

- **Python**: The primary language used for scripting.
- **Selenium**: Used for web scraping to automate browser actions.
- **Pandas**: For handling the data, including converting the scraped data into a DataFrame.
- **ChromeDriver**: WebDriver for automating Chrome browser.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhaveshk22/Cars24-ScrapeAndAnalyze.git
cd Cars24-ScrapeAndAnalyze
```

### 2. Install Dependencies

It is recommended to create a virtual environment before installing the required packages.

```bash
pip install -r requirements.txt
```

### 3. Setup Selenium WebDriver

Ensure you have installed the ChromeDriver that matches your Chrome browser version. You can download it from [here](https://sites.google.com/chromium.org/driver/).

Make sure that the ChromeDriver executable is in your system's PATH.

## Usage

1. **Run the Scraper**: The script `scraping.py` handles the entire scraping process.
    ```bash
    python scraping.py
    ```

2. **Data Output**: Once the script finishes running, the scraped data is converted into a Pandas DataFrame, which can be further processed or exported to a file such as CSV.



3. **Customizing Scraping Logic**: You can modify the `scraping.py` script to target specific pages or add more details to be scraped.

## Future Enhancements

- Implement more robust error handling and retries for failed page loads.
- Integrate dynamic user-agent rotation to avoid being blocked by the website.
- Add functionality to scrape data from other pages or filter based on specific criteria.
- Store the data in a database instead of a CSV file for more efficient querying.
