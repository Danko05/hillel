x = 950400
s = 0
m = 60
h = 3600
d = 86400
days, x = divmod(x, d)
print(days)
hours, x = divmod(x, h)
print(hours)
minutes, x = divmod(x, m)
print(minutes)
seconds = x
print(seconds)
if days % 10 == 1:
    print('день')
elif 2 <= days % 10 <= 4 and days % 10 == 0:
    print('днів')
print(days, str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2))

