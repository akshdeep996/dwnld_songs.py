import string
from selenium import webdriver
from pyvirtualdisplay import Display



print("Please enter song name")
a = input()
cap = string.capwords(a)

diff = a.split(" ")
comb = "+".join(diff)

display = Display(visible=0, size=(800,600))
display.start()

b = webdriver.Firefox()
b.get("http://mp3-skulls.net/music/search.php?ty=" + comb + "&sh=Song")


elem = b.find_element_by_xpath('//strong[contains(text(),"%s")]' % cap)
elem.click()	



elemen = b.find_element_by_xpath('//a[contains(text(),"Download In High Quality [128 kpbs]")]')
elemen.click()


newurl = b.current_url

b.quit()
display.stop()

import requests

res = requests.get(newurl)

res.raise_for_status()

file_name = comb + ".mp3"

music = open(file_name,"wb")

for chunk in res.iter_content(100000):
	music.write(chunk)

music.close()


from twilio.rest import TwilioRestClient
	

accountSID = 'AC44a06791903b9b513c48ca1d2ea4efa5'
authToken = '8d80926d94f72ccc36aebbf7cd1cc2b9'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+12017304733'
myCellPhone = '+919632402156'
message = twilioCli.messages.create(body= " " + comb + 'Song has been succesffuly downloaded', from_=myTwilioNumber, to=myCellPhone)

