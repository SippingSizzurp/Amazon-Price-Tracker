
# Amazon Price Tracker  

## Project Overview  
The Amazon Price Tracker project is a Python-based framework designed to monitor the price of specific products on Amazon. When the price falls below a predetermined threshold, the framework can be extended to trigger alerts, integrate with broader systems, or handle multiple products. This utility simplifies price tracking for desired products, enabling users to make timely purchasing decisions.  

## Goal  
The primary goal of this project is to automate and streamline the process of monitoring product prices on Amazon, with support for scalability and integration into more complex systems.  

## Reasoning  
Manually checking product prices frequently is inconvenient and impractical, especially for multiple items. This project not only automates price tracking but also introduces an extendable structure for future enhancements and functionality.  

## How It Works  
1. **Product Tracker Setup**: The framework allows users to create tracker instances for specific Amazon product URLs.  
2. **Web Scraping**: The framework utilizes `requests` and `BeautifulSoup` to scrape the product's current price and title from the Amazon webpage.  
3. **Price Retrieval**: The extracted price is processed and returned for further use, such as notifications or logging.  
4. **Scalable Design**: The refactored class structure supports tracking multiple products simultaneously and offers easier integration with external systems.  

## Code Explanation  
- **Libraries Used**:  
  - `requests`: For sending HTTP requests to the Amazon product page.  
  - `BeautifulSoup` from `bs4`: For parsing HTML and extracting product data.  
  - `lxml`: A parser used by BeautifulSoup for handling the HTML.  

- **Framework Highlights**:  
  - **Class-Based Design**: Refactored from a script to a `Tracker` class, which encapsulates functionality for modularity and scalability.  
  - **Price Extraction**: Retrieves and processes product prices for comparison or logging.  
  - **Product Title Extraction**: Extracts and displays the product name for identification.  

## Acknowledgements  
This project builds upon the initial work of [Omerhalid](https://github.com/omerhalid/Amazon-Price-Tracker), whose script for scraping Amazon product prices provided a helpful foundation for web scraping functionality. While the original work focused on a single-product script, this version introduces a class-based design and extensibility to support broader use cases.  

## Disclaimer  
This project is intended for educational purposes. Please ensure compliance with Amazon's terms of service regarding web scraping.  

---  

*Track smarter, save better!*  

---  
