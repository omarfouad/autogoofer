from utils.WebDriver import WebDriver
from os import system
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format


browser = WebDriver(dev=False)
system('cls')
cprint(figlet_format('AutoGoofer', font='slant'), 'green', attrs=['bold'])
cprint('Executing Script. Please hold on...', 'green')

browser.get('https://youtube.com/goofer')

subs = browser.find_element_by_xpath('//*[@id="subscriber-count"]')
subCount = subs.text
browser.quit()
cprint('Done! --------------------------------------', 'blue')
cprint("You Have " + subCount + " on YouTube", 'yellow')
system("pause")