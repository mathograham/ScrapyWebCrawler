#venv called lettfreqproj
import scrapy

class LetterSpider(scrapy.Spider):
    name = "lettfreq"
    
    start_urls = [
            'https://www.gutenberg.org/cache/epub/32522/pg32522-images.html',
            
    ]
        
    def parse(self, response):
        for line in response.css("p"):
                yield {
                    'text': line.css("::text").getall(),
                    }
