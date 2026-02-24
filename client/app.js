window.onload = function () {
    loadCities();

    // Area slider live update
    let areaSlider = document.getElementById("area");
    let areaValue = document.getElementById("areaValue");

    areaValue.innerText = areaSlider.value;

    areaSlider.oninput = function () {
        areaValue.innerText = this.value;
    };
};

function loadCities() {
    fetch("http://127.0.0.1:5000/get_city_names")
        .then(response => response.json())
        .then(data => {
            let citySelect = document.getElementById("city");
            data.cities.forEach(city => {
                let option = document.createElement("option");
                option.value = city;
                option.text = city;
                citySelect.appendChild(option);
            });
        });
}

function predictRent() {

    let formData = new FormData();

    formData.append("area", document.getElementById("area").value);
    formData.append("beds", document.getElementById("beds").value);
    formData.append("bathrooms", document.getElementById("bathrooms").value);
    formData.append("furnishing", document.getElementById("furnishing").value);
    formData.append("city", document.getElementById("city").value);

    fetch("http://127.0.0.1:5000/predict_rent", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_rent !== undefined) {
            document.getElementById("result").innerText =
                "Estimated Rent: ₹ " + data.predicted_rent.toLocaleString();
        } else {
            document.getElementById("result").innerText =
                "Error: Something went wrong";
        }
    });
}