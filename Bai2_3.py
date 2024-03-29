import Travel.Rate.Rate__money
import Travel.Schedule.Schedule__far
schedule = float(input("Nhập vào số dặm bay: "))
money = float(input("Nhập vào số tiền/ dặm: "))
total_money = schedule * money
print('Số tiền VND phải trả là: ', total_money, "VND")
print('Số tiền USD phải trả là: ', round(Travel.Schedule.Schedule__far.vnd_to_usd(total_money), 2), "USD")
print('Số tiền EUR phải trả là: ', round(Travel.Schedule.Schedule__far.eur(total_money), 2), "EUR")
print('Số tiền JPY phải trả là: ', round(Travel.Schedule.Schedule__far.vnd_to_jpy(total_money), 2), "JPY")
