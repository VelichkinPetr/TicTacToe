# TicTacToe
## Описание проекта

Игра "Крестики-нолики" - это простая логическая игра, в которой два игрока 
по очереди ставят крестики и нолики на игровое поле размером 3x3.  
Цель игры - первым составить линию из трех своих знаков по горизонтали, вертикали или диагонали.

## Установка
### Вариант 1. Получить исходный код
1. Склонировать репозиторий
```bash
git clone https://github.com/VelichkinPetr/storage_recipes.git
```
2. Установить необходимые библиотеки
```
pip install customtkinter
pip install pillow
pip install logging 
```
3. Запустить файл TicTacToe.py

### Вариант 2. Получить файл в .exe
1. Скачать по ссылке ==> [TicTacToe.exe](https://disk.yandex.ru/d/VQ-X3owkhkqNLA "кара")


## Функциональные возможности

1. **Игровое поле:**
    - Игровое поле размером 3x3 клетки, на котором игроки могут размещать свои знаки (крестики или нолики).
2. **Режим игры:**
    - Возможность игры против другого игрока (Два игрока).
    - Возможность игры против компьютера (одиночный режим).
3. **Выбор уровня сложности:**
    - Возможность выбора уровня сложности при игре против компьютера [легкий, средний, сложный]. *p.s. режимы реализованы c помощью emoji, слева на право по возрастанию сложности.*
4. **Правила игры:**
    - Поочередные ходы игроков.
    - Проверка на выигрышную комбинацию после каждого хода.
    - Объявление победителя или ничьей после завершения игры.
5. **Графический интерфейс:**
    - Простой и интуитивно понятный интерфейс, отображающий игровое поле и текущий статус игры.
6. **Статистика игр:**
    - Ведение статистики побед, поражений и ничьих для режима игры “Два игрока” и "Одиночный режим".
7. **Темы оформления:**
    - Поддержка смены графических тем для игрового интерфейса. (Светлая и Темная)
8. **История ходов:**
    - Возможность просмотра истории ходов после завершения игры. *steps_history.log - создается автоматически в корневой директории*
9. **Очистка Кэша:**
    - Возможность очистить статистику и историю ходов.

## Технологии

- Язык программирования: Python
- Библиотеки:
  - *CustomTkinter* (для разработки игры), 
  - *Logging* (интерфейс для логирования)
  - *Pillow* (добавляет возможности обработки изображений)
  - *json* (для работы с json файлами для хранений статистики).
