stripWord = ' Hello World '
course = 'Python Öğrenmesi kolay OOP 1 Dildir.'
alphabetic = "Merhaba"
digit = '123'

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

# isdigit method
digitResult = digit.isdigit()

#print(digitResult)

# center method, add lenght parameter and second add chracter

centerResult = alphabetic.center(50, '-')
centerResult1 = alphabetic.center(45, '*')
justResult = alphabetic.ljust(50, '*')
justResult2 = alphabetic.rjust(50, '-')

"""
print(centerResult)
print(centerResult1)
print(justResult)
print(justResult2)
"""

# replace char
replaceResult = course.replace(' ', '-')

#repalce char for ranage
replaceResult1 = course.replace(' ', '-', 3)

#replace delete char
replaceResult2 = course.replace(' ', '')

#replace word
replaceResult3 = stripWord.replace('World', 'There')

print(replaceResult)
print(replaceResult1)
print(replaceResult2)
print(replaceResult3)










