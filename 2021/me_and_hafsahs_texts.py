from time import sleep as s


my_day = 'making my day'
thanking = ' thanking me for'
thanku = ' thanking you for'
yr_day = 'making yr day'


def send_text(yr_day, my_day, thanking, thanku, n, text):
    if n == 500:
        exit()
    if n == -1:
        print('Hafsah: ', text, my_day, '\n')
        print()
    n += 1
    if not n % 2:
        text += thanking
        print('Rami: ', text, yr_day, 'that made my day\n')
        print()
        return send_text(yr_day, my_day, thanking, thanku, n, text)
    if n % 2:
        text += thanku
        print('Hafsah: ', text, my_day, 'that made my day\n')
        print()
        return send_text(yr_day, my_day, thanking, thanku, n, text)


send_text(yr_day, my_day, thanking, thanku, n=-1, text='Aw thank you for')


def get_gpa(list):
    sum_of_gpas = 0
    for gpa in list:
        sum_of_gpas += gpa
    print(sum_of_gpas)
    average = sum_of_gpas/len(list)
    return average


list_of_gpas = [3.7, 3.7, 4, 4, 4]
avg = get_gpa(list_of_gpas)
print(avg)
print(sum(list_of_gpas)/len(list_of_gpas))
