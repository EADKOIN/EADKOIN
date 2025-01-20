const baseValues = {
    usa: 1.00,
    eu: 1.08,
    africa: 0.80
};

const inflationRate = 0.05;

function adjustCurrency() {
    document.getElementById("usa-value").innerText = (baseValues.usa * (1 + inflationRate)).toFixed(2);
    document.getElementById("eu-value").innerText = (baseValues.eu * (1 + inflationRate)).toFixed(2);
    document.getElementById("africa-value").innerText = (baseValues.africa * (1 + inflationRate)).toFixed(2);
}
