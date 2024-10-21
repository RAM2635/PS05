# Lighting Spider

Этот проект представляет собой паука, написанного на Scrapy, предназначенного для сбора информации о светильниках с сайта `divan.ru`, конкретно для региона Ставрополь. Пауку извлекает информацию, такую как название, цена и URL каждого светильника, представленного на странице.

## Предварительные требования

Для запуска этого паука необходимо иметь установленный Python и Scrapy. Вы можете установить Scrapy с помощью pip:

```bash
pip install scrapy
```

## Детали паука

- **Имя паука:** `lightingspider`
- **Разрешенные домены:** Пауку ограничен для сбора данных только с `divan.ru`.
- **Начальный URL:** Процесс сбора данных начинается с `https://www.divan.ru/stavropol/category/svet`.

## Как это работает

1. **Инициализация:** Пауку начинает работу с URL, указанного в `start_urls`.
2. **Парсинг:** Метод `parse` обрабатывает ответ от начального URL. Он ищет элементы, содержащие детали о светильниках, используя CSS-селекторы.
3. **Извлечение данных:** Для каждого найденного светильника:
   - Извлекается название продукта с помощью CSS-селектора `div.lsooF span::text`.
   - Извлекается цена продукта с помощью CSS-селектора `div.pY3d2 span::text`.
   - Извлекается URL продукта, используя атрибут `href` тега ссылки.
4. **Вывод:** Извлеченные данные возвращаются в виде словаря, содержащего `name`, `price` и `url`.

## Конфигурация

Убедитесь, что CSS-селекторы, используемые в пауке (`div._Ud0k`, `div.lsooF span::text`, `div.pY3d2 span::text`), являются актуальными и соответствуют реальной структуре веб-страницы, которую вы парсите. Возможно, вам потребуется обновить эти селекторы, если структура сайта изменится.

## Использование

Чтобы запустить паука и сохранить вывод в файл (например, `lightings.json`), используйте следующую команду в терминале:

```bash
scrapy runspider lightingspider.py -o lightings.json
```

Эта команда выпол

Нейрокот, [21.10.2024 16:13]
нит паука и сохранит извлеченные данные в `lightings.json`.

## Заметки

- **Соблюдайте условия использования сайта:** Убедитесь, что ваши действия по парсингу соответствуют условиям использования `divan.ru`.
- **Обработка изменений:** Веб-сайты часто изменяют свою структуру, что может потребовать обновления CSS-селекторов в пауке.
- **Расширяемость:** Вы можете расширить этого паука для обработки пагинации или извлечения дополнительных полей по мере необходимости. Настройте CSS-селекторы и логику в методе `parse` соответствующим образом.

## Заключение

Этот паук Scrapy является базовым примером веб-скрапинга для образовательных целей. Его можно модифицировать и расширять для более сложных задач или других веб-сайтов.