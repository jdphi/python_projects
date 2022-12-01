def sals_shipping(weight):

  if weight > 10:
    gr_price = 4.75*(weight) + 20
    drone_price = 14.25*(weight)
  elif weight > 6:
    gr_price = 4.00*(weight) + 20
    drone_price = 12.00*(weight)
  elif weight > 2:
    gr_price = 3.00*(weight) + 20
    drone_price = 9.00*(weight)
  else:
    gr_price = 1.50*(weight) + 20
    drone_price = 4.50*(weight)

  gr_premium = 125

  if gr_price < drone_price and gr_price < gr_premium:
    return 'ground shipping is best with price of : ' + str(gr_price)
  elif drone_price < gr_price and drone_price < gr_premium:
    return 'drone shipping is best with price of : ' + str(drone_price)
  elif gr_premium < drone_price and gr_premium < gr_price:
    return 'ground premium is best with price of : ' + str(gr_premium)
  elif gr_price == gr_premium or gr_price == drone_price:
    return 'ground shipping with price of : ' +str(gr_price)
  elif drone_price == gr_price or drone_price == gr_premium:
    return 'drone shipping with price of : ' + str(drone_price)
  else: return 'premium ground shipping with price of : ' + str(gr_premium)

print(sals_shipping(6))


