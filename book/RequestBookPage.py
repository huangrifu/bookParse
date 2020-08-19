from urllib import request
import urllib.request
import json

elementUrl = "http://e.dangdang.com/media/api.go?action=getPcChapterInfo&epubID=1901146839&permanentId" \
             "=20200429151400362374460542146507956&consumeType=1&platform=3&deviceType=Android&deviceVersion=5.0.0" \
             "&channelId=70000&platformSource=DDDS-P&fromPaltform=ds_android&deviceSerialNo=html5&clientVersionNo=5.8.4" \
             "&token={token}&chapterID={chapterID}&pageIndex={pageIndex}" \
             "&locationIndex={locationIndex}&wordSize=2&style=2&autoBuy=0&chapterIndex="
catalogUrl = "http://e.dangdang.com/media/api.go?action=getPcMediaInfo&consumeType=1&platform=3&deviceType=Android&deviceVersion=5" \
             ".0.0&channelId=70000&platformSource=DDDS-P&fromPaltform=ds_android&deviceSerialNo=html5&clientVersionNo=5.8.4&epubID" \
             "=1901146839&token=pc_dab1ce1a1f95e83c6984ac6edd3cbaf6d59636a82d21830b22d7b13c5271445&wordSize=2&style=2 "

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
'Cookie' :'__permanent_id=20200429151400362374460542146507956; MDD_channelId=70000; MDD_fromPlatform=307; permanent_key=202004291514229391839500786b83bf; __ddc_15d_f=1597108581%7C!%7C_ddclickunion%3D419-997686%257C00792427d6ae731125ba; MDD_custId=VdAiKYM2x3twT0dhP5ziXQ%3D%3D; MDD_username=139****7323; readType=2; ddUserFirstToRead=yes; ddscreen=2; producthistoryid=1901146839; __visit_id=20200819103059619759056874310500972; __out_refer=1597804260%7C!%7Cp.gouwubang.com%7C!%7C; __ddc_1d=1597804260%7C!%7C_ddclickunion%3D419-997686%257C00792427d6ae731125ba; __ddc_15d=1597804260%7C!%7C_ddclickunion%3D419-997686%257C00792427d6ae731125ba; __ddc_24h=1597804260%7C!%7C_ddclickunion%3D419-997686%257C00792427d6ae731125ba; USERNUM=y0i0dCF53CzzEGBMyAFfvQ==; dangdang.com=email=b2NpbDV1UHBHU2p2R25vbVV6Ymo2N0B3ZWl4aW5fdXNlci5jb20=&nickname=&display_id=8117077766463&customerid=t886cxTaQeLXv3RA3fCSQQ==&viptype=WV/jnPMWKJc=&show_name=139%2A%2A%2A%2A7323; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_6_end=1597806447352; pos_6_start=1597806453730; LOGIN_TIME=1597807079163; pageNum=1901146839%3A828_1901146838%3A25_1901166838%3A2_1901166638%3A3_1901166589%3A2_1901167895%3A6_1901167896%3A2_1901167898%3A1_1901167899%3A4; pos_9_end=1597807089956; pos_0_start=1597807089973; pos_0_end=1597807089979; ad_ids=3675023%2C3675016%7C%233%2C3; login.dangdang.com=.AYH=2020081911181908193240157&.ASPXAUTH=Iwrwr2/WnyTKzvtx1gHAAaL/HeG0HsYl9Y493p3su6L/IpCHQ7LMKg==; __rpm=s_112100...1597807091754%7Clogin_page.login_password_div..1597807102802; ddoy=email=ocil5uPpGSjvGnomUzbj67%40weixin_user.com&nickname=&agree_date=1&validatedflag=0&uname=13925757323&utype=1&.ALFG=on&.ALTM=1597807104; sessionID=pc_befb1b5ccfe70f67b8b7d77fc6891cb6ae56bee4088c79e341d99c8db9f2e525; __dd_token_id=2020081911182454579560529554bf59; __trace_id=20200819111827676366724518310711015'
}


class RequestBookPage:
    catalogs = {}
    token = "pc_befb1b5ccfe70f67b8b7d77fc6891cb6ae56bee4088c79e341d99c8db9f2e525"

    def requestElement(self, num):
        print("页数 = ", num)
        catalog = self.getCatalog(num)
        if catalog is None:
            return ''
        try:
            url = elementUrl.format(token=self.token, pageIndex=catalog['pageIndex'], chapterID=catalog['chapterID'],
                                    locationIndex=num)

            # 创建请求
            request = urllib.request.Request(url, headers=headers)
            # 发送请求
            response = urllib.request.urlopen(request)

            # response = request.urlopen(url,headers=headers)
            responseStr = response.read().decode('utf-8')
            data = json.loads(responseStr)
            return json.loads(data['data']['chapterInfo'])['snippet']
        except BaseException as e:
            print("requestElement出错")
            return ''

    def requestCatalog(self):
        response = request.urlopen(catalogUrl)
        responseStr = response.read().decode('utf-8')
        data = json.loads(responseStr)
        self.catalogs = data['data']['mediaPageInfo']

    def getCatalog(self, num):
        return self.catalogs.get("pagenum%d" % num)
