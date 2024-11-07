import an_bisect
from datetime import datetime

print(an_bisect)
print(an_bisect.__doc__)
print(an_bisect.filtreaza_anii)
print(an_bisect.filtreaza_anii.__doc__)

print(an_bisect.__name__)


print(__name__)

rezultat = an_bisect.filtreaza_anii(1999, 2000, 2003)

print(rezultat)

