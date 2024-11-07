

# 1. Divizibili cu 400 - sunt bisecti
# 2. Divizibili cu 100 dar nu cu 400 - nu sunt bisecti
# 3. Divizibili cu 4, dar nu cu 100 - sunt bisecti

# În program sunt definite variabilele startDate şi endDate care reprezintă anul iniţial şi cel final.
# Trebuie creată o funcție care, pe baza acestor două valori, va afişa lista anilor bisecți
# Aplicaţia trebuie să aibă o ieşire identică celei de mai jos:

from datetime import datetime

def ani_bisecti(start, stop=datetime.now().year+1):
    return list(range(((start+3) // 4) * 4, stop, 4))

start_year = 2005 # 2001, 2002, 2003 -> 2004
stop_year = 2010

print(ani_bisecti(start_year, stop_year))
print(ani_bisecti(start_year))

