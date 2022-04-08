first = float(input('How much first do you want (first price: 4000 UZS)'))
second = float(input('How much do you want to buy from second ? (1 liter of second: 6000 UZS)'))
third = float(input('How much do you want to buy from third ? (1 kilo of third: 70000 UZS)'))
fourth = float(input('How much do you want to buy from fourth ? (1 kilo of fourth: 15000 UZS)'))
fifth = float(input('How much do you want to buy from fifth ? (1 package of fifth: 3000 UZS)'))

firstTot = first * 4000
secondTot = second * 6000
thirdTot = third * 70000
fourthTot = fourth * 15000
fifthTot = fifth * 3000

total = thirdTot + secondTot + thirdTot + fourthTot + fifthTot

print('First: {0}, Second: {1}, Third: {2}, Fourth: {3}, Fifth: {4}. Total: {5}'.format(firstTot, secondTot, thirdTot, fourthTot, fifthTot, total))