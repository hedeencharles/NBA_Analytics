//////////////////////////////////////////////////////////////////////////////////////////
// Functions/Visualizations
//////////////////////////////////////////////////////////////////////////////////////////
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





// Highcharts.getJSON('http://127.0.0.1:5000/api/ws_birthplace', function (data) {
//
// // Make codes uppercase to match the map data
// data.forEach(function (p) {
//
//   p.code = p.code;
// });
//
//   // Instantiate the map
//   Highcharts.mapChart('heatmap', {
//
//     chart: {
//       map: 'countries/us/us-all',
//       borderWidth: 1
//     },
//
//     title: {
//       text: 'Total Career Win Shares by US State (1976-2020)'
//     },
//
//     exporting: {
//       sourceWidth: 600,
//       sourceHeight: 500
//     },
//
//     legend: {
//       layout: 'horizontal',
//       borderWidth: 0,
//       backgroundColor: 'rgba(255,255,255,0.85)',
//       floating: true,
//       verticalAlign: 'top',
//       y: 25
//     },
//
//     mapNavigation: {
//       enabled: true
//     },
//
//     colorAxis: {
//       min: 1,
//       max: 5000,
//       type: 'logarithmic',
//       minColor: '#fafa6e',
//       maxColor: '#2a4858',
//       stops: [
//         [0, '#fafa6e'],
//         [0.25, '#86d780'],
//         [0.50, '#23aa8f'],
//         [0.75, '#007882'],
//         [1, '#2a4858']
//       ]
//     },
//
//     series: [{
//       animation: {
//         duration: 1000
//       },
//       data: data,
//       colorAxis: 1,
//       nullColor: 'red',
//       joinBy: ['name', 'birthplace'],
//       states: {
//           hover: {
//               color: '#86d780',
//               borderColor: '#303030',
//               borderWidth: 3
//                           }
//                       },
//       dataLabels: {
//         enabled: true,
//         color: '#FFFFFF',
//         format: '{point.birthplace}'
//       },
//       name: 'Win Shares',
//       tooltip: {
//         pointFormat: '{point.birthplace}: {point.win_shares}'
//       }
//     }]
//   });
// });
