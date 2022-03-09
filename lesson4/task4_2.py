from requests import get


def currency_get():
    """function to get the list of names and values of all currencies for today"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_rate = []
    for el in response.split('<CharCode>')[1:]:
        cur_list = []
        currency_name = el.split('</CharCode>')[0]
        v = ((el.split('<Value>')[1]).split('</Value>')[0]).replace(',', '.')
        value = float(v)
        nominal = int(el.split('<Nominal>')[1].split('</Nominal')[0])
        cur_list.append(currency_name)
        cur_list.append(value)
        cur_list.append(nominal)
        currency_rate.append(cur_list)
    return currency_rate


def currency_rates(currency_name):
    """ function to print the value of certain currency"""
    for el in currency_get():
        if el[0] == currency_name:
            print(f'Курс {currency_name} на сегодня равен {round(el[1], 2)} руб. за {el[2]} {el[0]}')
        else:
            print('неверный код валюты')
            break


if __name__ == "__main__":
    n = input('Введите обозначение валюты: ')
    currency_rates(n)
