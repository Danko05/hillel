x = int(input('Введіть число:'))
if 0 <= x <= 8640000:
    s = 0
    m = 60
    h = 3600
    d = 86400

    days, x = divmod(x, d)
    hours, x = divmod(x, h)
    minutes, x = divmod(x, m)
    seconds = x

    a = ''
    if 5 <= days <= 20 or days == 11 or days == 0 or 6 <= days % 10 <= 9 :
        a = 'днів,'
    elif days % 10 == 1:
        a = 'день,'
    elif 2 <= days % 10 <= 4:
        a = 'дні,'
    print(days, a, str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2))

else:
    print('Введіть число від 0 до 8640000')
