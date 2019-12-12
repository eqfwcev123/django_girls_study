from django.conf import settings
from django.db import models
from django.utils import timezone


# Field 타입으로 알 수 있는 것들
# 1. Column type: 데이터베이스에 어떠한 데이터를 추가할지
# 2. Minimal Django requirements

# 자주 사용되는 필드 목록:
# 1. models.BooleanField()
# 2. models.CharField(max_length = None) : 설정하지 않으면 max_length는 0. 사용자가 직접 지정

# DateField VS DateTimeField : DateField 는 datetime.date 이고 DateTimeField 는 datetime.datetime. 이 둘의 차이점은 DateField 는 날짜만 나오고 DateTimeField 는 날짜와 시간 모두 나온다
# 3. models.DateField(auto_now = False, auto_now_add=False, **options) : a date represented in Python by a datetime.date instance.
# auto_now : autmoatically set the field to now every time the object is saved.
# auto_now_add : automatically set the field to now when the object is first created.
# For DateField: default = date.today from datetime.date.today()
# 4. models.DateTimeField() : A date and time represented in Python by a datetime.datetime instance.
# For DateTimeField: default = timezone.now()
# 5. models.EmailField()
# 6. models.IntegerField()
# 7. models.TextField() : text가 길경우 CharField 가 아닌 TextFiled 를 사용
# 8. models.TimeField()
#
# Releationship 필드 목록: ForeignKey, ManyToManyField and OneToOneField require the first argument to be a model class.
# 1. models.ForeignKey(클래스이름, on_delete) : Many to One Relationship. ForeignKey() requires a positional argument, the class to which the model is related(다른 클래스의 이름).
    # on_delete argument : when an object referenced by a ForeignKey object is deleted, Django will emulate the behavior of SQL constraint specified by the on_delete argument
    # on_delete = modlels.CASCADE = When an object referenced by a FK is deleted, the FK object is also deleted.
    # on_delete = models.PROTECT
    # on_delete = models.SET_NULL
    # on_delete = models.SET_DEFAULT
    # on_delete = models.SET
    # on_delete = models.DO_NOTHING
# 2. models.ManyToManyField()
# 3. models.OneToOneField()

# FieldOptions
# 1. Primary key: If True, the filed is the primary key for the model. If we dont specify primary_key = True for any fields in our model, Django will automatically add an
# Integer Field to hold the primary key so we don't have to set primary_key = True on any of our fields unless we want to override the default pk behavior. Primary_ket = True implies the field is unique = True
# 2. Unique : If True, the field should be unique throughout the table. (Cannot save duplicate values if the Filed is unique)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
