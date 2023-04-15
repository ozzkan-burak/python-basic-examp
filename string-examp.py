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

## count letter for word
countResult = course.count('i')
## cont for range
countRangeResult = course.count('i',10, 20)

print(countResult)
print(countRangeResult)




