from selenium import webdriver
from selenium.webdriver.common.by import By

def get_score(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text.strip())
        if score > 1 and score < 1000:
          return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        driver.quit()

# Example Usage
#url = "http://localhost:5000"
#score = get_score(url)
#print("Extracted Score:", score)
def main():
  url = "http://localhost:5000"  # Replace with the actual URL
  if get_score(url):
    exit(0)
  else:
    exit(-1)
#exit(exit_code)  # Exit with the appropriate code


#def main():
 # url = "http://localhost:5000"
  #score = get_score(url)
  #print("Extracted Score:", score)

main()