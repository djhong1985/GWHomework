// @TODO: YOUR CODE HERE!
var svgWidth = 830;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart,
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Load data
d3.csv("./assets/data/data.csv").then(function(healthData) {
  console.log(healthData);
  
  // Step 1: Parse Data/Cast as numbers
  healthData.forEach(function(data) {
    healthData.healthcare = +healthData.healthcare;
    healthData.poverty = +healthData.poverty;
  });

  // Step 2: Create scale functions
  var xLinearScale = d3.scaleLinear()
    .domain([8, d3.max(healthData, function(d){return +d.poverty;})])
    .range([0, width]);
    

  var yLinearScale = d3.scaleLinear()
    // .domain([0, d3.max(healthData, d => d.healthcare)])
    .domain([0, d3.max(healthData, function(d){return +d.healthcare;})])
    .range([height, 0]);

  // Step 3: Create axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Step 4: Append Axes to the chart
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  chartGroup.append("g")
    .call(leftAxis);

  // Step 5: Create Circles
  var circlesGroup = chartGroup.selectAll("circle")
    .data(healthData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "15")
    .attr("fill", "black")
    .attr("opacity", ".5");

  // Step 6: Add State Abbrv
    var textGroup = chartGroup.selectAll("text")
    .data(healthData)
    .enter()
    .append("text")
    .attr("x", d => xLinearScale(d.poverty))
    .attr("y", d => yLinearScale(d.healthcare))
    .attr("fill", "blue")
    .attr("opacity", ".5")
    .attr("dy", function(data, index){return 5;})
    .attr("text-anchor", "middle")
    .text(function(data, index){return data.abbr;})
    .attr("font-size", 12)
    .attr('fill', 'white');

  // Step 6: Initialize tool tip
  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${d.state}<br>Poverty: ${d.poverty}<br>Healthcare: ${d.healthcare}`);
      });

  // Step 7: Create tooltip in the chart
  chartGroup.call(toolTip);

  // Step 8: Create event listeners to display and hide the tooltip
  circlesGroup.on("click", function(data) {
    toolTip.show(data, this);
  })
  // onmouseout event
  .on("mouseout", function(data, index) {
    toolTip.hide(data);
  });

  // Create axes labels
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 0)
    .attr("x", 0 - (height / 2))
    .attr("text-anchor", "middle")
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Lacks Healthcare (%)");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .attr("text-anchor", "middle")
    .text("In Poverty (%)");
  });


  