#Input currency in rupees and output in USD.

conversion_rate = 83.5
currency_input = float(input("Please Enter the currency in Rupees: "))

usd = currency_input/conversion_rate
print(f"{currency_input} INR  is approximately {usd:.2f} USD")

