import exchange
#moduel 1 chứa tỉ giả ngoại tệ
usd_to_vnd = 23000
eur_to_vnd = 27000
jpy_to_vnd = 210

schedule = float(input("Nhập vào số dặm bay: "))
money = float(input("Nhập vào số tiền/ dặm: "))
total_money = schedule * money
print('Số tiền VND phải trả là: ', total_money, "VND")
print('Số tiền USD phải trả là: ', round(exchange.vnd_to_usd(total_money), 2), "USD")
print('Số tiền EUR phải trả là: ', round(exchange.eur(total_money), 2), "EUR")
print('Số tiền JPY phải trả là: ', round(exchange.vnd_to_jpy(total_money), 2), "JPY")