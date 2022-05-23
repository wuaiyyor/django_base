from django.db import models

# Create your models here.
"""
1.模型类 需要继承自 models.Model
2.定义属性
    id系统自带
    属性名=Model.类型（选项）
    2.1 属性名 对应 字段名
        不要使用python，mysql关键字
        不要使用连接的下划线
    2.2 类型 mysql的类型
    2.3 选项 是否有默认值，是否唯一，是否null
        CharField 必须设置 max_length
        verbose_name 主要是admin站点使用
3. 改变表的名称
    默认表的名称是：子应用名_类名 都是小写
    修改表的名字
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "bookinfo"  # 修改表的名字
        verbose_name = "书籍管理"  # 修改admin站点的名字

    def __str__(self):
        return self.name


class PersonInfo(models.Model):
    GENDER_CHOICE = {
        (1, "male"),
        (0, "female")
    }
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    # 外键：系统会自动为外键添加 id
    # 外键的级联操作
    # 主表的一条数据 如果删除了
    # 从表有关联的数据，该怎么办
    # 1.设置为空    SET_NULL
    # 2.抛出异常不让删除    PROTECT
    # 3.级联删除    CASCADE
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "personinfo"

    def __str__(self):
        return self.name
