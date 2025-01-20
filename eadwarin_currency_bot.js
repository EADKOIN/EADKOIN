// Initial base values
const baseValues = {
    usa: 1.00,
    eu: 1.08,
    africa: 0.80
};

// Inflation percentage for the adjustment
const inflationRate = 0.05; // 5% inflation increase

function adjustCurrency() {
    document.getElementById("usa-value").innerText = (baseValues.usa * (1 + inflationRate)).toFixed(2);
    document.getElementById("eu-value").innerText = (baseValues.eu * (1 + inflationRate)).toFixed(2);
    document.getElementById("africa-value").innerText = (baseValues.africa * (1 + inflationRate)).toFixed(2);
}
