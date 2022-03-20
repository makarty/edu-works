# Подготовка виртуального окружения

## Установка библиотек

```bash
sudo apt install doxygen
```

## Сборка программы

Создание исполняемых файлов

```bash
gcc -pthread -o main main.c
```

Генерация документации(опционально)

```bash
doxygen Doxyfile
```
