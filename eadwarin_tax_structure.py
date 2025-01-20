class TaxStructure:
    def __init__(self):
        self.tax_rates = {
            'usa': 10,
            'eu': 12,
            'africa': 7
        }
        self.inflation_rate = 0.05  # Inflation rate (5%)

    def adjust_tax_rate(self, region):
        if region in self.tax_rates:
            base_rate = self.tax_rates[region]
            adjusted_rate = base_rate * (1 + self.inflation_rate)
            return round(adjusted_rate, 2)
        else:
            raise ValueError("Region not found in tax rates")

    def simulate_tax_updates(self):
        regions = ['usa', 'eu', 'africa']
        for region in regions:
            new_rate = self.adjust_tax_rate(region)
            print(f"Adjusted tax rate for {region.upper()}: {new_rate}%")

# Instantiate and simulate tax updates
tax_structure = TaxStructure()
tax_structure.simulate_tax_updates()
