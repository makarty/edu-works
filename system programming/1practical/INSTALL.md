# Подготовка виртуального окружения

## Установка библиотек

```bash
sudo apt update
sudo apt-get install libcunit1 libcunit1-doc libcunit1-dev
sudo apt install doxygen
```

## Сборка программы

Создание исполняемых файлом:

```bash
gcc main.c -o main
gcc ChildProgram.c -o ChildProgram
gcc test.c -o test -lcunit
```

Генерация документации(опционально):

```bash
doxygen Doxyfile
```
