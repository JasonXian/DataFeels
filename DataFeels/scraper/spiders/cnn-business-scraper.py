import scrapy as sc
import indicoio as ic
import csv

ic.config.api_key = '771904709f35ee2b6a5e17da2c79ed43'

class Product(sc.Item):
    title = sc.Field()
    url = sc.Field()
    sentiment_score = sc.Field()
    sentiment_hq_score = sc.Field()
    keywords = sc.Field() 
    personality = sc.Field()
    emotion = sc.Field()
    summarization = sc.Field()
    source = sc.Field()

class CNNBusiness(sc.Spider):
    name = "cnnscraper"
    # THIS IS THE WEBSITE WITH THE ARTICLE IT SHOULD SCRAPE
    cnn_urls = [
        "https://www.cnn.com/2018/11/23/business/carlos-ghosn-nissan-renault/index.html",
        "https://www.cnn.com/2018/10/05/tech/cryptocurrency-bitcoin-explainer/index.html",
        "https://www.cnn.com/2018/11/20/tech/bitcoin-cryptocurrency-types/index.html",
        "https://www.cnn.com/2018/10/05/tech/bitcoin-investors-survey/index.html",
        "https://www.cnn.com/2018/11/16/tech/nvidia-stock-earnings-cryptocurrency/index.html",
        "https://www.cnn.com/2018/11/14/tech/bitcoin-price-drop/index.html",
        "https://www.cnn.com/2018/10/12/perspectives/digital-currency-race/index.html",
        "https://www.cnn.com/2018/10/09/media/civil-media-token-sale/index.html",
        "https://www.cnn.com/2018/10/03/tech/blockchain-explainer/index.html",
        "http://money.cnn.com/2018/09/26/investing/markets-now-novogratz-bitcoin/index.html",
        "https://money.cnn.com/2018/09/06/technology/ibm-blockchain-gamble/index.html"
    ]

    thisismoney_urls = [
        "https://www.thisismoney.co.uk/money/podcast/article-6422551/What-burst-bitcoin-bubble-rise-Money-podcast.html",
        "https://www.thisismoney.co.uk/money/diyinvesting/article-6414951/Five-things-learn-bitcoin-bubble.html",
        "https://www.thisismoney.co.uk/money/investing/article-6409587/Bitcoin-price-nosedives-13-month-low-bought-peak-sitting-77-loss.html",
        "https://www.thisismoney.co.uk/money/investing/article-6341737/Is-Initiative-Q-good-true-need-know-it.html",
        "https://www.thisismoney.co.uk/money/investing/article-6337749/Bitcoin-suffers-year-year-loss-10th-birthday-teeters-6k-mark.html",
        "https://www.thisismoney.co.uk/money/markets/article-6140263/Online-currency-bitcoin-suffers-worst-sell-far-year.html",
        "https://www.thisismoney.co.uk/money/markets/article-6139023/Cryptocurrency-mania-sinks-bitcoin-ethereum-prices-fall-Goldman-Sachs-shelves-plans.html",
        "https://www.thisismoney.co.uk/money/investing/article-6006537/Bitcoin-bounce-holds-firm-Price-cryptocurrency-rises-40-year-low.html",
        "https://www.thisismoney.co.uk/money/investing/article-5900309/Bitcoin-price-drops-6k-mark-expert-warns-rout-isnt-finished.html",
        "https://www.thisismoney.co.uk/money/investing/article-5838851/Bitcoin-price-tumbles-2018-low-65-mid-December-peak.html"
        ]

    investopedia_urls = [
        "https://www.investopedia.com/tech/cryptocurrency-dead-good/",
        "https://www.investopedia.com/news/litecoin-future-cryptocurrency/",
        "https://www.investopedia.com/investing/understanding-cryptocurrency-etfs/",
        "https://www.investopedia.com/advisor-network/articles/investing-cryptocurrency-risks/",
        "https://www.investopedia.com/tech/cryptocurrency-this-week/",
        "https://www.investopedia.com/articles/forex/091013/future-cryptocurrency.asp",
        "https://www.investopedia.com/news/are-there-advantages-cryptocurrency-market-pullback/",
        "https://www.investopedia.com/news/cryptocurrency-winners-and-losers-week/",
        "https://www.investopedia.com/news/cryptocurrency-hedge-funds-still-rise/",
        "https://www.investopedia.com/news/whats-behind-latest-cryptocurrency-slump/"
        ]

    yhfinance_urls = [
        "https://finance.yahoo.com/news/apos-crypto-civil-war-apos-235600408.html?.tsrc=fin-srch",
        "https://finance.yahoo.com/news/bitcoin-btc-nobody-knows-down-120025094.html",
        "https://finance.yahoo.com/m/5dcd7994-90ae-3a4a-965c-395c965a4b9f/bitcoin-will-fall-30%25-before.html",
        "https://finance.yahoo.com/m/b49b22c7-08c4-3627-a2d3-53bf9dc58113/overstock-surges-26%25-after.html",
        "https://finance.yahoo.com/news/nvidia-lives-crypto-then-dives-141937699.html",
        "https://finance.yahoo.com/news/britain-says-may-ban-cryptoasset-113543477.html?.tsrc=fin-srch"
        ]

    fool_urls = [
        "https://www.fool.ca/2018/07/18/ride-the-cryptocurrency-and-blockchain-craze-with-hive-blockchain-technologies-ltd-tsxvhive/",
        "https://www.fool.ca/2018/03/30/bitcoin-investors-is-there-any-hope-of-a-rally-for-the-cryptocurrency/",
        "https://www.fool.ca/2018/02/05/the-cryptocurrency-bubble-is-deflating-case-in-point-long-blockchain-corp/",
        "https://www.fool.ca/2018/01/15/cryptocurrency-investing-is-quickly-turning-into-an-eternal-waking-nightmare/",
        "https://www.fool.ca/2017/12/28/2018-new-years-resolution-avoid-all-things-cryptocurrency-like-the-plague/",
        "https://www.fool.ca/2017/12/18/the-most-important-reason-to-stay-away-from-bitcoin-and-other-cryptocurrency/",
        "https://www.fool.ca/2017/12/11/understanding-the-psychology-of-bitcoin-and-the-cryptocurrency-bubble/",
        "https://www.fool.ca/2017/12/07/hive-blockchain-technologies-ltd-the-volatile-rise-of-a-cryptocurrency-mining-stock/",
        "https://www.fool.ca/2018/11/18/forget-bitcoin-i-think-artificial-intelligence-could-be-the-next-big-growth-sector/",
        "https://www.fool.com/investing/2018/11/23/nvidia-lives-by-the-crypto-then-dives-by-the-crypt.aspx"
        ]

    def start_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        for link in self.cnn_urls:
            yield sc.Request(link, callback=self.construct_cnn_data, headers=headers)

        for link in self.thisismoney_urls:
            yield sc.Request(link, callback=self.construct_thisismoney_data, headers=headers)

        for link in self.investopedia_urls:
            yield sc.Request(link, callback=self.construct_investopedia_data, headers=headers)

        for link in self.yhfinance_urls:
            yield sc.Request(link, callback=self.construct_yhfinance_data, headers=headers)

        for link in self.fool_urls:
            yield sc.Request(link, callback=self.construct_fool_data, headers=headers)


    def construct_cnn_data(self, response):
        item = self.parse_cnn_article(response)
        yield item

    def parse_cnn_article(self, response):
        title = response.xpath("//h1/text()").extract()
        #UNUSED author = response.xpath("//span[contains(@class, 'author')]/text()")#.extract_first().replace("By ","").split(',')[0]
        #UNUSED article = response.xpath("//div[contains(@class, 'zn')]/descendant-or-self::*/text()").extract_first()

        itm = Product() 
        itm['title'] = title
        itm['url' ] = response.url
        itm['sentiment_score'] = ic.sentiment(response.url)
        itm['sentiment_hq_score'] = ic.sentiment_hq(response.url)
        itm['keywords'] = ic.keywords(response.url, version=4)
        itm['personality'] = ic.personality(response.url)
        itm['emotion'] = ic.emotion(response.url)
        itm['summarization'] = ic.summarization(response.url)
        itm['source'] = 'CNN'
        
        return itm

    def construct_thisismoney_data(self, response):
        item = self.parse_thisismoney_article(response)
        yield item

    def parse_thisismoney_article(self, response):
        title = response.xpath('//title/text()').extract_first()

        itm = Product() 
        itm['title'] = title
        itm['url'] = response.url
        itm['sentiment_score'] = ic.sentiment(response.url)
        itm['sentiment_hq_score'] = ic.sentiment_hq(response.url)
        itm['keywords'] = ic.keywords(response.url, version=4)
        itm['personality'] = ic.personality(response.url)
        itm['emotion'] = ic.emotion(response.url)
        itm['summarization'] = ic.summarization(response.url)
        itm['source'] = 'thisismoney'

        return itm

    def construct_investopedia_data(self, response):
        item = self.parse_investopedia_article(response)
        yield item

    def parse_investopedia_article(self, response):
        title = response.xpath('//h1/text()').extract_first().strip()

        itm = Product()
        itm['title'] = title
        itm['url'] = response.url
        itm['sentiment_score'] = ic.sentiment(response.url)
        itm['sentiment_hq_score'] = ic.sentiment_hq(response.url)
        itm['keywords'] = ic.keywords(response.url, version=4)
        itm['personality'] = ic.personality(response.url)
        itm['emotion'] = ic.emotion(response.url)
        itm['summarization'] = ic.summarization(response.url)
        itm['source'] = 'investopedia'

        return itm

    def construct_yhfinance_data(self, response):
        item = self.parse_yhfinance_article(response)
        yield item

    def parse_yhfinance_article(self, response):
        title = response.xpath('//h1[contains(@itemprop, "headline")]/text()').extract_first()

        itm = Product()
        itm['title'] = title
        itm['url'] = response.url
        itm['sentiment_score'] = ic.sentiment(response.url)
        itm['sentiment_hq_score'] = ic.sentiment_hq(response.url)
        itm['keywords'] = ic.keywords(response.url, version=4)
        itm['personality'] = ic.personality(response.url)
        itm['emotion'] = ic.emotion(response.url)
        itm['summarization'] = ic.summarization(response.url)
        itm['source'] = 'yahoofinance'

        return itm

    def construct_fool_data(self, response):
        item = self.parse_fool_article(response)
        yield item

    def parse_fool_article(self, response):
        title = response.xpath('//header/h1/text()').extract_first()

        itm = Product()
        itm['title'] = title
        itm['url'] = response.url
        itm['sentiment_score'] = ic.sentiment(response.url)
        itm['sentiment_hq_score'] = ic.sentiment_hq(response.url)
        itm['keywords'] = ic.keywords(response.url, version=4)
        itm['personality'] = ic.personality(response.url)
        itm['emotion'] = ic.emotion(response.url)
        itm['summarization'] = ic.summarization(response.url)
        itm['source'] = 'The motley fool'

        return itm
