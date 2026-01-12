import requests
import time
import bs4

url = 'https://dskbank.bg/car-giveaway'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

while True:
    try:
        session = requests.Session()
        response = session.get(url, headers=headers)
        if response.status_code != 200:
            print(f'Failed to fetch page: {response.status_code}')
            time.sleep(3600)
            continue
        
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'name': 'defaultFormctl00$Main$C180'})
        if not form:
            print('Form not found')
            time.sleep(3600)
            continue
        
        data = {}
        for inp in form.find_all('input'):
            name = inp.get('name')
            if name:
                value = inp.get('value', '')
                data[name] = value
        
        # Override with our data
        data['TextFieldController_0'] = 'Алекс Иванов Цветанов'
        data['TextFieldController_1'] = '0248126408'
        data['CountryPhoneCode'] = '+359'
        data['MobileNumber'] = '988329931'
        data['MobileOperator'] = '4'
        data['CheckboxesFieldController'] = 'Yes'
        data['MobileNumberSelectorController'] = '+359 988329931'
        
        submit_response = session.post(url, data=data, headers=headers)
        
        print(f'Submission at {time.ctime()}: Status {submit_response.status_code}')
        if submit_response.status_code == 200:
            print('Submission successful Alex')
        else:
            print('Submission failed Alex')
        data['TextFieldController_0'] = 'Кирил Георгиев Вълков'
        data['TextFieldController_1'] = '0346106685'
        data['CountryPhoneCode'] = '+359'
        data['MobileNumber'] = '877691277'
        data['MobileOperator'] = '4'
        data['CheckboxesFieldController'] = 'Yes'
        data['MobileNumberSelectorController'] = '+359 877691277'
        submit_response = session.post(url, data=data, headers=headers)

        print(f'Submission at {time.ctime()}: Status {submit_response.status_code}')
        if submit_response.status_code == 200:
            print('Submission successful Kiril')
        else:
            print('Submission failed Kiril')
    except Exception as e:
        print(f'Error: {e}')
    time.sleep(3600)  # Wait 1 hour
