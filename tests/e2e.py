from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException

def get_score(url):
    """Fetches the score from the webpage and returns True if valid, False otherwise."""
    driver = None
    try:
        driver = webdriver.Chrome()  # Initialize WebDriver
        driver.get(url)  # Open the webpage

        # Try to find the score element
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        # Ensure score is a valid integer
        score = int(score_text)

        # Validate score range
        return 1 < score < 1000

    except NoSuchElementException:
        print("❌ Error: 'score' element not found on the page.")
    except ValueError:
        print(f"❌ Error: Unable to convert '{score_text}' to an integer.")
    except WebDriverException as e:
        print("❌ WebDriver Error: The site may be unavailable or invalid URL.", e)
    except Exception as e:
        print("❌ Unexpected Error:", e)
    finally:
        if driver:
            driver.quit()  # Ensure WebDriver closes properly

    return None  # Return None in case of failure

def main():
    """Main function to execute the test and exit with appropriate code."""
    url = "http://localhost:8777"
    result = get_score(url)

    if result is True:
        exit(0)  # Success
    else:
        exit(-1)  # Failure

if __name__ == "__main__":
    main()
