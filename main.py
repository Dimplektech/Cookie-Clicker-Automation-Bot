
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def setup_driver():
    """
       Sets up the Chrome WebDriver and navigates to the Cookie Clicker game.

       Returns:
           WebDriver: A configured Chrome WebDriver instance.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return driver


def get_item_ids(driver):
    """
        Retrieves the IDs of all upgrade items from the store.

        Args:
            driver (WebDriver): The WebDriver instance.

        Returns:
            list: A list of item IDs as strings.
    """
    # Get upgrade item ids
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    return [item.get_attribute("id") for item in items]

def get_prices(driver):
    """
        Extracts the prices of all upgrade items from the store.

        Args:
            driver (WebDriver): The WebDriver instance.

        Returns:
            list: A list of integer prices for each upgrade.
    """
    # Get all upgrade <b> tag
    all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_prices = []

    # Convert <b> into an integer
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            # Extract and convert the price from the text format "Name - Price"
            cost = int(element_text.split(" - ")[1].replace(",", ""))
            item_prices.append(cost)
    return item_prices

def get_cookie_count(driver):
    """
        Retrieves the current number of cookies from the game.

        Args:
            driver (WebDriver): The WebDriver instance.

        Returns:
            int: The current cookie count as an integer.
    """
    # Get current cookie count
    money_element = driver.find_element(By.ID, value="money").text
    money_element = money_element.replace(",", "")
    try:
        return  int(money_element)
    except ValueError:
        return  0 # return 0 if parsing fails



def get_affordable_upgrades(cookie_count, item_prices,item_ids):
    """
        Identifies the upgrades that can be afforded based on the current cookie count.

        Args:
            cookie_count (int): The current number of cookies.
            item_prices (list): List of item prices.
            item_ids (list): List of item IDs.

        Returns:
            dict: A dictionary of affordable upgrades with prices as keys and item IDs as values.
        """
    # Create dictionary to store item and prices
    cookie_upgrades = {}
    for n in range(len(item_prices)):
        cookie_upgrades[item_prices[n]] = item_ids[n]

    # Find upgrades that we can currently afford
    affordable_offers = {}
    for cost, id in cookie_upgrades.items():
        if cookie_count > cost:
            affordable_offers[cost] = id
    return affordable_offers

def purchase_upgrade(driver,to_purchase_id ):
    """
       Purchases an upgrade by clicking on its ID.

       Args:
           driver (WebDriver): The WebDriver instance.
           to_purchase_id (str): The ID of the upgrade to be purchased.
    """
    driver.find_element(By.ID, value=to_purchase_id).click()


def main():
    """
    Main function that automates clicking the cookie and purchasing upgrades.
    """

    driver = setup_driver()  # Initialize the WebDriver and open the game
    coockie = driver.find_element(By.ID, value="cookie") # Locate the cookie element
    item_ids = get_item_ids(driver) # Get the IDs of all available upgrades

    timeout_start = time.time() # Record the start time
    timeout_interval = 5 # Set the interval for checking upgrades (in seconds)
    next_check_time = timeout_start + timeout_interval  # Calculate the time for the next check
    five_mins = timeout_start + 60*5 # Set the total runtime to 5 minutes


    while True:
        coockie.click() # Simulate a click on the cookie

        # Check if it's time to evaluate and purchase upgrades
        if time.time() > next_check_time:
            item_prices = get_prices(driver) # Get the current prices of upgrades
            coockie_count = get_cookie_count(driver) # Get the current cookie count

            # Get upgrades that can be afforded
            affordable_offers =get_affordable_upgrades(coockie_count,item_prices,item_ids)
            # Purchase the most expensive affordable upgrade
            if affordable_offers:
                # Find and purchase the most expensive affordable upgrade
                highest_price_affordable_upgrade = max(affordable_offers)
                purchase_upgrade(driver, affordable_offers[highest_price_affordable_upgrade])

            # Update the time for the next check
            next_check_time = time.time() + timeout_interval

        # Break the loop after 5 minutes
        if time.time() > five_mins:
            break

    cookies_per_second = driver.find_element(By.ID,value="cps").text
    print(cookies_per_second)


if __name__ =="__main__":
    main()




