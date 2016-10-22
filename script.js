
//Updates table
function createTable() {

	var request = new XMLHttpRequest();
    request.open('GET', 'service.php', false);
    request.send();

    if (request.status != 200) {
      	 alert("Ajax went wrong");
    }

	//Build array from the jsonObject
	var customers = new Array();
	var jsonArr = JSON.parse(request.responseText);
	//var jsonArr = jsonObject['log'];
	for(var i in jsonArr){
		customers.push((jsonArr[i]['date']) );
		customers.push((jsonArr[i]['time']) );
		customers.push((jsonArr[i]['temp']) );
		customers.push((jsonArr[i]['humidity']));
	}

	//Remove existing tables.
	var myNode = document.getElementById('logDiv');
	while (myNode.hasChildNodes()) {
  	   		myNode.removeChild(myNode.firstChild);
	}

	var container = document.getElementById('logDiv');
	var table = document.createElement('table');
	var tbody = document.createElement('tbody');
	table.className = "sortable";

	//Adds table headers
	var headers = ["Hum", "Temp", "Time", "Date"]
    var hrow = document.createElement('tr');
	for (var b = 0; b < 4; b++) {
        var cell = document.createElement('th');
        cell.textContent = headers[b];
        hrow.appendChild(cell);
		counter++;
    }
    tbody.appendChild(hrow);

	var counter = customers.length-1;
	// loop and create rows
	for (i = 0; i < customers.length/4; i++) {
		var values = customers[i];
		var row = document.createElement('tr');
		
		// loop and create columns
		for (var b = 0; b < 4; b++) {
			var cell = document.createElement('td');
			cell.textContent = customers[counter];
			row.appendChild(cell);
			counter--;
		}
		tbody.appendChild(row);
	}
	table.appendChild(tbody);
	container.appendChild(table);
}
	
