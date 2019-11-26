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
<br>
</div>


```
createdb wizello_db
psql wizello_db
CREATE USER wizello_usr WITH PASSWORD 'jbZV1?#&3V5_A&$@';
GRANT ALL PRIVILEGES ON DATABASE mrhassanzadeh_db to wizello_usr;
```

<div dir="rtl">
سپس دستورات زیر با برای راه اندازی دیتا بیس و ساخت جداول در shell پروژه ‌Django وارد نمایید:
<br>
</div>

```
Python manage.py makemigrations
Python manage.py migrate
python manage.py loaddata <  initialdata.json
Python manage.py runserver
```

<div dir="rtl">
  در صورتی که مراحل بالا به درستی انجام شده باشند با باز کردن آدرس http://127.0.0.1:8000 صفجه اصلی نرم افزار به صورت زیر نمایش داده میشود :
</div>


![Home](https://cdn1.imggmi.com/uploads/2019/11/26/0001af98b19c58345d24be10883b5b78-full.png)
<div dir="rtl">
لیست کاربران تعریف شده :
</div>

```
Admin : 12345678
manager : 12345678
firstEmployee : 12345678
```
<div dir="rtl">
برای ورود به سیستم از منوی بالا روی  گزینه Login کلیک کنید و میتوانید با اطلاعات کاربران بالا وارد سیستم شوید , در ضمن میتوانید با کلیک روی گزینه Register Employee کارمند جدیدی در سیستم تعریف کنید.
<h3>
  نکته : تمامی کاربران حتی SuperUser که Admin هست هم  فقط از صفحه لاگین برای ورود استفاده میکنند و نیازی به وارد شدن به DjangoAdmin نیست.
 </h3>
</div>  

## Test API
<div dir="rtl">
برای آزمایش بخش API در ابتدا از ابزار نمایش DRF استفاده کردم و بعد از پیاده سازی کامل از ابزار PostMan برای آزمایش دقیق تر استفاده کردم.
</div>  

![PostMan_list](https://cdn1.imggmi.com/uploads/2019/11/26/24c04bd03ebcbcbd190eb7555ee59748-full.png)
![PostMan_Update](https://cdn1.imggmi.com/uploads/2019/11/26/24c04bd03ebcbcbd190eb7555ee59748-full.png)
