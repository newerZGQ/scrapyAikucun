import scrapy

USER_AGENT = "Mozilla/5.0 (Linux; Android 10; TAS-AL00 Build/HUAWEITAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/45016 Mobile Safari/537.36 MMWEBID/1198 MicroMessenger/7.0.10.1580(0x27000A5B) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"

Cookies = {
    "mstoken": "b9d859290571397480fd51321c5ff6fd",
    "_dx_uzZo5y": "f441480a4559b89d8300d4315d2029942cca8a0f618db53d4135f8c8b30f6d617c476c45",
    "msOpenId": "obhVk0U0beyp8RGn4D11JAHHqgH8"
}

Body = "{'pageNum':1,'pageSize':10,'activityTagNo':'10','forwarded':false,'sortedType':2,'sortedModel':'1'}"

formBody = {"pageNum":1,"pageSize":10,"activityTagNo":"10","forwarded":False,"sortedType":2,"sortedModel":"1"}
class QuotesSpider(scrapy.Spider):

    name = "feeds"

    def start_requests(self):
        urls = [
            'https://zuul.aikucun.com/aggregation-center-facade/api/app/conference/list/v1.0?sign=2AE96EEDA41690A2D1653C2F992AB994&userid=402e9a9861a59e0c7983219dee6cfe36&conferenceId=41&channelId=33&needHeader=1&pageno=1&pagesize=10&time=1580203241191'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, method="get", headers={
                "USER_AGENT": USER_AGENT,
                "origin": "https://mall.xiangtuan.xyz",
                "accept": 'application/json, text/plain, */*',
                "x-requested-with": "com.tencent.mm"
            }, cookies=Cookies)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'feeds.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)