// Variables globales
const resultsDiv = document.getElementById('results');
const volumeInput = document.getElementById('volume');

// Constantes para cálculos
const TEU_CAPACITY = 33.2;  // Capacidad en metros cúbicos por TEU
const LCL_THRESHOLD = 20.0; // Umbral para recomendación de LCL

// Función principal para calcular TEUs
function calculateTEUs() {
    // Limpiar resultados anteriores
    resultsDiv.innerHTML = '';

    // Obtener el volumen ingresado
    const volume = parseFloat(volumeInput.value);

    if (isNaN(volume) || volume <= 0) {
        showError('Por favor, ingrese un número válido mayor que 0');
        return;
    }

    // Calcular TEUs necesarios
    const teus = Math.ceil(volume / TEU_CAPACITY);
    const capacityUsed = teus * TEU_CAPACITY;

    // Determinar tipo de envío recomendado
    const recommendation = volume < LCL_THRESHOLD 
        ? 'Recomendación: Envío LCL' 
        : `Recomendación: Envío en ${teus} TEUs`;

    // Mostrar resultados
    displayResults(volume, teus, capacityUsed, recommendation);
}

// Función para mostrar resultados
function displayResults(volume, teus, capacityUsed, recommendation) {
    const results = `
        <h2>Resultados</h2>
        <p>Para ${volume} m³ se necesitan ${teus} TEUs</p>
        <p>Capacidad total utilizada: ${capacityUsed.toFixed(1)} m³</p>
        <p>${recommendation}</p>
    `;
    
    resultsDiv.innerHTML = results;
}

// Función para mostrar errores
function showError(message) {
    resultsDiv.innerHTML = `
        <div class="error">${message}</div>
    `;
}

// Agregar evento de tecla enter
volumeInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculateTEUs();
    }
});
