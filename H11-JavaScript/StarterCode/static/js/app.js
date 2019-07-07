// from data.js
var tableData = data;
var tbody = d3.select("tbody");

console.log(tableData);

data.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
  
  //write JavaScript code that will listen for events and
  //search through the date/time column to find rows that match user input.

var submit = d3.select("#filter-btn");

submit.on("click", function() {
  
    // Prevent the page from refreshing
    d3.event.preventDefault();
  
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
  
    console.log(inputValue);
      
    var filteredData = tableData.filter(date => date.datetime === inputValue);
  
    console.log(filteredData);

    tbody.html("");
 
    filteredData.forEach((incident) => {
        var row = tbody.append("tr");
        Object.entries(incident).forEach(([key, value]) => {
          var cell = row.append("td");
          cell.text(value);
        });
    });
});