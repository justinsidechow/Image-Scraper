# Image-Scraper

The guide I used to create this version of the code was from Fabian Bosler.
https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

He explains how to Image Scrape with Python and I modified it to work on opensea.io.
One of the problem his code faced was the infinite scroll issue of pages and was build more toward google image scraping instead of fully dynamic page scrapping.

The code could be ran faster as it takes all the image's url into an array then downloads them. This is quite slow as the webbrowser slows down as thousands of images are still loaded while the scraper is still taking the image's url. Image Scrapping 6844 cryptopunks took about 3 hours and I believe I can optimize it more in the future if another NFT collection is that big needs scrapping.