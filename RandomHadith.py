#print("importing")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

#print("writhing functions")

def get_vals(book):
	html = urlopen(f"https://sunnah.com/{book}")
	res = BeautifulSoup(html.read(),"html5lib")
	found = res.find_all("div")
	vals = []
	for f in found:
		try:
			if f['class'] == ['book_range']:
				v = int(str(f.find_all("div")[2]).strip("</div>")) - int(str(f.find_all("div")[0]).strip("</div>"))
				vals.append(v)
		except:
			pass
	return vals


def get_hadith_link():
	book =  random.choice(["bukhari" , "muslim"])
	vals = get_vals(book)
	sub_book = random.randint(1,len(vals))
	hadith = random.randint(1,vals[sub_book - 1]+1)
	print( f"https://sunnah.com/{book}/{sub_book}/{hadith}")
	return f"https://sunnah.com/{book}/{sub_book}/{hadith}"

def print_hadith(hadith):
	for h in hadith:
		print(str(h).strip("</p>"))

#print("while loop started")

works = False
while not works:
	try:
		html = urlopen(get_hadith_link())
		res = BeautifulSoup(html.read(),"html5lib");
		works = True
	except:
#		print("did not work")
		works = False

hadith = res.find_all("p")[-2:]
print_hadith(hadith)

