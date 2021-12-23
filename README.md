## Клонирование и установка зависимостей

Рассчитано на работу с venv.
После создания нового чистого окружения venv открываем его консоль и закидываем в него необходимые пакеты:
```
pip install -r packages.list
```
Чтобы не проебать версии пакетиков, после клонирования требуется создать в `cirnaba/.git/hooks/` файл `prepare-commit-msg` со следующим содержимым:
```
#!/bin/sh
. <путь-к-окружению>/venv/Scripts/activate
pip freeze > packages.list
```
Например, для следующей структуры каталогов:
```
cirnaba-project
    venv          # чистое виртуальное окружение  
    cirnaba       # этот репозиторий
        .git
        ... 
```
cкрипт должен иметь следующее содержимое:
```
#!/bin/sh
. ../venv/Scripts/activate
pip freeze > packages.list
```
