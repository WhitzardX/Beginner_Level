import time
def slow (text, delay = 0.5):
      ''' loops through the text to print each letter slowly in respect to delay time,  flush =True'''
      for char in text:
      	print(char,end ='',flush =True)
      	time.sleep(delay)
      print()
      
def slow_no_flush(text, delay = 0.5):
      ''' loops through the text to print each letter slowly in respect to delay time, flush =False'''
      for char in text:
      	print(char,end ='')
      	time.sleep(delay)
      print()
	
text= 'Hello!! \nMoshi! Moshi!!'
delay = 0.05
slow(text,delay)

text = 'This is Stephen speaking!!, '
slow(text,0.1)

text = '\tCan someone please tell me '
slow(text,0.03)

text= 'WHAT \n\tTHE \n\t\t F%#k '
slow_no_flush(text,0.1)
text= '\t\t\tis going on!! '
slow(text,0.04)
