from django.db import models
from db.banse_model import BaseModel

class OrderInfo(BaseModel):
    '''订单模型'''

    PAY_METHOD_CHOICES = (
        (1, '货物到付'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付'),
    )

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成'),
    )

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户')
    addr = models.ForeignKey('user.Address', on_delete=models.CASCADE, verbose_name='收货地址')

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单编号')

    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单价格')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')

    class Meta:
        db_table = 'offtake_order_info'
        verbose_name = '订单'
        verbose_name_plural = verbose_name

class OrderGoods(BaseModel):
    '''订单商品模型类'''

    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name='订单')
    sku = models.ForeignKey('goods.GoodsSku', on_delete=models.CASCADE, verbose_name='商品SKU')
    count = models.IntegerField(default=1, verbose_name='商品数目')
    prince = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品单价')
    comment = models.CharField(max_length=256, verbose_name='评论')

    class Meta:
        db_table = 'offtake_order_goods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name








