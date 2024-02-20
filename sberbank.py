from decimal import Decimal
from enum import Enum


class AssetPrice(Enum):
    """
    Основной функционал
    """
    # Котировальный список активов.
    LKOH = Decimal(5896)
    SBER = Decimal(250)
    # Количество активов в портфеле
    NUMBER_ASSETS = {
        "LKOH": 0,
        "SBER": 0,
    }

    def asset_buy(self):
        """
        Метод для покупки активов на финансовом рынке
        """
        quantity_buy = input(
            f'\nКакое количество {self.name} по цене {self.value} руб/шт. вы хотели бы приобрести?\n'
        )

        approve_buy = input(
            f'Подтвердите покупку {quantity_buy} активов {self.name}.| '
            f'Стоимостью {Decimal(quantity_buy) * self.value} руб.'
            f'\n 1 - да\n 2 - нет\n')

        if int(approve_buy) == 1:
            print(f'Вы успешно приобрели {self.name} в количестве {quantity_buy}/шт\n')
            # Обновление кол-ва активов, путем замены дефолтного значения на полученое при покупке
            AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value[self.name] += int(quantity_buy)
        else:
            print('Покупка отменена\n')

    def asset_sell(self):
        """
        Метод для продажи активов на финансовом рынке
        """
        quantity_sell = input(f'\nКакое количество {self.name} по цене {self.value}руб/шт. вы хотели бы продать?\n')

        aprove_sell = input(
            f'Подтвердите продажу {quantity_sell} активов {self.name}.| '
            f'Стоимостью {Decimal(quantity_sell) * self.value} руб.'
            f'\n 1 - да\n 2 - нет\n')

        if int(aprove_sell) == 1:
            if AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value[self.name] >= int(quantity_sell):
                print(f'Вы успешно продали {self.name} в количестве {quantity_sell}/шт\n')
                # Обновление кол-ва активов, путем замены дефолтного значения на полученое при покупке
                AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value[self.name] -= int(quantity_sell)
            else:
                print('У вас нет столько ативов!')
        else:
            print('Продажа отменена\n')

    def getting_price_portfolio(self):
        """
        Метод получения текущей стоимости портфеля
        """
        # Стоимость всех акций Лукоил
        lukoil_assets = self.LKOH.value * Decimal(
            AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value["LKOH"]
        )

        # Стоимость всех акций Сбербанка
        sber_assets = self.SBER.value * Decimal(
            AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value["SBER"]
        )

        # Получение конечной стоимости портфеля
        print(f'\nСтоимость портфеля: {lukoil_assets + sber_assets} руб. \n'
              f'Кол-во: {self.LKOH.name} : {AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value["LKOH"]}| '
              f'Общая цена: {lukoil_assets} руб. \n'
              f'Кол-во: {self.SBER.name} : {AssetPrice.NUMBER_ASSETS.__getattribute__("NUMBER_ASSETS").value["SBER"]}| '
              f'Общая цена: {sber_assets} руб. \n')


if __name__ == "__main__":
    print('Добро пожаловать в симулятор торговли финансовыми активами от СБЕРа.\n'
          'Управление осуществляется цифрами.')

    while True:
        select_asset = int(input('1) Управлять активами СБЕР\n'
                                 '2) Управлять активами ЛУКОИЛ\n'
                                 '3) Посмотреть стоимость портфеля\n'
                                 '4) Выход\n'
                                 'Введите цифру: '))

        if select_asset == 1:
            print('Добро пожаловать в управление активами СБЕР')
            SBERBANK = AssetPrice.SBER
            select_method = int(input('1) Купить\n'
                                      '2) Продать\n'
                                      'Введите цифру: '))
            if select_method == 1:
                SBERBANK.asset_buy()
            elif select_method == 2:
                SBERBANK.asset_sell()
            else:
                print('Выберите один из доступных методов\n')

        elif select_asset == 2:
            print('Добро пожаловать в управление активами ЛУКОИЛ')
            LUKOIL = AssetPrice.LKOH
            select_method = int(input('1) Купить\n'
                                      '2) Продать\n'
                                      'Введите цифру: '))
            if select_method == 1:
                LUKOIL.asset_buy()
            elif select_method == 2:
                LUKOIL.asset_sell()
            else:
                print('Выберите один из доступных методов\n')

        elif select_asset == 3:
            PORTFOLIOVALUE = AssetPrice.NUMBER_ASSETS
            PORTFOLIOVALUE.getting_price_portfolio()

        elif select_asset == 4:
            print('До встречи!')
            break

        else:
            print('Выберите одну из указаных цифр выше!\n')
