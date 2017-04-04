# morphodelilka

установка - склонировать репозиторий (залить все файлы в папку) в место, где лежат все библиотеки (обычно  Дистрибутив\Lib\site-packages)

импорт - from morphodelilka import prjscript
или имя папки, куда залили файлы вместо morphodelilka

разбор слова - prjscript.MorphSplitnCheck(слово)

морфемы - обьект.root, .prefix, .suffix, .postfix, .extraRoot, .extraPrefix, .interfix
разделенное слово графически - объект.separated
