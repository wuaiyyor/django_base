from django.shortcuts import render
from book.models import BookInfo, PersonInfo


# Create your views here.
def index(request):
    context = {
        "name": "双十一，点击有惊喜",
    }
    return render(request, "book/index.html", context)


#####################增加数据#########################################
# 方式1
book = BookInfo(
    name="Django",
    pub_date="2000-1-1"
)
# 必须要调用对象的save方法才能将数据保存到数据库中
book.save()

# 方式2
# objects--相当于一个代理实现增删改查
BookInfo.objects.create(
    name="测试开发入门",
    pub_date="2020-1-1"
)

#################修改数据################################
# 方式1
book = BookInfo.objects.get(id=6)
book.name = "yunweikai"
book.save()

# 方式2
# filter 过滤
BookInfo.objects.filter(id=6).update(name="爬虫入门")

####################删除数据################################
# 方式1
book = BookInfo.objects.get(id=6)
book.delete()

# 方式2
BookInfo.objects.get(id=5).delete()
BookInfo.objects.filter(id=5).delete()

#######################查询###########################
# get查询单一结果，如果不存在就会抛出异常
try:
    book = BookInfo.objects.get(id=1)
except:
    print("查询结果不存在")
# all查询多个结果
BookInfo.objects.all()
# count查询结果数量
BookInfo.objects.count()

#######################过滤查询###########################
# 实现sql中的where功能

# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值)
# 模型类名.objects.exclude(属性名 运算符=值)
# 模型类名.objects.get(属性名 运算符=值)

book1 = BookInfo.objects.get(id=1)
book2 = BookInfo.objects.get(id__exact=1)
book3 = BookInfo.objects.get(pk=1)
book4 = BookInfo.objects.filter(id=1)
BookInfo.objects.get(name__contains="湖")
BookInfo.objects.filter(name__endswith="部")
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(id__in=[1, 3, 5])
BookInfo.objects.filter(id__gt=3)
# great大于  equal等于  little小于
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(pub_date__gt="1990-1-1")

from django.db.models import F

# 使用：2个属性的比较
# 语法形式：以filter为例： 模型类名.objects.filter(属性名__运算符=F("第二个属性名"))

# 查询阅读量大于等于评论量图书
BookInfo.objects.filter(read_count__gte=F("comment_count"))

BookInfo.objects.filter(read_count__gt=20).filter(id__lt=3)
BookInfo.objects.filter(read_count__gt=20, id__lt=3)

from django.db.models import Q

# 或者语法：  模型类名.objects.filter(Q(属性名__运算符=值)|Q(id__lt=3))

BookInfo.objects.filter(Q(read_count__gt=20) | Q(id__lt=3))

# 聚合函数
from django.db.models import Sum, Avg, Max, Min, Count

# 模型类名.objects.aggregate(Xxx("字段名"))
BookInfo.objects.aggregate(Sum('read_count'))

BookInfo.objects.all().order_by("read_count")

book = BookInfo.objects.get(id=1)
# 系统会固定设置personinfo_set
book.personinfo_set.all()

# 关联过滤查询
BookInfo.objects.filter(personinfo__name__exact="郭靖")
BookInfo.objects.filter(personinfo__name="郭靖")

BookInfo.objects.filter(personinfo__description__contains="八")

PersonInfo.objects.filter(book__name="天龙八部")
