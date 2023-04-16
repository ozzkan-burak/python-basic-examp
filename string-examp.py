stripWord = ' Hello World '
course = 'Python Öğrenmesi kolay OOP 1 Dildir.'
alphabetic = "Merhaba"

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

"""
print(countRangeResult)
print(countResult)
"""

## letter startwith
startWithResult = wordStrip.startswith('www')
startWithResult1 = wordStrip.startswith('a')

## letter endwidth
endwidthResult = wordStrip.endswith('com')
endwidthResult1 = wordStrip.endswith('tr')

"""
print(startWithResult)
print(startWithResult1)
print(endwidthResult)
print(endwidthResult1)
"""
## returns the first letter index
findWordResult = course.find('O')
## if no letter returns -1
findWordResult1 = course.find('Z')
## searches in range, is 
findWordResult2 = course.find('z', 0, 20)

"""
print(findWordResult)
print(findWordResult2)
"""

## searches result with index method
indexMethodResult = course.index('Dildir')
#indexMethodResult1 = course.index('Dildir-')

"""
print(indexMethodResult)
print(indexMethodResult1)
"""
## isAlpha
islAlphaResult = course.isalpha()
islAlphaResult1 = alphabetic.isalpha()

"""
print(islAlphaResult)
print(islAlphaResult1)
"""









