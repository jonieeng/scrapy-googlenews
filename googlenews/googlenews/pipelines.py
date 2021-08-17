# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class GooglenewsPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            user='',
            password='',
            host='',
            port=3306,
            database=''
        )

        self.curr = self.conn.cursor()
    
    # 'start','end','query', 'region', 'title', 'excerpt', 'date', 'source', 'link' 
    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS semiconductor(
            id INT AUTO_INCREMENT PRIMARY KEY,
            start DATE,
            end DATE,
            query VARCHAR(255),
            region VARCHAR(2),
            title TEXT,
            excerpt TEXT,
            date DATE,
            source VARCHAR(255),
            link TEXT
        )""")

    def process_item(self, item, spider):
        self.store_db(ItemAdapter(item).asdict())

    def store_db(self, item):
        myquery = """INSERT into semiconductor
        (
            start,
            end,
            query,
            region,
            title,
            excerpt,
            date,
            source,
            link
        )
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        value = (
            item["start"],
            item["end"],
            item["query"][0],
            item["region"][0],
            item["title"],
            item["excerpt"],
            item["date"],
            item["source"],
            item["link"]
        )

        self.curr.execute(myquery, value)
        self.conn.commit()
    
    def close_spider(self, spider):
        self.conn.close
