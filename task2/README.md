## Локальный запуск скриншотных тестов

1. `cd task2` - перейти в папку второго задания
2. `poetry shell` - создать виртуальное окружение
3. `poetry install` - установить зависимости
4. `pytest` - запуск тестов

Результаты тестов располагаются в папке `output`. 

Изменить папку расположения скриншотов можно с помощью изменения переменной `OUTPUT_SCREENSHOT_FOLDER`, которая располагается в файле `constants.py`