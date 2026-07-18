import scrapy
from scrapy.crawler import CrawlerProcess

class DronesSpider(scrapy.spider):                # This creates a new "Spider" (a bot that crawls the web) by borrowing 
                                                   #all the heavy-lifting logic built into Scrapy's standard blueprint (scrapy.Spider).                       
                                                   
    name = "drone_spider"                               # Every spider needs a unique identifier name
    start_urls = ['https://books.toscrape.com/']         # This is the launchpad.
    
    def parse(self, response):
        for product in response.css('article.product_pod'):           # This scans the HTML page for specific HTML boxes
            yield {
                'name': product.css('h3 a::attr(title)').get(),       # 1) Instead of searching the whole website, this searches only
                'price': product.css('p.price_color::text').get(),         #inside that specific product's box
                
                                                                       # 2) Tell Scrapy to strip away the ugly HTML tags 
                                                                            #and grab only the raw text or the link properties.
            }
    if __name__ == "__main__":          # This tells Python: "Only run this bottom block if I directly 
                                            #click the play button on this specific file.
        process = CrawlerProcess(settings={
            'FEEDS': {                    # It tells Scrapy: every time conveyer belt yields item format it
                                        #into a CSV row and it in specific folder etc
                'format': 'csv',
                'encoding': 'utf8',
            },
            'USER_AGENT': 'Mozilla/5.0...'  # This mimics a standard web browser
        })
        process.crawl(DronesSpider)
        process.start()                   # These two methods feeds your custom spider blueprint into the
                                            #execution engine and turns the key to start the scraping process.