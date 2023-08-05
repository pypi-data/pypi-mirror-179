import validators
from validators import ValidationFailure
import re
import phonenumbers

def is_string_an_url(url_string: str) -> bool:
    result = validators.url(url_string)

    if isinstance(result, ValidationFailure):
        return False

    return result

def basic_clean_address(raw_data):
	"""
	# Basic Cleaner of The Text From Address
	
	- Remove duplicates words in address delimated with comma
	- Strip spaces from each word and remove multiple commas
	lower all values
	"""
	all_words_in_address = [raw_str.strip(' -+/\\:;,') for raw_str in str(re.sub(r'\s+', ' ',str(raw_data).strip(' -+/\\:;,'))).split(',')]
	length = len(all_words_in_address)
	if length == 1:
		return all_words_in_address[0].replace(' ', '')
	elif length == 0:
		return ''
	else:
		new_list = list()
		new_list_lower = list()
		for word in all_words_in_address:
			if word not in ['', ' ']:
				if word.strip().lower() not in new_list_lower:
					new_list_lower.append(word.strip().lower())
					new_list.append(word.strip())

		return ','.join(new_list)

def retrieve_emails(raw_data):
	"""
	# Retrieve all the emails in raw_data as list
	"""
	raw_data = str(raw_data)
	words_in_address = raw_data.replace(' ', ',').split(',')
	emails_found = list()
	
	for word in words_in_address:
		if ('@' in word) and ('.' in word):
			if ' ' not in word.lower().strip():
				emails_found.append(word.lower().strip())

	return emails_found

def retrieve_urls(raw_data):
	"""
	# Retrieve all the emails in raw_data as list
	"""
	raw_data = str(raw_data)
	words_in_address = raw_data.replace(',', '').split()
	urls_found = list()
	
	for word in words_in_address:
		if ('@' not in word) and ('.' in word):
			if ' ' not in word.strip():
				urls_found.append(word.strip())

	return urls_found

def retrieve_phone_numbers(raw_data, raw=False, country_code='IN'):
	"""
	This function will retrieve Phone Numbers from complete text and return a list

	Example Given Below
	
	```python
	>>> retrieve_phone_numbers("Call me at 1800-202-2022 if it's before 9:30, or on 703-4800500 after 10am.")
	['18002022022', '7034800500']
	```
	"""
	raw_data = str(raw_data)
	phone_numbers_found = list()
	for match in phonenumbers.PhoneNumberMatcher(raw_data, country_code):
		if raw == False:
			phone_numbers_found.append(str(match.number.national_number))
		else:
			phone_numbers_found.append(str(match.raw_string))
	
	return phone_numbers_found

def remove_phone_numbers(raw_data, country_code='IN'):
	"""
	This function will retrieve Phone Numbers from complete text and return a list

	Example Given Below
	
	```python
	>>> retrieve_phone_numbers("Call me at 1800-202-2022 if it's before 9:30, or on 703-4800500 after 10am.")
	['18002022022', '7034800500']
	```
	"""
	raw_data = str(raw_data)
	for match in phonenumbers.PhoneNumberMatcher(raw_data, country_code):
		raw_data = raw_data.replace(str(match.raw_string), '')
	
	return basic_clean_address(raw_data)

