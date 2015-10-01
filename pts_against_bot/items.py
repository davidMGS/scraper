# Define here the models for your scraped items

from scrapy.item import Item, Field

class PtsItem(Item):
    team = Field()
    opponent = Field()
    position = Field()
    points_against = Field()