async function getDashboard(data) {
    var response = await fetch("http://localhost:8000/api/dashboard", {
        method: "GET",
        headers: {
            Accept: "application/json",
        },
    });
    response = await response.json();
    data.nectar_points = response.nectar_points;
    data.expenses = response.expenses;
    data.category_data = response.category_data;
}

async function getReceipts() {
    var response = await fetch("http://localhost:8000/api/history", {
        method: "GET",
        headers: {
            Accept: "application/json",
        },
    });
    response = await response.json();
    return response;
}

function importData(data) {
    let input = document.createElement("input");
    input.type = "file";
    input.onchange = async (_) => {
        data.modal = true;
        data.receipt_status = "Loading...";
        var form = new FormData();
        form.append("my_file", input.files[0]);
        // form.append("my_file", dataString);
        var response = await fetch("http://localhost:8000/api/uploadfile", {
            // Your POST endpoint
            method: "POST",
            body: form,
        });
        data.receipt_status = "Upload successful";
        response = await response.json();
        data.dataToVerify = response;
    };
    input.click();
}

function loadPieChart(el, category_data) {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([["Category", "Units"]].concat(Object.entries(category_data)));
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
    data.modal = false;
    data.dataToVerify = false;
}

async function login() {
    await auth0Client.loginWithRedirect();
}

async function logout() {
    await auth0Client.logout();
}

async function loginLogoutFlow() {
    if (await auth0Client.isAuthenticated()) {
        logout();
    } else {
        login();
    }
}

let auth0Client = null;
async function onPageLoad(data) {
    window.onload = async function (e) {
        auth0Client = await window.auth0.createAuth0Client({
            domain: "dev-f1l6uy3hj102ba78.uk.auth0.com",
            clientId: "c0slXneAJT5ne8ULL6U0EOg53WRGhqzQ",
            authorizationParams: {
                redirect_uri: "http://localhost:3000/app.html",
            },
        });
        if (
            location.search.includes("state=") &&
            (location.search.includes("code=") || location.search.includes("error="))
        ) {
            await auth0Client.handleRedirectCallback();
            window.history.replaceState({}, document.title, "/app.html");
        }
        if (await auth0Client.isAuthenticated()) {
            const user = await auth0Client.getUser();
            data.message = "Welcome, " + user.given_name + "!";
            data.login_button_text = "Logout";
        } else {
            data.message = "Welcome!";
        }
    };
}
