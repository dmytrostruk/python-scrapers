from scraper import EbayScraper
import sys

searchString = sys.argv[-1] if len(sys.argv) > 1 else '' 

if searchString != '':
  scraper = EbayScraper()
  scraper.printJSON(searchString)
else:
  print('Search string was not provided')