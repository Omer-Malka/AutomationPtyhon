from selenium import webdriver


class Music():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\Program Files\ProgFiles\chromedriver.exe")

    def Play(self):
        name = input("enter a youtube channel name")
        self.driver.get("https://www.youtube.com/c/"+name+"/videos")

        new = self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[3]')
        new.click()


bot = Music()
bot.Play()
