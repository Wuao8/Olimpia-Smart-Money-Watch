const API="http://127.0.0.1:8000/api/live";

async function loadData(){

const response=await fetch(API);

const data=await response.json();

const table=document.getElementById("tableBody");

table.innerHTML="";

data.signals.forEach(signal=>{

table.innerHTML+=`

<tr>

<td>${signal.market}</td>

<td>${signal.asset}</td>

<td>${signal.action}</td>

<td>${signal.size}</td>

<td>${signal.who}</td>

<td>${signal.source}</td>

</tr>

`;

});

}

loadData();

setInterval(loadData,10000);
