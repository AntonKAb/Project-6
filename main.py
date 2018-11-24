
def dividends_calc(amount, D_dev, S_dev, S_am):
    ''' Посчет дивидендов.'''
    DPS = (D_dev  - S_dev) / S_am
    dividends_1 = DPS * amount
    print('Дивиденд с акций:', round(dividends_1, 2))

def dividend_yield_calc(price, D_dev, S_dev, S_am):
    ''' Посчет дивидендной доходности. '''
    DPS_2 = (D_dev - S_dev) / S_am
    dividend_yield = DPS_2 / price
    print('Дивидендной доходность:', round(dividend_yield, 2) * 100, '%')

def main():
    amount = float(input('Введите количество акций, которыми Вы владеете:'))
    price = float(input('Введите цену одной акции в $:'))
    D_dev = float(input('Cумма, выплачиваемая в виде регулярных дивидендов:'))
    S_dev = float(input('Сумма, выплачиваемая в в виде специальных (разовых) дивидендов:'))
    S_am = float(input('Общее количество акций компании:'))
    dividends_calc(amount, D_dev, S_dev, S_am)
    dividend_yield_calc(price, D_dev, S_dev, S_am)

if __name__ == '__main__':
    main()