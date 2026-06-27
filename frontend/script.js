const API = "https://olimpia-smart-money-watch.onrender.com";

async function loadData() {
    try {
        const response = await fetch(API);
        const data = await response.json();

        const table = document.getElementById("tableBody");
        table.innerHTML = "";

        // sort by score
        const signals = data.signals.sort((a, b) => b.score - a.score);

        // TOP SIGNAL
        const top = signals[0];
        document.getElementById("topSignal").innerText =
            `${top.asset} (${top.action})`;

        document.getElementById("topScore").innerText =
            top.score;

        document.getElementById("cryptoCount").innerText =
            signals.filter(s => s.market === "Crypto").length;

        // TABLE
        signals.forEach(signal => {
            table.innerHTML += `
                <tr>
                    <td>${signal.market}</td>
                    <td><b>${signal.asset}</b></td>
                    <td>${signal.action}</td>
                    <td>${signal.size}</td>
                    <td>${signal.who}</td>
                    <td>${signal.source}</td>
                    <td><b>${signal.score}</b></td>
                </tr>
            `;
        });

    } catch (err) {
        console.error("Error loading data:", err);
    }
}

loadData();
setInterval(loadData, 10000);
