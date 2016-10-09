from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()

class Movie(Item):
    zone = Field()
    url_id = Field()
    title = Field()
    divcontent = Field()
    topimg = Field()
    kind = Field()
    xflink = Field()
    create_time = Field()
class Pics(Item):
    zone= Field()
    url_id = Field()
    title = Field()
    divcontent = Field()
    kind = Field()
    create_time = Field()
