# [leetscraper](https://pypi.org/project/leetscraper/ "leetscraper on pypi")  
[![Downloads](https://pepy.tech/badge/leetscraper)](https://pepy.tech/project/leetscraper "Total downloads from pypi") &middot; 
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/pavocracy/leetscraper.svg)](http://isitmaintained.com/project/pavocracy/leetscraper "Average time to resolve an issue") &middot; 
[![Percentage of issues still open](http://isitmaintained.com/badge/open/pavocracy/leetscraper.svg)](http://isitmaintained.com/project/pavocracy/leetscraper "Percentage of issues still open") &middot; 
[![codecov](https://codecov.io/gh/Pavocracy/leetscraper/branch/main/graph/badge.svg?token=KUQ6T9TPLO)](https://codecov.io/gh/Pavocracy/leetscraper) &middot; 
[![CodeQL](https://github.com/Pavocracy/leetscraper/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Pavocracy/leetscraper/actions/workflows/codeql-analysis.yml)  
  
leetscraper, a coding challenge scraper for leetcode, and other websites!  
  
This scraper currently works for 
[leetcode.com](https://leetcode.com "leetcode website"), 
[codechef.com](https://codechef.com "codechef website"), 
[codewars.com](https://codewars.com "codewars website"), 
[hackerrank.com](https://hackerrank.com "hackerrank website"), 
[projecteuler.net](https://projecteuler.net "projecteuler website"). 

It was created as a way to gather coding problems to solve without having to sign up to a website or submit your code to a checker.

***

# Usage
  
### Install package

Installing leetscraper with pip will also install python dependencies needed. Chrome or Firefox are also required for this scraper to work.
```python
python3 -m pip install leetscraper
```

### Examples

Import the module and Initialize the class. The class has some kwargs options to control the behaviour of the scraper.
However, all the default values will start to scrape all problems from leetcode.com to the cwd.
  
The most basic usage looks like this:
```python
from leetscraper import Leetscraper

if __name__ == "__main__":
    Leetscraper()
```

The avaliable kwargs to control the behaviour of the scraper are:
```python
"""
website_name: name of a supported website to scrape ("leetcode.com" set if ignored)
scrape_path: "path/to/save/scraped_problems" (Current working directory set if ignored)
scrape_limit: integer of how many problems to scrape at a time (no limit set if ignored)
auto_scrape: "True", "False" (True set if ignored)
"""
```

For further examples on how to use keyword arguments, or manually using class methods, please see [ADVANCED_USAGE.md](https://github.com/Pavocracy/leetscraper/blob/main/docs/ADVANCED_USAGE.md "Advanced usage doc")

### Information

How fast and reliable this scraper performs will change depending on things like which website you are scraping and your internet connection. 
There is also no guarantee that as these websites add new problems, that they will use the same class names in their html tags. Expect things 
to break and for some requests to fail. leetscraper.log will contain urls of failed scrapes if you wish to grab these manually, or run the scraper
again and see if the failures were just timeouts or dropped requests. Your mileage absolutely WILL vary, but as a rough point of reference of what you can expect, here is the results of a complete and unlimited test scrape.  
  
 *10 hours, 30 minutes and 40 seconds to scrape 15665 problems from 5 websites with an error rate of 0.54%*
```
14/02/2022 12:52:53 PM [INFO]: Getting the list of leetcode.com problems to scrape
14/02/2022 12:52:54 PM [INFO]: Attempting to scrape 1694 leetcode.com problems
14/02/2022 02:51:05 PM [DEBUG]: Scraping 1693 leetcode.com problems took 7088 seconds
14/02/2022 02:51:05 PM [WARNING]: Scraped 1693 problems, but 1 problems failed! Check leetscraper.log for failed scrapes.
14/02/2022 02:51:05 PM [INFO]: Getting the list of projecteuler.net problems to scrape
14/02/2022 02:51:07 PM [INFO]: Attempting to scrape 785 projecteuler.net problems
14/02/2022 03:16:16 PM [DEBUG]: Scraping 785 projecteuler.net problems took 1506 seconds
14/02/2022 03:16:16 PM [INFO]: Successfully scraped 785 projecteuler.net problems
14/02/2022 03:16:16 PM [INFO]: Getting the list of codechef.com problems to scrape
14/02/2022 03:16:32 PM [INFO]: Attempting to scrape 2973 codechef.com problems
14/02/2022 04:44:35 PM [DEBUG]: Scraping 2892 codechef.com problems took 5280 seconds
14/02/2022 04:44:35 PM [WARNING]: Scraped 2892 problems, but 81 problems failed! Check leetscraper.log for failed scrapes.
14/02/2022 04:44:35 PM [INFO]: Getting the list of hackerrank.com problems to scrape
14/02/2022 04:45:14 PM [INFO]: Attempting to scrape 1089 hackerrank.com problems
14/02/2022 05:38:43 PM [DEBUG]: Scraping 1086 hackerrank.com problems took 3207 seconds
14/02/2022 05:38:43 PM [WARNING]: Scraped 1086 problems, but 3 problems failed! Check leetscraper.log for failed scrapes.
14/02/2022 05:38:43 PM [INFO]: Getting the list of codewars.com problems to scrape
14/02/2022 05:38:43 PM [INFO]: **NOTE** codewars can take up to 5 minutes to find all problems!
14/02/2022 05:43:30 PM [INFO]: Attempting to scrape 9209 codewars.com problems
14/02/2022 11:23:33 PM [DEBUG]: Scraping 9209 codewars.com problems took 20340 seconds
14/02/2022 11:23:33 PM [INFO]: Successfully scraped 9209 codewars.com problems
```

***

# Contributing
If you would like to contribute, adding support for a new coding challenge website, or fixing current bugs is always appreciated!
I would encourage you to see [CONTRIBUTING.md](https://github.com/Pavocracy/leetscraper/blob/main/docs/CONTRIBUTING.md "Contributing doc") for further details.
If you would like to report bugs or suggest websites to support, please add a card to [Issues](https://github.com/Pavocracy/leetscraper/issues "Github issues").  
  
Thank you to all contributors of this project!  
  
<a href="https://github.com/pavocracy/leetscraper/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=pavocracy/leetscraper" />
</a>  

***

# Code of Conduct

Contributing to this project means you are willing to follow the same conduct that others are held to! Please see [Code of Conduct](https://github.com/Pavocracy/leetscraper/blob/main/docs/CODE_OF_CONDUCT.md "Code of conduct doc") for further details.

***

# License
This project uses the GPL-2.0 License, As generally speaking, I want you to be able to do whatever you want with this project, But still have the ability to add your changes
to this codebase should you make improvements or extend support.
For further details on what this licence allows, please see [LICENSE.md](https://github.com/Pavocracy/leetscraper/blob/main/LICENSE.md "GPL v2 Licence")

***

***Copyright (C) 2022 Pavocracy <pavocracy@pm.me>***  
***Signed using PGP key [DB8E4775334F64B2D20279996A592E7961A0EFE4](https://github.com/Pavocracy/Pavocracy/blob/main/pavocracy.pub "Public PGP Key")***  
*See related docs for [how to verify](https://github.com/Pavocracy/leetscraper/blob/main/docs/VERIFY_SIGNED_PACKAGES.md) signed packages*
