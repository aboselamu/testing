from RPA.Browser.Selenium import Selenium 
from robocorp.tasks import task

class BrowserManager:
    def __init__(self):
        self.browser = None

    #oppening the site aljazeera.com
    def opening_the_news_Site(self,url):
        global browser
        # logger.info("Opening the news site.")
        browser = Selenium(auto_close = False)
        
        # Define Chrome options to disable popup blocking
        options = [
            "--disable-popup-blocking",
            "--ignore-certificate-errors"
        ]

        

        # Open browser with specified options
        browser.open_available_browser(url, 
                                            browser_selection="Chrome", 
                                            options=options)
        # browser.close_all_browsers()
        # return browser
        print("oppend browser at last")


    def search_the_phrase(self):
        global browser
        print("inside search method")
        if(self.browser):
            print("found browser")
        else:
            print("not found browser")
        # logger.info(f"Searching the phrase: {phrase}")
        # if the site contains collecting cookies 
        try:
            print("inside tyr")
            sbrowser.click_button('Allow all')
            print("it clicked allow")

        except:
            print("it didn't clicked allow")
            pass
        # finding the serach icon and field
        phrase = "Business"
        locator1 = "//button[@aria-pressed='false']//*[name()='svg']"
        browser.wait_until_page_contains_element(locator1, timeout=10)
        browser.click_element(locator1)

        # inserting the search phrase in the input field
        browser.input_text("//input[@placeholder='Search']",phrase)
        browser.click_button("//button[@aria-label='Search Al Jazeera']")
        # browser.close_all_browsers()


        # Trying to find it there is a realated articles with the search phrase
        try:
            locator2 = "//select[@id='search-sort-option']"
            browser.wait_until_element_is_visible(locator2, timeout=10)
            browser.click_element(locator2)
        except:
            return "No news associated with the search phrase"

        # sort by time
        dropdown_locator = "//select[@id='search-sort-option']/option[1]" 
        browser.click_element(dropdown_locator)

        try:
            # browser.wait_until_element_is_visible("xpath://*[@id='main-content-area']/div[2]/div[2]", timeout=10)
            elements1 = browser.find_elements('css:.search-result__list')
            for element in elements1:
                print(element.text)  # Example action on each element
            print("YEs it worked")
        except Exception as e:
            print(e, "NOOOOOO it didn't find it")
@task
def main():
    bm = BrowserManager()
    url = "https://www.aljazeera.com/"
    bm.opening_the_news_Site(url)
    # br = bm.browser
    bm.search_the_phrase()
