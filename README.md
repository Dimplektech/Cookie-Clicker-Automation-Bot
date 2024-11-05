# Cookie Clicker Automation Bot

This project is a Python script that automates the Cookie Clicker game using Selenium. The bot continuously clicks the cookie and purchases the most expensive affordable upgrades to optimize the cookie production rate.

## Features

- Automatically clicks the cookie at high speed.
- Periodically checks for available upgrades and purchases the most expensive one that can be afforded.
- Runs for a set duration (default is 5 minutes).
- Reports the cookies per second (CPS) rate after running.

## Prerequisites

- Python 3.x installed
- Google Chrome installed
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatible with your Chrome version
- `selenium` Python package

## Installation

1. **Clone the repository or download the script**:
    ```bash
    git clone https://github.com/your-username/cookie-clicker-bot.git
    cd cookie-clicker-bot
    ```

2. **Install the required Python packages**:
    ```bash
    pip install selenium
    ```

3. **Ensure `chromedriver` is in your system path** or place it in the project directory.

## Usage

1. Run the Python script:
    ```bash
    python main.py
    ```

2. The bot will:
    - Open the Cookie Clicker game in Chrome.
    - Start clicking the cookie.
    - Purchase upgrades at regular intervals to maximize cookie production.
    - Stop after 5 minutes and display the cookies per second (CPS) rate.

## Code Overview

The main script is organized into functions for clarity and modularity:

- **`setup_driver()`**: Initializes and returns the Selenium WebDriver.
- **`get_item_ids(driver)`**: Retrieves IDs of all upgrade items.
- **`get_prices(driver)`**: Extracts the prices of available upgrades.
- **`get_cookie_count(driver)`**: Gets the current number of cookies.
- **`get_affordable_upgrades(cookie_count, item_prices, item_ids)`**: Returns a dictionary of upgrades that can be afforded.
- **`purchase_upgrade(driver, upgrade_id)`**: Purchases the specified upgrade.
- **`main()`**: Controls the main automation loop and logs the CPS at the end.

## Example Output
Cookies per second: 60

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request.

## Troubleshooting

- **ChromeDriver Version Mismatch**: Ensure that the `chromedriver` version matches your installed Chrome version.
- **Selenium Version**: Use the latest version of Selenium to avoid compatibility issues.



*Happy Clicking!*


