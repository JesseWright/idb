    var baseUrl = "https://crossorigin.me/http://itslaunchti.me/api/"

var childTypes = {
  "agencies": "missions",
  "missions": "launches",
  "launches" : "locations"
};
var idSwap = {
  "agencies" : "agencies",
  "missions" : "missions",
  "launches" : "launch_id",
  "locations" : "location_id"
}

// Maps from id to names for each data type.
var maps = {};

// Holds callback data that depends on the data in maps which may not be loaded.
var deferred = {
  "agencies": [],
  "missions" : [],
  "launches": [],
  "locations": []
};

// Retry on failed requests.
function spamRequest(url, callback) {
  d3.json(url, function(error, data) {
    if(!data) {
      spamRequest(url, callback);
    } else {
      callback(data);
    }
  })
}

function makeUrl(type, id) {
  return baseUrl + type + "?id=" + id;
}

spamRequest(baseUrl + "agencies", function(data) {
  console.log("bleh");
  var treeData =
  {
    "name": "Agencies",
    "children": [],
    "loaded": true,
    "image" : ""
  };
  
 for (var i = 0; i < data.length; i += 5){
    var d = data[i];
    treeData.children.push({
      "name": d.abbrev,
      "url": makeUrl("agencies", d.id),
      "type": "agencies",
      "loaded" : false,
      "image" : ""
    });
  }
  
  drawTree(treeData);
});

function loadMap(type) {
  spamRequest(baseUrl + type, function(data) {
    var map = {};

    for (var i = 0; i < data.length; i++) {
      var d = data[i];
      map[d.id] = d.name;
    }
    maps[type] = map;
    for (var i = 0; i < deferred[type].length; i++) {
      deferred[type][i]();
    }
  });
}
loadMap("missions");
loadMap("launches");
loadMap("locations");

function drawTree(treeData) {
  console.log(treeData);
  // Set the dimensions and margins of the diagram
  var margin = {top: 20, right: 90, bottom: 30, left: 90},
      width = 960 - margin.left - margin.right,
      height = 900 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  // appends a 'group' element to 'svg'
  // moves the 'group' element to the top left margin
  var svg = d3.select("#content").append("svg")
      .attr("width", width + margin.right + margin.left)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate("
            + margin.left + "," + margin.top + ")");
  console.log("thing");
  var i = 0,
      duration = 750,
      root;

  // declares a tree layout and assigns the size
  var treemap = d3.tree().size([height, width]);

  // Assigns parent, children, height, depth
  root = d3.hierarchy(treeData, function(d) { return d.children; });
  root.x0 = height / 2;
  root.y0 = 0;

  // Collapse after the second level
  root.children.forEach(collapse);

  update(root);

  // Collapse the node and all it's children
  function collapse(d) {
    if(d.children) {
      d._children = d.children
      d._children.forEach(collapse)
      d.children = null
    }
  }

  function update(source) {

    // Assigns the x and y position for the nodes
    var treeData = treemap(root);

    // Compute the new tree layout.
    var nodes = treeData.descendants(),
        links = treeData.descendants().slice(1);

    // Normalize for fixed-depth.
    nodes.forEach(function(d){ d.y = d.depth * 250});

    // ****************** Nodes section ***************************

    // Update the nodes...
    var node = svg.selectAll('g.node')
        .data(nodes, function(d) {return d.id || (d.id = ++i); });

    // Enter any new modes at the parent's previous position.
    var nodeEnter = node.enter().append('g')
        .attr('class', 'node')
        .attr("transform", function(d) {
          return "translate(" + source.y0 + "," + source.x0 + ")";
      })
      .on('click', click);

    // Add Circle for the nodes
    nodeEnter.append('circle')
        .attr('class', 'node')
        .attr('r', 1e-6)
        .style("fill", function(d) {
            return d._children ? "lightsteelblue" : "#fff";
        });

    // Add labels for the nodes
    nodeEnter.append('text')
        .attr("dy", ".35em")
        .attr("x", function(d) {
            return d.children || d._children ? -13 : 13;
        })
        .attr("text-anchor", function(d) {
            return d.children || d._children ? "end" : "start";
        })
        .text(function(d) { return d.data.name; });

    // UPDATE
    var nodeUpdate = nodeEnter.merge(node);

    // Transition to the proper position for the node
    nodeUpdate.transition()
      .duration(duration)
      .attr("transform", function(d) { 
          return "translate(" + d.y + "," + d.x + ")";
       });

    // Update the node attributes and style
    nodeUpdate.select('circle.node')
      .attr('r', 10)
      .style("fill", function(d) {

          return d._children ? "lightsteelblue" : "#fff";
      })
      .attr('cursor', 'pointer');


    // Remove any exiting nodes
    var nodeExit = node.exit().transition()
        .duration(duration)
        .attr("transform", function(d) {
            return "translate(" + source.y + "," + source.x + ")";
        })
        .remove();

    // On exit reduce the node circles size to 0
    nodeExit.select('circle')
      .attr('r', 1e-6);

    // On exit reduce the opacity of text labels
    nodeExit.select('text')
      .style('fill-opacity', 1e-6);

    // ****************** links section ***************************

    // Update the links...
    var link = svg.selectAll('path.link')
        .data(links, function(d) { return d.id; });

    // Enter any new links at the parent's previous position.
    var linkEnter = link.enter().insert('path', "g")
        .attr("class", "link")
        .attr('d', function(d){
          var o = {x: source.x0, y: source.y0}
          return diagonal(o, o)
        });

    // UPDATE
    var linkUpdate = linkEnter.merge(link);

    // Transition back to the parent element position
    linkUpdate.transition()
        .duration(duration)
        .attr('d', function(d){ return diagonal(d, d.parent) });

    // Remove any exiting links
    var linkExit = link.exit().transition()
        .duration(duration)
        .attr('d', function(d) {
          var o = {x: source.x, y: source.y}
          return diagonal(o, o)
        })
        .remove();

    // Store the old positions for transition.
    nodes.forEach(function(d){
      d.x0 = d.x;
      d.y0 = d.y;
    });

    // Creates a curved (diagonal) path from parent to the child nodes
    function diagonal(s, d) {

      path = `M ${s.y} ${s.x}
              C ${(s.y + d.y) / 2} ${s.x},
                ${(s.y + d.y) / 2} ${d.x},
                ${d.y} ${d.x}`

      return path
    }

    // Toggle children on click.
    function toggle(d) {
      if (d.children) {
          d._children = d.children;
          d.children = null;
        } else {
          d.children = d._children;
          d._children = null;
        }
      update(d);
    }

    function populateChildren(childType, childIds, depth, parent) {
      if(!childIds || !childIds.length) {
        console.log(childIds);
        return undefined;
      }
      var children = [];
      for(var i = 0; i < childIds.length && i < 50; i++) {
        var id = childIds[i];
        var obj = d3.hierarchy({
          "name": maps[childType][id],
          "url": makeUrl(childType, id),
          "type": childType,
          "loaded" : false,
          "image" : ""
        });
        obj.depth = depth;
        obj.parent = parent;
        children.push(obj);
      }
      return children;
    }

    function flatten(map) {
      var list = [];
      for(var key in map) {
        if(map.hasOwnProperty(key)) {
          list.push(key);
        }
      }
      return list;
    }
    // Toggle children on click.
    function click(d) {
      if (d.data.loaded) {
        toggle(d);
      } else {
        var childType = childTypes[d.data.type];
        var callback = function() {
          spamRequest(d.data.url, function(data) {
            data = data[0];
            if(childType) {
              var temp = data[idSwap[childType]];
              if(typeof(temp) == "number") {
                temp = [temp];
              } else {
                temp = flatten(temp);
              }
              d.children = populateChildren(childType, temp, d.depth + 1, d);
            }
            d.data.loaded = true;
            update(d);
          });
        };

        if (maps[childType]) {
          callback();
        } else {
          deferred[childType].push(callback);
        }
      }
    }
  }
}