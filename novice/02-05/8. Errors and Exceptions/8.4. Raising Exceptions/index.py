# raise NameError('HiThere'):
 File "<stdin>", line 1, in <module>
NameError: HiThere
raise ValueError

try:
      raise NameError('HiThere')
  except NameError:
      print('An exception flew by!')
      raise

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>