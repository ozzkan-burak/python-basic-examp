stripWord = ' Hello World '

## iki taraftan boşlukları siler
stripResult = stripWord.strip()
## soldan boşluk siler
stripResultForLeft = stripWord.lstrip()
## sağdan boşluk siler
stripResultForRight = stripWord.rstrip()

"""
print(stripResult)
print(stripResultForLeft)
print(stripResultForRight)
"""

## word strip
## letter delete for word

wordStrip = 'www.burayaeklenenkelime.com.tr'

wordStripResult = wordStrip.strip('w.comtr')

#print(wordStripResult)

course = 'Python Öğrenmesi kolay OOP bir Dildir.'

lowerCaseResult = course.lower()
upperCaseResult = course.upper()
titleResult = course.title()

"""
print(lowerCaseResult)
print(upperCaseResult)
print(titleResult)
"""




