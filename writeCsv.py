import csv
import random

price = 200

def change_price(price1):
    global price
    price = price1


last_number = 0
yesterday_revenue = 0
yesterday_offerId = 0

def csv_start():
    global last_number
    global yesterday_revenue
    global yesterday_offerId

    with open("CSV/foodAppOfferIncomeMarging.csv", 'w') as file:
        feildNames = ["number", "offerId","today_rewenue", "tommorow_rewenue", "marginal_rewenue"]
        writter = csv.DictWriter(file, fieldnames=feildNames)
        writter.writeheader()
       # rows = [{"number":1,"offerId":1 , "today_rewenue":1000,"tommorow_rewenue":1500,"marginal_rewenue":500} ,{"number": 2, "offerId": 1, "today_rewenue": 1000, "tommorow_rewenue": 1500, "marginal_rewenue": 500} ]
        #writter.writerows(rows)
        for i in range(1 , 100):
            packet = random.randint(50 , 200)
            tomorrow_packets = packet + random.randint(-2 , 10)
            today_rewenue = packet * price
            tomorrow_revenue = tomorrow_packets * price
            margin_revenue = tomorrow_revenue - today_rewenue
            offer_id = random.randint(1, 10)
            writter.writerow({"number": i, "offerId": offer_id, "today_rewenue": today_rewenue, "tommorow_rewenue": tomorrow_revenue, "marginal_rewenue": margin_revenue})
            last_number+=1
            yesterday_revenue = today_rewenue
            yesterday_offerId = random.randint(1, 10)


def csv_write_new_row(today_packets):
    global last_number
    global yesterday_revenue
    global yesterday_offerId

    today_revenue = today_packets * price
    with open("CSV/foodAppOfferIncomeMarging.csv", 'a') as file:
        feildNames = ["number", "offerId", "today_rewenue", "tommorow_rewenue", "marginal_rewenue"]
        writter = csv.DictWriter(file, fieldnames=feildNames)
        writter.writerow({"number": last_number, "offerId": yesterday_offerId, "today_rewenue": yesterday_revenue, "tommorow_rewenue": today_revenue, "marginal_rewenue": today_revenue - yesterday_revenue})
        last_number+=1
        yesterday_revenue = today_revenue


def set_offer_id(offer_id):
    global yesterday_offerId
    yesterday_offerId = offer_id


