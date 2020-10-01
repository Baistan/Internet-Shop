import requests
API_KEY = "e64802ca4677b6c72cd097c488d64d43-aff2d1b9-298960e4"
API_BASE_URL = " https://api.mailgun.net/v3/sandbox2e8044ecac3849d0bf9459ace44e7dcf.mailgun.org/messages"


def send_email(API_KEY, API_BASE_URL, cartage_list, total):
    response = requests.post(
        API_BASE_URL,
        auth=("api", API_KEY),
        data={"from": "almazbekovbaistan@gmail.com",
              "to": ["maximneveraa@gmail.com", ],
              "subject": "Приобретенные товары",
              "text": [final_list,"Общая стоимость покупки: ", total], })

    print(response)
    return response




def auth(login,password):

   if len(login) < 20 and not password.isalpha() and not password.isdigit():
        return True
   else:
        return False

login = "killer"
password = "12345kill"
login_check = input("Введите имя пользователя: ")
password_check = input("Введите пароль: ")




def counter(money,price):
    if money > price:
        money = money - price
        return money
    else:
        return "Недостаточно средств"




catalogue = {'microphone':1500,'air-pods':4000,'beats':8000,
             'samsung a5': 10500,'Acer ASPIRE e15': 30000,
             'hard drive':6400,'iphone 8s': 16000,'iphone X': 40000,
             'mouse RX7':8000,'hikvision laland':2280,'kocom': 3990,
             'HIKVISION DS-KD-DIS': 5410, 'commaX cdv':9560,
             'TP-LINK TL-WR841N':1450,'hoco m60': 120,
             'SVEN ap':290,'panasonic': 32460,'Falcon sdd ADATA':6650,
             'Apple Watch':8000}

def cartage():
    list_shop = []
    num = 4
    for i in range(num):
        tovar = input("Введите наименование товара: ")
        list_shop.append(tovar)
    return list_shop

purchase = cartage()
print(cartage(),"Товары добавлены в каталог")


final_list = []
for i in purchase:
    final_list.append("Вы купили товар:" + i)

def buy(purchase):
    if auth(login,password):
        money = int(input("Введите кол-во средств для опкупок: "))
        all_money = money
        for bought in purchase:
            if bought in catalogue:
                key_price = catalogue[bought]
                money = counter(money,key_price)

        send_email(API_KEY=API_KEY, API_BASE_URL=API_BASE_URL, cartage_list=final_list, total=all_money-money)
        return money
    else:
        return "Выполните вход!"


print(buy(purchase))



