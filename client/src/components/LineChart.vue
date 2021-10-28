<template>
  <div class="svg-container">
    <svg id="container"/>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'LineChart',
  props: {
    graph_data: {
      required: true,
      type: Object,
    },
    column_list: {
      required: true,
      type: Object,
    },
    date_field_name: {
      default: "date",
      type: String,
    },
    width: {
      default: 600,
      type: Number,
    },
    height: {
      default: 300,
      type: Number,
    }
  },
  watch: {
    graph_data: function () {
      if(this.graph_data && this.column_list) {
        this.retrieveGraph(this.graph_data, this.column_list);
      }
    },
    column_list: function () {
      if(this.graph_data && this.column_list) {
        this.retrieveGraph(this.graph_data, this.column_list);
      }
    }
  },
  data() {
    return {
      padding: 5,
      margin: 5,
      adj: 30
    };
  },
  computed: {
  },
  mounted() {
    if(this.graph_data && this.column_list) {
      this.retrieveGraph(this.graph_data, this.column_list);
    }
  },
  methods: {
    retrieveGraph(data, columns) {
      // Clean the canvas first
      d3.select("svg#container").selectAll("*").remove();
      // Now draw on it
      const svg = d3.select("svg#container")
          .attr("preserveAspectRatio", "xMinYMin meet")
          .attr("viewBox", "-"
                + this.adj + " -"
                + this.adj + " "
                + (this.width + this.adj * 3) + " "
                + (this.height + this.adj * 3))
          .style("padding", this.padding)
          .style("margin", this.margin)
          .classed("svg-content", true);

      //-----------------------------DATA-----------------------------//
      const timeConv = d3.timeParse("%Y-%m-%d");
      const dateName = this.date_field_name;
      var slices = Object.keys(data[0])
        .filter(function(key) { 
          return ((key !== dateName) && (columns.includes(key)));
        })
        .map(function(id) {
          return {
            id: id,
            values: data.map(function(d) {
              return {
                date: timeConv(d[dateName]),
                measurement: +d[id]
              };
            })
          };
        });

      //----------------------------SCALES----------------------------//
      const xScale = d3.scaleTime().range([0,this.width]);
      const yScale = d3.scaleLinear().rangeRound([this.height, 0]);
      xScale.domain(d3.extent(data, function(d){
          return timeConv(d[dateName])}));
      yScale.domain([(0), d3.max(slices, function(c) {
          return d3.max(c.values, function(d) {
              return d.measurement + 4; });
              })
          ]);

      //-----------------------------AXES-----------------------------//
      const yaxis = d3.axisLeft()
          .scale(yScale);

      const xaxis = d3.axisBottom()
          .tickFormat(d3.timeFormat('%b %d'))
          .scale(xScale);

      //----------------------------LINES-----------------------------//
      const line = d3.line()
          .x(function(d) { return xScale(d.date); })
          .y(function(d) { return yScale(d.measurement); }); 

      let id = 0;
      const ids = function () {
          return "line-"+id++;
      }  
      //-------------------------2. DRAWING---------------------------//
      //-----------------------------AXES-----------------------------//
      svg.append("g")
          .attr("class", "axis")
          .attr("transform", "translate(0," + this.height + ")")
          .call(xaxis);

      svg.append("g")
          .attr("class", "axis")
          .call(yaxis)
          .append("text")
          .attr("transform", "rotate(-90)")
          .attr("dy", ".75em")
          .attr("y", 6)
          .style("text-anchor", "end");
          //.text("Frequency");

      //----------------------------LINES-----------------------------//
      const lines = svg.selectAll("lines")
          .data(slices)
          .enter()
          .append("g");

          lines.append("path")
          .attr("class", ids)
          .attr("d", function(d) { return line(d.values); });

          lines.append("text")
          .attr("class","series_label")
          .datum(function(d) {
              return {
                  id: d.id,
                  value: d.values[d.values.length - 1]}; })
          .attr("transform", function(d) {
                  return "translate(" + (xScale(d.value.date) - 10)  
                  + "," + (yScale(d.value.measurement) + 5 ) + ")"; })
          .attr("x", 5)
          .text(function(d) { return d.id; });
    }
  }
};
</script>

<style>
/* AXES */
/* ticks */
.axis line{
stroke: #706f6f;
stroke-width: 0.5;
shape-rendering: crispEdges;
}

/* axis contour */
.axis path {
stroke: #706f6f;
stroke-width: 0.7;
shape-rendering: crispEdges;
}

/* axis text */
.axis text {
fill: #2b2929;
font-family: Georgia;
font-size: 120%;
}

/* LINE CHART */
path.line-0 {
    fill: none;
    stroke: #ed3700;
}

path.line-1 {
    fill: none;
    stroke: #2b2929;
    stroke-dasharray: 2;
}

path.line-2 {
    fill: none;
    stroke: #9c9c9c;
    stroke-dasharray: 6;
}

.series_label {
  fill: #2b2929;
  font-family: Georgia;
  font-size: 80%;
}
</style>