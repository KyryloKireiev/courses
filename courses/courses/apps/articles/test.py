import datetime
from django.utils import timezone


a = '2011-02-03'
b = '2022-05-03'

begin_search =a.replace('-', '')
end_search = b.replace('-', '')

start = datetime.datetime.strptime(begin_search, '%Y%m%d')
new_end = datetime.datetime.strptime(end_search, '%Y%m%d')

print(start)
print(new_end)

t = "Cffsd SSS"
print(t.lower())

