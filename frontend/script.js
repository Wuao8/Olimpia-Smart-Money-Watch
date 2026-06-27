const API = "https://olimpia-smart-money-watch.onrender.com";

async function loadData() {
    try {
        const response = await fetch(API);
        const data = await response.json();

        console.log("API RESPONSE:", data);

        const table = document.getElementById("tableBody");
        table.innerHTML = "";

        // sicurezza anti crash
        const signals = data.signals || [];

        // ordina per score
        signals.sort((a, b) => b.score - a.score);

        // TOP SIGNAL
        if (signals.length > 0) {
            const top = signals[0];

            document.getElementById("topSignal").innerText =
                `${top.asset} (${top.action})`;

            document.getElementById("topScore").innerText =
                top.score;

            document.getElementById("cryptoCount").innerText =
                signals.filter(s => s.market === "Crypto").length;
        }

        // TABLE
        signals.forEach(signal => {
            table.innerHTML += `
                <tr>
                    <td>${signal.market}</td>
                    <td>${signal.asset}</td>
                    <td>${signal.action}</td>
                    <td>${signal.size}</td>
                    <td>${signal.who}</td>
                    <td>${signal.source}</td>
                    <td>${signal.score}</td>
                </tr>
            `;
        });

    } catch (err) {
        console.error("Error loading data:", err);
    }
}

// init
loadData();

// refresh ogni 10 secondi
setInterval(loadData, 10000);
