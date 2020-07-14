import scrapy

USER_AGENT = "Mozilla/5.0 (Linux; Android 10; TAS-AL00 Build/HUAWEITAS-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/45016 Mobile Safari/537.36 MMWEBID/1198 MicroMessenger/7.0.10.1580(0x27000A5B) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"

Cookies = {
    "mstoken": "c1fbd635a722892f92682b4192df5b47",
    "_dx_uzZo5y": "f441480a4559b89d8300d4315d2029942cca8a0f618db53d4135f8c8b30f6d617c476c45",
    "msOpenId": "obhVk0U0beyp8RGn4D11JAHHqgH8"
}

Body = "{'pageNum':1,'pageSize':10,'activityTagNo':'10','forwarded':false,'sortedType':2,'sortedModel':'1'}"

formBody = {"pageNum":1,"pageSize":10,"activityTagNo":"10","forwarded":False,"sortedType":2,"sortedModel":"1"}
class QuotesSpider(scrapy.Spider):

    name = "coupon"

    def start_requests(self):
        urls = [
            'https://mall.xiangtuan.xyz/api/spweb/order/selectUserTicketlist?status=0&shopBizCode=tyJEENwV6l&pageNum=1&pageSize=10&distributorId=u6Ntz4CPLr'
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
        filename = 'coupon.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)