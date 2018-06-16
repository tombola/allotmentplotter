$allotment = d3.select("#allotment");
  plantingRow = [ 2, 6, 8, 4, 6, 8, 3, 4]
  plotWidth = 500;
  plotHeight = 400;
  plantingDistance = 30;
  rowDistance = 40;

  var $plot = $allotment.append('svg')
    .attr('width', plotWidth)
    .attr('height', plotHeight)

  $plants = $plot.selectAll('circle')
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

  // TODO: Create guides based on array
  // TODO: Use plot data for array
  var drawGuides = function($plot, guideArray) {
    var $guides = $plot.append("path")
      .attr("d", rowGuideLine('vertical', 200))
      .attr("class", "row-guide")
  }

  drawGuides($plot, [])