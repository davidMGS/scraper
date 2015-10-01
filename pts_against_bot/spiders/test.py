from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from pts_against_bot.items import PtsItem


class MySpider(BaseSpider):
    name = "pts_against_bot"

    # Position vars
    QB = "1"
    RB = "2"
    WR = "3"
    TE = "4"
    K = "7"
    DEF = "8"

    # Site info
    base_url = "http://fantasy.nfl.com/research/pointsagainst?sort=pointsAgainst_pts&statCategory=pointsAgainst&statSeason=2015&statType=seasonPointsAgainst&position="

    allowed_domains = ["nfl.com"]
    start_urls = [base_url + QB,
                  base_url + RB,
                  base_url + WR,
                  base_url + TE,
                  base_url + K,
                  base_url + DEF]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//table[@class='tableType-team hasGroups']/tbody/tr")
        items = []
        for titles in titles:
            item = PtsItem()
            item["team"] = titles.select("td[@class='teamNameAndInfo first']/div/text()").extract()
            item["opponent"] = titles.select("td[@class='playerOpponent']/span/text()").extract()
            item["position"] = titles.select("td[@class='teamNameAndInfo first']/div/em/text()").extract()
            item["points_against"] = titles.select("td[@class='stat numeric sorted']/span/text()").extract()
            items.append(item)
        return items