"""
№6
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""
#  Немного изучал ООП, логично тут сделать банкомат как отдельный объект
#  логично делать класс банкомат

class CacheMachine():
    def __init__(self, amount=0):
        self.amount = float(amount)  # начальная сумма
        self.allowed_banknotes = 50.0

        self.percent_withdrawal = 1.5
        self.min_tax = 30.0
        self.max_tax = 600.0

        self.count_withdrawal = 1
        self.extra_tax = 3.0

        self.rich_tax_summ_max = 5_000_000.0
        self.rich_tax_percent_withdrawal = 10.0

    def over_ammount_tax(self, cash) -> float:
        tax = (cash * self.rich_tax_percent_withdrawal) / 100 if cash > self.rich_tax_summ_max else 0
        return tax

    def counter_tax(self, cash) -> float:
        extra_counter_tax = (cash * self.extra_tax / 100) if self.count_withdrawal % 4 == 0 else 0
        return extra_counter_tax

    def add(self, cash: float):
        float(cash)
        if cash % self.allowed_banknotes == 0:
            tax = self.over_ammount_tax(cash) + self.counter_tax(cash)
            self.amount += cash - tax  # пополнить
            message = (f'Пополнение на сумму: {cash}, на счете: {self.amount}.')
            print(message, f'Nalog included: {tax}') if tax else print(message)
            self.count_withdrawal += 1
        else:
            print(f'Банкомат принимает купюры только кратные {self.allowed_banknotes}')

    def withdrawal_tax(self, cash) -> float:
        tax = (cash * self.percent_withdrawal / 100) + self.counter_tax(cash)
        if cash < self.rich_tax_summ_max:
            if self.min_tax <= tax <= self.max_tax:
                return tax
            elif tax > self.max_tax:
                return self.max_tax
            elif tax < self.min_tax:
                return self.min_tax
        return tax

    def get(self, cash: float):
        float(cash)
        if self.amount >= cash and cash % self.allowed_banknotes == 0:
            tax = self.withdrawal_tax(cash) + self.over_ammount_tax(cash) + self.counter_tax(cash)
            self.amount -= cash + tax
            print(f'Вы сняли: {cash}, заплатили налог {tax}, остаток {self.amount}')
            self.count_withdrawal += 1
        elif self.amount < cash:
            print(f'Не достаточно средств на счёте, остаток: {self.amount}')
        else:
            print(f'Банкомат выдает купюры только кратные {self.allowed_banknotes}')

    def get_balance(self) -> float:
        return self.amount


if __name__ == "__main__":
    b = CacheMachine()
    balance = b.get_balance()

    b.add(100)
    b.add(100)
    b.add(100)
    b.add(100)
    b.add(100)
    # b.add(100)
    b.add(700)
    b.add(6500000)
    #
    b.get(35)
    b.get(100)
    b.get(5500000)
