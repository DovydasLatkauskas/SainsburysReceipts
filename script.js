async function getReceipts() {
    return [
        {
            receipt_id: 123,
            line_items: [
                {
                    name: "Waitrose Essential Oatmilk",
                    price: 1.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/4/LN_718674_BP_4.jpg",
                },
                {
                    name: "Oat Milk Hot Chocolate",
                    price: 2.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/11/LN_595718_BP_11.jpg",
                },
            ],
        },
        {
            receipt_id: 123,
            line_items: [
                {
                    name: "Oat Milk Hot Chocolate",
                    price: 2.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/11/LN_595718_BP_11.jpg",
                },
            ],
        },
        {
            receipt_id: 456,
            line_items: [
                {
                    name: "Milk",
                    price: 2.49,
                    quantity: 2,
                    image_url: "https://assets.sainsburys-groceries.co.uk/gol/1137637/1/640x640.jpg",
                },
            ],
        },
        {
            receipt_id: 456,
            line_items: [
                {
                    name: "Milk",
                    price: 2.49,
                    quantity: 1,
                    image_url: "https://assets.sainsburys-groceries.co.uk/gol/1137637/1/640x640.jpg",
                },
            ],
        },
    ];
}

function importData(data) {
    let input = document.createElement("input");
    input.type = "file";
    input.onchange = (_) => {
        let files = Array.from(input.files);
        //console.log(files);
        data.modal = true;
    };
    input.click();
}

function loadPieChart(el) {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ["Category", "Units"],
            ["Dairy", 3],
            ["Confectionary", 20],
            ["Pizza", 8],
        ]);
        var options = {
            colors: ["#7F0442", "#F06C00", "#837F5D", "#0C1B33", "#7B6080"],
            width: 500,
            height: 400,
            enableInteractivity: false,
            chartArea: { width: "100%", height: "80%" },
            backgroundColor: { fill: "transparent" },
            fontSize: 16,
            pieHole: 0.4,
        };
        var chart = new google.visualization.PieChart(el);
        chart.draw(data, options);
    }
}

async function submitForm(data) {
    console.log(JSON.stringify(data.dataToVerify));
    var response = await fetch("http://localhost:8000/api/submit_receipt", {
        method: "POST",
        mode: "no-cors",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data.dataToVerify),
    });
    // response = await response.json();
    // console.log(JSON.stringify(response));
    data.modal = false;
}

// this doesn't work and I can't fix it :(
let auth0Client = null;
window.onload = async function (e) {
    auth0Client = await window.auth0.createAuth0Client({
        domain: "dev-f1l6uy3hj102ba78.uk.auth0.com",
        clientId: "c0slXneAJT5ne8ULL6U0EOg53WRGhqzQ",
        authorizationParams: {
            redirect_uri: "http://localhost:8000/app.html",
        },
    });
    // await auth0Client.loginWithRedirect();
    // if (
    //     location.search.includes("state=") &&
    //     (location.search.includes("code=") || location.search.includes("error="))
    // ) {
    //     await auth0Client.handleRedirectCallback();
    //     // window.history.replaceState({}, document.title, "/");
    // }
};
