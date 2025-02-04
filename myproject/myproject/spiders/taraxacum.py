# Import required libraries
import scrapy
from scrapy.http.response import Response
import json
from scrapy.crawler import CrawlerProcess
from typing import Dict, List, Any, Generator

class TaraxacumSpider(scrapy.Spider):
    """Spider to scrape data about Taraxacum (Dandelion) from Wikipedia"""
    
    # Name of the spider - used by Scrapy to identify this spider
    name: str = 'taraxacum'
    # Starting URL for the spider to begin crawling
    start_urls: List[str] = ['https://en.wikipedia.org/wiki/Taraxacum']
    

    def parse(self, response: Response) -> Generator[Dict[str, Any], None, None]:
        """
        Parse the Wikipedia page and extract only JSON-LD data
        
        Args:
            response (Response): The response object containing the page content
            
        Yields:
            Dict[str, Any]: Dictionary containing the JSON-LD data
        """
        # Extract JSON-LD data from the script tag in the page
        json_ld: str | None = response.css('script[type="application/ld+json"]::text').get()
        if json_ld:
            # Parse and yield JSON data if found
            data: Dict[str, Any] = json.loads(json_ld)
            # Pretty print the JSON data
            print(json.dumps(data, indent=2))
            yield data
        else:
            # Yield empty dict if no JSON-LD data found
            yield {}

if __name__ == '__main__':
    # Configure Scrapy settings to minimize logging
    process = CrawlerProcess({
        'LOG_LEVEL': 'ERROR',  # Only show errors
        'LOG_ENABLED': False,  # Disable all Scrapy logging
    })
    process.crawl(TaraxacumSpider)
    process.start()

#RETURNED JSON-LD DATA
# {
#   "@context": "https://schema.org",
#   "@type": "Article",
#   "name": "Taraxacum",
#   "url": "https://en.wikipedia.org/wiki/Taraxacum",
#   "sameAs": "http://www.wikidata.org/entity/Q30024",
#   "mainEntity": "http://www.wikidata.org/entity/Q30024",
#   "author": {
#     "@type": "Organization",
#     "name": "Contributors to Wikimedia projects"
#     "@type": "Organization",
#     "name": "Wikimedia Foundation, Inc.",
#     "logo": {
#       "@type": "ImageObject",
#       "url": "https://www.wikimedia.org/static/images/wmf-hor-googpub.png"
#     }
#   },
#   "datePublished": "2002-06-15T03:33:23Z",
#   "dateModified": "2025-01-27T19:12:35Z",
#   "image": "https://upload.wikimedia.org/wikipedia/commons/4/4f/DandelionFlower.jpg",
#   "headline": "genus of plants"
# }
