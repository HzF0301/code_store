"""
用于类的定义
"""


class Record:

    def __init__(self, date, order_id, money, province):
        self.date = date                # 日期
        self.order_id = order_id      # id
        self.money = money              # 销售额
        self.province = province        # 销售省份

    def __str__(self):
        return f'{self.date}, {self.order_id}, {self.money}, {self.province}'



