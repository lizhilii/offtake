from django.db import models

class CartInfo(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey('goods.GoodsSKU', on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name='商品数量')  # 记录用户买个多少单位的商品

    class Meta:
        db_table = 'offtake_cart'
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user + '的购物车'
