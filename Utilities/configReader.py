from configparser import ConfigParser  # internal library


# config = ConfigParser()
# config.read("config.ini")       #giving file name
# print(config.get("locator","username"))             #provide the section you want to read and key in get()
# #it is like driver.find_element(By.XPATH)
# print(config.get("basic info", "testsiteurl"))

# create utility function for above code
def readConfig(section, key):
    config = ConfigParser()
    config.read("..//ConfigurationData//conf.ini")
    return config.get(section, key)

