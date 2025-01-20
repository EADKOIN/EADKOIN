from currency_bot import EADWARINCurrencyBot

inflation_rate = 0.05
currency_bot = EADWARINCurrencyBot()

def adjust_for_inflation():
    currency_bot.simulate_currency_update()

if __name__ == "__main__":
    adjust_for_inflation()
