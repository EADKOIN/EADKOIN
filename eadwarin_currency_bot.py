class EADWARINCurrencyBot:
    def __init__(self):
        self.base_values = {
            'usa': 1.00,
            'eu': 1.08,
            'africa': 0.80
        }
        self.inflation_rate = 0.05  # Inflation rate (5%)

    def adjust_currency(self, region):
        if region in self.base_values:
            base_value = self.base_values[region]
            adjusted_value = base_value * (1 + self.inflation_rate)
            return round(adjusted_value, 2)
        else:
            raise ValueError("Region not found in base values")

    def simulate_currency_update(self):
        regions = ['usa', 'eu', 'africa']
        for region in regions:
            new_value = self.adjust_currency(region)
            print(f"Adjusted value for {region.upper()}: {new_value} EADKOIN")

# Instantiate and run the currency bot
currency_bot = EADWARINCurrencyBot()
currency_bot.simulate_currency_update()
