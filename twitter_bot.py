from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login/')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(6)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(10)
        for i in range(1,3):
            time.sleep(10)
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(20)
        #tweets = bot.find_element_by_xpath('//*[@data-testid="tweet"]')
        tweetLinks = [elem.get_attribute('href') for elem in bot.find_elements_by_xpath("//a[@dir='auto']")]
        FilteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))
        print(len(FilteredLinks))
        print(FilteredLinks)
        for link in FilteredLinks:
            bot.get(link)
            time.sleep(3)
            try:
                bot.find_element_by_xpath('//*[@data-testid="like"]').click()
                time.sleep(10)
            except Exception as ex:
                time.sleep(60)


botObject = TwitterBot('username', 'password') #Replace With Username and Password
botObject.login()
queries = ['lockdown4', 'ferrari', 'covid', 'corona', 'mobile photography', 'architecture photography', 'wildlife photography', 'product photography']
for query in queries:
    botObject.like_tweet('query')