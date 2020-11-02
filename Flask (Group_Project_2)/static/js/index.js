

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// HIGHCHART'S LINE CHART
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Highcharts.getJSON(
  'http://127.0.0.1:5000/api/player_salary',
  function (data) {

    // console.log(data);

    // groupby function
    function groupBy(array, key) {
      return Array.from(
          array.reduce((m, o) => {
              var temp = m.get(o[key]);
              if (!temp) {
                  m.set(o[key], temp = {});
              }
              Object.entries(o).forEach(([k, v]) => {
                  if (k === key) {
                      return;
                  }
                  temp[k] = temp[k]  || { sum: 0, count: 0 };
                  temp[k].sum += v;
                  temp[k].count++;
              });
              return m;
          }, new Map),
          ([k, v]) => Object.assign({ [key]: k }, ...Object.entries(v).map(([l, { sum, count }]) => ({ [l]: +(sum / count).toFixed(1) })))
      );
    };
    // console.log(groupBy(data, 'season_start'));
  
    let grouped_arrays = groupBy(data, 'season_start').sort(function(a,b) {
      return a.season_start - b.season_start
    });
    // console.log(grouped_arrays);
  
    // create series for chart
    let series = [];
    grouped_arrays.forEach(function (p) {
      let post = [
        p.season_start,
        p.salary_$
      ];
      series.push(post);
    });

    // console.log(series);
      
    /////////////////////////////////////////////
    // Chart Boiler plate
    /////////////////////////////////////////////
    Highcharts.chart('container', {
      chart: {
        zoomType: 'x'
      },
      title: {
        text: 'Avg Player Salary 1990-2017'
      },
      subtitle: {
        text: document.ontouchstart === undefined ?
          'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
      },
      xAxis: {
        type: 'Year',
        title: {
          text: 'Year'
        }
      },
      yAxis: {
        title: {
          text: 'Yearly Salary'
        }
      },
      legend: {
        enabled: false
      },
      plotOptions: {
        area: {
          fillColor: {
            linearGradient: {
              x1: 0,
              y1: 0,
              x2: 0,
              y2: 1
            },
            stops: [
              [0, Highcharts.getOptions().colors[0]],
              [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
          },
          marker: {
            radius: 2
          },
          lineWidth: 1,
          states: {
            hover: {
              lineWidth: 1
            }
          },
          threshold: null
        }
      },
      series: [{
        type: 'area',
        name: 'Average Salary',
        data: series
      }]
    });
  }
);

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Highcharts USA map with WS
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Highcharts.getJSON('http://127.0.0.1:5000/api/states_winshare', function (data) {
  console.log(data)
  // Instantiate the map
  Highcharts.mapChart('heatmap', {
    chart: {
      map: 'countries/us/us-all',
      borderWidth: 3,
      borderColor: '#23aa8f'
    },
    title: {
      text: 'Total Career Win Shares by US State (1976-2020)'
    },
    exporting: {
      sourceWidth: 600,
      sourceHeight: 500
    },
    legend: {
      layout: 'horizontal',
      borderWidth: 0,
      backgroundColor: 'rgba(255,255,255,0.85)',
      floating: true,
      verticalAlign: 'top',
      y: 25
    },
    mapNavigation: {
      enabled: true
    },
    colorAxis: {
          min: 1,
          max: 5000,
          type: 'logarithmic',
          minColor: '#fafa6e',
          maxColor: '#2a4858',
          stops: [
            [0, '#fafa6e'],
            [0.25, '#86d780'],
            [0.50, '#23aa8f'],
            [0.75, '#007882'],
            [1, '#2a4858']
          ]
        },
    series: [{
      animation: {
        duration: 1000
      },
      data: data,
      joinBy: ['postal-code', 'code'],
      states: {
          hover: {
          borderColor: '#303030',
          borderWidth: 4
              }
          },
      dataLabels: {
        enabled: true,
        color: '#FFFFFF',
        format: '{point.code}'
      },
      name: 'Win Shares',
      tooltip: {
        pointFormat: '{point.code}: {point.value}'
      }
    }]
  });
});