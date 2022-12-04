import phonenumbers
number = "+919450278176"

from phonenumbers import geocoder
from phonenumbers import carrier

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en",  region="US"))
service_number = phonenumbers.parse(number)



