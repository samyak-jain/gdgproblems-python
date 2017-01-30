from bs4 import BeautifulSoup
import re
import requests
import webbrowser

def removechar(x):
	return re.sub(r'[\s\n]*$','', re.sub(r'^[\s\n]*','', x))

votes = []
questions = []
answers = []
query = input("Your query: ")
html_doc = requests.get("http://stackoverflow.com/search?q=" + query).text
soup = BeautifulSoup(html_doc, 'html5lib')
q1 = soup.find_all("div", "search-results js-search-results")[0].contents[1]

votes.append(q1.find("span", "vote-count-post ").string)
questions.append(removechar(q1("div", "result-link")[0].find("a").string))
answers.append(requests.get("http://stackoverflow.com" + q1("div", "result-link")[0].find("a")['href']))

for i in q1.find_next_siblings():
	votes.append(i.find("span", "vote-count-post ").string)
	questions.append(removechar(i("div", "result-link")[0].find("a").string))
	answers.append(requests.get("http://stackoverflow.com" + i("div", "result-link")[0].find("a")['href']))


for j in range(4):
	xstr = ''
	for i in BeautifulSoup(answers[j].text, 'html5lib').find('div', attrs={'id': 'answers'}).find('div', 'post-text').contents:
		try:
			if i.string is None:
				for x in i.contents:
					xstr += removechar(x.string) + ' '
			else:
				xstr += removechar(i.string)
		except TypeError: pass
		xstr += '\n'
	answers[j] = xstr

print('Enter the entry number to be viewed in the webbrowser in the end')
print('\n\n')	
for i in range(len(votes)):
	print("Entry " + str(i+1) + ' ' + '*'*80, '\n')
	print("Votes: ", votes[i])
	print(questions[i], '\n')
	print('Answer:')
	print(answers[i])
	print('*'*90)
	print('\n\n')
	
entryno = input("Entry Number (enter q to not take any action): ")
if (entryno!='q'):
	if (entryno == '1'): webbrowser.open("http://stackoverflow.com" + q1("div", "result-link")[0].find("a")['href'])
	else: webbrowser.open("http://stackoverflow.com" + q1.find_next_siblings()[int(entryno)-1]('div', 'result-link')[0].find("a")['href'])