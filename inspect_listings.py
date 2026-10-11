from bs4 import BeautifulSoup 

from lab_selectors import extract_listings




with open('sample_merchandise.html') as f:
    html = f.read()
    listings = extract_listings(html)
    for listing in listings:
        print(listing['name'])




#with open('sample_listings.html') as f:
   # html = f.read()
  #  listings = extract_listings(html)
  #  print(listings)
  #  soup = BeautifulSoup(html, 'html.parser')
  #  for listing in soup.select('.price'):
  #      print(listing.text)


#selectors = ['item', '.badge', '.free-shipping', '.sponsored', 
#             '#results > li', '.item + .item', 'li.item > a', 
#            '.sponsored', '#results > li', '.item + .item',
 #            'li.item > a'
 #            ]

#for selector in selectors:
  #  print("for",selector, "there are this many:",len(soup.select(selector)))