<h1 align="center">Здравствуйте! <p align="center"> я <a href="https://daniilshat.ru/" target="">Андрей</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<p><h3 align="center">это мое тестовое задание на 
<a href="https://spb.hh.ru/vacancy/55356832?from=negotiations_item&hhtmFrom=negotiations_item"> вакансию </a></h3>
<h3 align="center"> в компанию Ranks</h3> 
документацию пишу на английском, разумеется, могу и на русском

---
<h1 align="center"> Starting project</h1> 
<h3 align="left"> Installing requitrements</h3> 

```bash
pip install -r requirements.txt
```

<h3 align="left"> Configuring variables</h3> 
 to configure variables replace data in .env_sample file with relevant data

```
SECRET_KEY - django secret key, should be private for the project? but i've left mine in sample
DATABASE_NAME - PostgreSQL database name
DATABASE_USER -  PostgreSQL username. User should have rights to use selected database
DATABASE_PASSWORD - PostgreSQL user's password
DATABASE_HOST - PostgreSQL database host
DATABASE_PORT -  PostgreSQL database host
STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY - stripe publik and secret key you can get one in user profile
DOMAIN - site's domain. If it's in debug/testing mode leave http://127.0.0.1:8000
```
after configuring .env_sample rename it into ```.env```

<h3 align="left"> Starting Django project</h3>
<h4 align="left"> Migrating database</h4> 
To migrate database run

```bash
python manage.py migrate
```

or 

```bash
python3 manage.py migrate
```
(for MacOS and Windows users)

in project's directory
<h4 align="left"> Creating superuser</h4> 
Run in project's directory

```bash
python manage.py createsuperuser
```
or 

```bash
python3 manage.py createsuperuser
```
(for MacOS and Windows users)

and follow instructions to create superuser.
<h4 align="left"> Run django test server</h4> 

```bash
python manage.py runserver
```
or 

```bash
python3 manage.py runserver
```
(for MacOS and Windows users)

<h4 align="left"> Registration of items</h4> 
Login to http://127.0.0.1:8000/admin/ and create items. Price should be entered in cents. You can get Stripe price id for each item from your stripe account

---
<h1 align="center"> Доп. задания: </h1> 

- [ ] Запуск используя Docker
- [x] Использование environment variables
- [x] Просмотр Django Моделей в Django Admin панели
- [ ] Запуск приложения на удаленном сервере, доступном для тестирования
- [ ] Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- [ ] Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
- [ ] Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
- [ ] Реализовать не Stripe Session, а Stripe Payment Intent.

---
Надеюсь на обратную связь :)
<h4 align="right">Андрей Пивоваров, 2022</h4> 

