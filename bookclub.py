from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import sys

inviteLink = sys.argv[1]
nameBase = sys.argv[2]
numVotes = int(sys.argv[3])

browser = webdriver.Chrome()
browser.implicitly_wait(5)

for i in range(numVotes):
    email = "".join(random.choices(string.ascii_uppercase + string.digits, k=8)) + "@gmail.com"
    browser.get("https://bookclubs.com/signup")
    num = 3652 + i
    name = nameBase + " " + str(num)
    browser.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    browser.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys('password')
    browser.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
    browser.find_element(By.XPATH, "//a[@class='edit-profile-link'][normalize-space()='Edit Profile']")
    browser.get(inviteLink)
    browser.find_element(By.XPATH, "//button[normalize-space()='Explore The club']").click()
    browser.find_element(By.XPATH, "//button[normalize-space()='POLLS']").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn-vote:first-of-type").click()


