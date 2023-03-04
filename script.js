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

function importData() {
    let input = document.createElement("input");
    input.type = "file";
    input.onchange = (_) => {
        let files = Array.from(input.files);
        console.log(files);
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
            chartArea: { width: "100%", height: "80%" },
            backgroundColor: { fill: "transparent" },
            fontSize: 16,
            pieHole: 0.4,
        };
        var chart = new google.visualization.PieChart(el);
        chart.draw(data, options);
    }
}
