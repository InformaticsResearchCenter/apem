import speech_recognition as sr
def masuk():
        from selenium import webdriver 
        from selenium.webdriver.firefox.options import Options 
        opsi = Options() 
        opsi = webdriver.firefox.options.Options() 
        opsi.headless = False 
        cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX 
        cap['marionette'] = True 
        driver = webdriver.Firefox()
        driver.get("https://siap.poltekpos.ac.id") #19

def login():
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options 
        opsi = Options() 
        opsi = webdriver.firefox.options.Options() 
        opsi.headless = False
        cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX 
        cap['marionette'] = True 
        driver = webdriver.Firefox() 
        driver.get("https://siap.poltekpos.ac.id") #19
        driver.find_element_by_name('user_name').send_keys("1184030")
        driver.find_element_by_name('user_pass').send_keys("sariasih54")
        driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]/div/form/input[4]').click()
r= sr.Recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING, PLEASE")
    audio = r.listen(source)
try:
    print("TEXT : "+r.recognize_google(audio, language='id-ID'))
    x = "siap"
    y = "login siap"
    if (r.recognize_google(audio, language='id-ID')) == x:
        masuk()
    if (r.recognize_google(audio, language='id-ID')) == y:
        login()
except Exception as e:
    pass
 
print("Time is over, thanks")