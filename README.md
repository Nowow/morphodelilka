# morphodelilka

установка - склонировать репозиторий (залить все файлы в папку) в место, где лежат все библиотеки (обычно  Дистрибутив\Lib\site-packages). snowball.py положить в nltk\stem

ИЛИ установить морфочекер https://github.com/IvankovCL/heritage_morphchecker2.0 и воспользоваться prjscript.py там

пререквизиты - pymystem3, nltk

импорт - import morphodelilka (или соответствующие инструкции из морфчекера, если поставлен он)
или имя папки, куда залили файлы вместо morphodelilka

разбор слова - prjscript.MorphSplitnCheck(слово)

морфемы - обьект.root, .prefix, .suffix, .postfix, .extraRoot, .extraPrefix, .interfix
разделенное слово графически - объект.separated
