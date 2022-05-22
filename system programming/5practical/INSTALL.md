# Подготовка виртуального окружения

## Установка библиотек

```bash
sudo apt install doxygen
```

## Сборка программы

Создание исполняемых файлов

```bash
make -f Makefile
```

Удаление исполняемых файлов

```bash
make clean
```

Создание файла конфигурации Doxyfile(если его не существует)

```bash
doxygen -g Doxyfile
```

Генерация документации(опционально)

```bash
doxygen Doxyfile
```
