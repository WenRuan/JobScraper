import requests
from bs4 import BeautifulSoup


#Requests
monsterURL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Reno__2C-NV'
page = requests.get(monsterURL)

monster = BeautifulSoup(page.content, 'html.parser')


#Results for Monster
monsterAllListing = monster.find(id = 'ResultsContainer')
monsterListing = monsterAllListing.find_all('section', class_='card-content')
for monsterSummary in monsterListing:
	monsterTitle = monsterSummary.find('h2', class_='title')
	monsterCompany = monsterSummary.find('div', class_='company')
	monsterLocation = monsterSummary.find('div', class_='location')
	if None in (monsterTitle, monsterCompany, monsterLocation):
		continue

	print(monsterTitle.text.strip())
	print(monsterCompany.text.strip())
	print(monsterLocation.text.strip())
	print();


print()
print('Indeed:')

#Requests for indeed
indeedURL = 'https://www.indeed.com/jobs?q=software+developer&l=Reno%2C+NV'
indeedPage = requests.get(indeedURL)

indeed = BeautifulSoup(indeedPage.content, 'html.parser')


#Results for Indeed
indeedAllListing = indeed.find('td', id = 'resultsCol')
indeedListing = indeedAllListing.find_all('div', class_= 'jobsearch-SerpJobCard')
for indeedSummary in indeedListing:
	indeedTitle = indeedSummary.find('h2', class_ = 'title')
	indeedTitleText = indeedTitle.find('a')
	indeedCompany = indeedSummary.find('span', class_ = 'company')
	indeedLocation = indeedSummary.find('span', class_ = 'location')
	if None in (indeedTitle, indeedCompany, indeedLocation):
		continue

	print(indeedTitleText.text.strip())
	print(indeedCompany.text.strip())
	print(indeedLocation.text.strip())
	print()











