// script.js
const map = L.map('map').setView([0, 0], 2); // Set initial view coordinates and zoom level

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add this to script.js
function addGeoJSONLayer(data, style) {
    L.geoJSON(data, {
        style: style,
    }).addTo(map);
}

// Example usage
const geoJsonData = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]  // Replace with actual longitude and latitude values
            },
            "properties": {
                "name": "Sample Point",
                "description": "This is a sample point feature"
            }
        },
        // Add more features as needed
    ]
};

const layerStyle = { color: 'red', weight: 2, opacity: 1 }; // Customize style
addGeoJSONLayer(geoJsonData, layerStyle);


// Assuming your GeoJSON file is named 'your_data.geojson'
fetch('path/to/your_data.geojson')
    .then(response => response.json())
    .then(data => {
        const geoJsonData = data;
        // Now you can use the geoJsonData in your application
    })
    .catch(error => console.error('Error loading GeoJSON data:', error));


    
    // Add this to script.js
function geocodeAddress() {
    const address = document.getElementById('search-input').value;

    // Implement geocoding API call (e.g., using OpenCage Geocoding API)
    // Update map view with the geocoded coordinates
}
