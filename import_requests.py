import requests
from requests import get
from bs4 import BeautifulSoup as bsoup
import pandas as pd 
import numpy as np 

from time import sleep
from random import randint

#initialize storage
agent_name = []
verification = []
address = []
registration_date = []
phone_number = []
whatsapp_number = []

pages = np.arange(0, 1430)



for page in pages:
    page_s = requests.get('https://www.propertypro.ng/agents?page='+ str(page))
    
    soup = bsoup(page_s.text, 'html.parser')
    
    agents = soup.find_all('div', class_="agent-rp-inner")

    #sleep(randint(2,9))
    
    for agent in agents:
        container = agent.find_all('div',class_='rp-left-text')
        name = container[0].h2.a.text
        agent_name.append(name)

        verified_container = agent.find_all('div',class_='rp-inner-img')
        verified = verified_container[0].div.img if agent.findAll('div',{'class':'rp-inner-img'}) else 'not verified' 
        verification.append('verified')
        
              
        address_container = agent.findAll('div',{'class':'rp-left-text'})
        agent_address = address_container[0].h4.text
        address.append(agent_address)

        registration_container = address_container[0].find_all('h6')[1]
        registration = registration_container.text
        registration_date.append(registration)

        number_container = agent.findAll('div', {'class':'rp-social'})
        phone_num = number_container[0].find_all('a')[0]['href']
        phone_number.append(phone_num.translate({ord(i): None for i in 'tel :'}))

        whatsapp_num = number_container[0].find_all('a')[1]['href']
        whatsapp_number.append(whatsapp_num.translate({ord(i): None for i in 'tel :'}))

        
agent_data = pd.DataFrame({
    'names' : agent_name,
    'verifications' : verification,
    'agent address' : address,
    'registrations' : registration_date,
    'phone numbers' : phone_number,
    'whatsapp numbers' : whatsapp_number,
})

#print(agent_name)
agent_data.to_csv('agents data.csv')

            






            
        