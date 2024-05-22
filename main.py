import csv


with open('data.csv', 'a',newline ='') as f:
     date = input('Please type the date for the following products: ')
     counter = int(input('Please type the amount of products you would like to add'))
     while counter != 0:
     
          item = input('Type item name: ')
          price = (input('Type Price: '))
          quantity = (input('Type Quantity: '))
          f.writerow((item,date, price, quantity))

          counter -=1
     f.close()


