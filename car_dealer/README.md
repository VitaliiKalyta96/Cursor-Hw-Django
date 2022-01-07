# Setup

#### Create local env file

Just run `make test_env`


#### Build containers

`docker-compose -f docker-compose-dev.yml build`

#### In order run project to production.

`docker-compose -f docker-compose-prod.yml build`

#### Before running project

- Create local env file
- Build containers
- Run project

#### Run project

`docker-compose -f docker-compose-dev.yml up`

or

`docker-compose -f docker-compose-prod.yml up`

# Short overview

### This is main page project car_dealer.
![Screenshot from 2021-12-31 02-15-46](https://user-images.githubusercontent.com/86627796/147828004-e64e7d19-8df6-475d-9f24-ffd51f3ed7e7.png)


### Go to the dealer list and you see this such page.

![img_1.png](img_1.png)

### When go to the subscribe/new/ will be next.
![Screenshot from 2021-12-31 02-16-00](https://user-images.githubusercontent.com/86627796/147828046-3f846a32-6bb9-42d6-8e48-9a8ffd14cc1b.png)

### Note. If you want sign up your email success that subscriber and go to 
### success redirect page, first of all you must add email in admin directly in apps 
### newsletters after that sign up and all.=)
![Screenshot from 2021-12-31 02-16-11](https://user-images.githubusercontent.com/86627796/147828059-02fd2314-13b5-44e1-be9b-87255fd07b93.png)
![Screenshot from 2021-12-31 02-16-20](https://user-images.githubusercontent.com/86627796/147828123-7e72fe89-7791-467c-8974-dbdc4c2d7cd5.png)


####! All functions and views unfortunately don't work, but this is min startapp project
#### is called "Car Dealer"

This was short overview project

#### When project is running

- Apply db migrations `make migrations`
- Create superuser `make test_user`. After that you will be able to login into Admin
- Be happy

#### Create new app

`make app name=<app_name>`

### Project description

This is simple project just to demonstrate basic concept of Django.

- You are able to see Django Admin and create some articles in DB.
- You can search recently added articles on /articles/search/ page. 
And see the results on /articles/results/ page.

#### All commands you can find in `Makefile`


# Django course project description:
Проект являє собою журнал-каталог автомобілів іменних брендів.
Іншими словами - це ресурс, що дозволяє знайти автомобіль по заданих критеріях, серед тих що є в наявності в автосалонах.

### Основні ролі:
   - Користувач (той хто підбирає собі автомобіль)
   - Диллер (той хто виставляє автомобілі на продаж)
	
## Сценарії:
- Користувач шукає автомобіль по заданих критеріях використовуючи фільтри на уявному сайті. Він отримує результати свого пошуку з коротким описом знайденого (чи ні :)
- Користувач переходить на одну із обраних автомобілів. Він отримує розгорнутий опис зі всією інформацією про автомобіль
- Користувач підписується на щотижневу розсилку новин. Він отримує останні три випадкові автомобілі з останніх доданих на тижні (або раніше). Він отримує три найпопулярніші автомобілі на поточному тижні.
- Користувач оформляє замовлення на обраний ним автомобіль. Він отримує емейл з підтвердженням, що його заявка розглядається.
- Дилер вводить свої дані для входу в систему. Він отримує дозвіл на роботу з сайтом з свого профіля. (звичайна логінка по ресут)
- Дилер хоче змінити інформацію в своєму профілі. Він це і робить)
- Дилер вводить дані про новий автомобіль. Новий автомобіль створюється зі статусом Pending. 
- Дилер змінює інформацію про свій автомобіль або його “статус”. Його автомобіль оновлено.
- Дилер хоче переглянути всі наявні автомобілі. Йому виводиться список всіх авто але тільки для цього диллера. (Авто інших дилерів не відображаються)
- [Користувач замовив авто] Дилер отримав емейл про нову заявку на автомобіль. Він хоче переглянути всі нові заявки. Він отримує список заявок на автомобіль зі статусом New.
Дилер може міняти статус заявок на авто.