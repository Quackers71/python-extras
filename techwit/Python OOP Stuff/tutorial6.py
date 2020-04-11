import mod
from mod import NotPrivate, _Private

test1 = NotPrivate('pops')
test1.display() # This executes the public method from the file mod.py

test2 = _Private('fluffy')
test2._Display() # note capital 'D'

test3 = NotPrivate('dex')
test3._output()
