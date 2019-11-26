# Wize + Trello -> Wizello 

mini task managment project

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

http://wizeanalytics.com/
