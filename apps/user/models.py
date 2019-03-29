from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from db.banse_model import BaseModel


class User(AbstractUser, BaseModel):
    '''用户模型类'''

    # def generate_activate_token(self):
    #     '''生成用户签字字符串（用于加密）'''
    #     serializer = Serializer(settings.SECRET_KEY, 3600)
    #     info = {'confirm': self.id}
    #     token = serializer.dump(info)
    #     return token.decode()

    class Meta:
        db_table = 'offtake_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Address(BaseModel):
    '''地址模型类'''
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件人地址')
    zip_code = models.CharField(max_length=6, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否为默认地址')

    class Meta:
        db_table = 'offtake_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name







