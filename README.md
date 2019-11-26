# Wize + Trello -> Wizello 

mini task managment project http://wizeanalytics.com/

<div dir="rtl">
اگر از سیستم عامل Ubuntu استفاده میکنید میتوانید با استفاده از دستور زیر از ENV استفاده نمایید :
</div>

```source ENV/bin/activate```

<div dir="rtl">
البته در صورتی که Virtualenv روی سیستم عامل شما نصب باشد
اگر از سیستم عامل دیگری استفاده می کنید ابتدا باید پکیج های مورد نیاز را با دستور زیر نصب نمایید
</div>


```Pip install -r requirments.txt```


# DataBase
<div dir="rtl">
در این پروژه به دلیل اینکه داده ها دارای الگویی مشخصی بودند و برای افزایش سرعت و استفاده کامل از DjangoORM از دیتابیس RDMS استفاده کردم و به سراغ Nosql نرفم , همچنین از بین دیتابیس های Mysql و Postgresql هم دیتابیس Postgres را انتخاب کردم.
به دلیل پشتیبانی کامل از Acid و همچنین امکانات و سرعت بالا البته از نظر بنده اینطوره و امکان داره انتخابم کاملا درست هم نباشه.
</div>

## SetUp PostgresQL

<div dir="rtl">
در ابتدا روی سیستم عامل  Postgres نصب کنید و بعد از start سرویس آن با دستورات زیر دیتابیس را ایجاد و کاربر مربوط به آن را نیز با اطلاعات زیر ایجاد نمایید.
</div>

```
createdb wizello_db
psql wizello_db
CREATE USER wizello_usr WITH PASSWORD 'jbZV1?#&3V5_A&$@';
GRANT ALL PRIVILEGES ON DATABASE mrhassanzadeh_db to wizello_usr;
```

<div dir="rtl">
سپس دستورات زیر با برای راه اندازی دیتا بیس و ساخت جداول در shell پروژه ‌Django وارد نمایید:
</div>

```
Python manage.py makemigrations
Python manage.py migrate
python manage.py loaddata <  initialdata.json
Python manage.py runserver
```

<div dir="rtl">
در صورتی که مراحل بالا به درستی انجام شده باشند با باز کردن آدرس زیر :
http://127.0.0.1:8000/
صفجه اصلی نرم افزار به صورت زیر نمایش داده میشود :
</div>

![LoginPage](https://drive.google.com/open?id=1PMMfwEuqtSuzmkD256SSaug7p01NdAMa)
