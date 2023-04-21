from django import template


register = template.Library()

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name= ’currency_AD’ )


def currency(value):
   """
   value: значение, к которому нужно применить фильтр
   """
   #"""
   #value = ["fuck", "bitch", "Заголовок"]
   #"""
   # Возвращаемое функцией значение подставится в шаблон.
   return f'*'

#chars = ["*","#","%","&","?","@"]
#bw  = ["fuck", "bitch"]
#txt = 'Fuck you  fucker bitch'.lower().split(' ')

#for word in txt:
    #if word in bw:
        #temp = random.sample(chars, len(word))
        #i = ''.join(temp)
        #txt = [x.replace(word, i) for x in txt]

#res = ' '.join(txt)