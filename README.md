# Пререквизиты

pymystem3, nltk, Python 3.x 

pip install pymystem3, nltk
ИЛИ самостоятельно

# Установка 
зайти в \Lib\site-packages
git clone https://github.com/Nowow/morphodelilka.git
ИЛИ в папку вашего проекта/virtualenv

# Использование 
import morphodelilka.prjscript as morphSep 

разбор слова 
var = morphSep.morphSplitnCheck(слово)

выбор морфем:
var.root, .prefix, .second_prefix, .suffix, .postfix, .extraRoot, .extraPrefix, .interfix

увидеть разделенное слово:
var.separated
