from django.db import models

# Create your models here.

# 图书
class Book(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True) # 编号
    name = models.CharField(max_length=100) # 名称
    author = models.CharField(max_length=100) # 作者
    category = models.CharField(max_length=100) # 分类
    publisher = models.CharField(max_length=100) # 出版社
    publish_date = models.DateField(auto_now=True) # 出版日期
    description = models.CharField(max_length=100) # 图书简介
    amount = models.IntegerField(default=0) # 全部数量
    remaining = models.IntegerField(default=0) # 剩余数量

    def __str__(self):
        return '%d' % self.id

# 用户
class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True) # 编号
    cardID = models.CharField(max_length=100) # 借阅证号
    user_group = models.IntegerField() # 用户类型
    account = models.CharField(max_length=100) # 账号
    password = models.CharField(max_length=100) # 密码
    name = models.CharField(max_length=100) # 姓名
    major = models.CharField(max_length=100) # 系别

    def __str__(self):
        return '%d' % self.id

    
# 借阅信息
class BorrowInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True) # 编号
    borrow_date = models.DateField(auto_now=True) # 借阅日期
    return_date = models.DateField(auto_now=True) # 归还日期
    borrowerID = models.ForeignKey(User, on_delete=models.CASCADE) # 借阅者编号
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE) # 图书编号
    remark = models.CharField(max_length=100) # 借阅备注
    is_return = models.BooleanField(blank=True) # 已归还

    def __str__(self):
        return '%d' % self.id




