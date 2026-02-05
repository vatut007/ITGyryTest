# ITGyryTest
[Задание](https://docs.google.com/document/d/1IXCY12SSbktV2XM_X9tuIdnfpj1ZEnN05wCOhef5wpk/edit?tab=t.0)
## Схема база данных. Задание 1

Ознакомится со схемой базы данных можно по [ссылке](https://drawsql.app/teams/vatut007/diagrams/itgyrytest)

## SQl запросы. Задание 2 

Запросы находятся в папке sql_query

## Сервис апи

Для запуска нужно перейти в папку app
```bash
    cd app
```

Создать .env в app/.env со следующими переменными

```env
DB_NAME=shop_db
DB_PASSWORD=super
DB_USER=super
DB_ADDRESS=db
DB_PORT=5432
```
Выполнить 

```bash
docker-compose up -d 
```

Сервис будет доступен по http://localhost:8000/api/v1
Документация http://localhost:8000/api/v1/docs

Можно выполнить запрос по /v1/add_product

```json
{
  "order_id": 1,
  "product_id": 1,
  "quantity": 1
}
```

В заказ 1 добавится продукт 1 с количеством 1

Если выполнить 
```json

{
  "order_id": 1,
  "product_id": 1,
  "quantity": 100
}
```

Получим уведомеление что нет продукта в таком количестве