var $allotment = d3.select("#allotment");

var plantingRow = [ 2, 6, 8, 4, 6, 8, 3, 4]
var plotWidth = 500;
var plotHeight = 400;
var plantingDistance = 30;
var rowDistance = 40;
var guides = [
  {align:'vertical', position:100},
  {align:'vertical', position:240},
  {align:'vertical', position:40},
  {align:'horizontal', position:100},
  {align:'horizontal', position:300},
]

var $bed = $allotment.append('svg')
  .attr('width', plotWidth)
  .attr('height', plotHeight)
  .attr("class", "bed")

$plants = $bed.selectAll('circle')
  .data(plantingRow)
  .enter()
  .append('circle')
  .attr("fill", 'none')
  .attr("stroke", '#000')
  .attr("class", "plant")

$plants.attr('cy', function(d, i) {
      return ((i + 1) * plantingDistance);
  })
 .attr('cx', rowDistance)
 .attr("r", function(d) {
      return d;
 });

var rowGuideLine = function(align, position) {
  var lineFunction = d3.line()
    .x(function(d) { return d.x; })
    .y(function(d) { return d.y; })
    .curve(d3.curveLinear);

  if (align == 'vertical') {
    var guideData = [
      { x: position, y: 0},
      { x: position, y: 1000},
    ];
  }
  else if (align == 'horizontal') {
    var guideData = [
      { x: 0, y: position},
      { x: 1000, y: position},
    ];
  }
  return lineFunction(guideData)
}

// Take the array of guides and draw paths on  
var plotGuides = $bed.selectAll('.row-guide')
  .data(guides)
  .enter()
  .append("path")
  .attr("d", function(d,i) { return rowGuideLine(d.align, d.position)})
  .attr("class", "row-guide")

