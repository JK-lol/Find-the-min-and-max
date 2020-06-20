largest= -1
smallest= None
while True:
    num=input('Enter a number: ')
    if num == 'done':
        break
    try:
        fn= float(num)
    except:
        print('Invalid input')
        continue
    if num> largest:
      largest=num
    elif num< smallest:
      smallest=num

print('Maximum is',largest)
print('Minumum is',smallest)