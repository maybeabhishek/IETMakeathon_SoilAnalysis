
$(document).ready(function () {
  // Create the chart
  $('#chart_id_humidity').highcharts({
    chart: {
      events: {
        load: function () {

          // set up the updating of the chart each second
          var series = this.series[0];
          setInterval(function () {
            series.addPoint(humidityData, true, true);
          }, 1000);
        }
      }
    },

    time: {
      useUTC: false
    },

    title: {
      text: 'Humidity Data'
    },

    exporting: {
      enabled: false
    },

    series: [{
      name: '% % humidity',
      data: (function () {
        // generate an array of random data
        var data = [];
        for (i = -100; i <= 0; i += 1) {
          data.push(Math.floor(Math.random() * 40 + 10));
        }
        return data;
      }())
    }]
  });

});