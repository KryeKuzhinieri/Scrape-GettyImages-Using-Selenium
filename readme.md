- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Usage](#usage)
- [License](#license)

# Scrape Images From GETTYIMAGES.COM

## About The Project

The goal of this project is to scrape images from GettyImages.com and use them for classification purposes. The images are not in full resolution since to do that one would need an account. However, for my little project I do not need high-quality images and as such, I will download the photos that are presented once a query has been submitted.

## Getting Started

In order to successfully run the codes, you need to follow the steps below.

### Prerequisites

The packages that will be used are the following:

``` python
from selenium import webdriver
import urllib.request
import time
import os
```

### Usage

Download Scraper.py file and place it under your desired directory. 
Run the file by:

``` python
python scraper.py
```

If the dependencies have been installed correctly, you need to provide 4 different inputs.

* *person_name*: File's name (i.e: JohnTravolta)
* *url*: GettyImages.com url (i.e: https://www.gettyimages.com/photos/john-travolta?family=editorial&phrase=john%20travolta&sort=mostpopular#license)
* *dir*: Name of the directory you want to save the files. If the folder does not exist, it will create a new one. (i.e: data)
* *pages*: Number of pages that you want to scrape from the website. (i.e: 52)

## License

Distributed under the MIT License. See `LICENSE` for more information.
