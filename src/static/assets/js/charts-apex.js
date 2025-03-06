


(function () {
  let cardColor, headingColor, labelColor, borderColor, legendColor;

  if (isDarkStyle) {
      cardColor = config.colors_dark.cardColor;
      headingColor = config.colors_dark.headingColor;
      labelColor = config.colors_dark.textMuted;
      legendColor = config.colors_dark.bodyColor;
      borderColor = config.colors_dark.borderColor;
  } else {
      cardColor = config.colors.cardColor;
      headingColor = config.colors.headingColor;
      labelColor = config.colors.textMuted;
      legendColor = config.colors.bodyColor;
      borderColor = config.colors.borderColor;
  }

  const chartColors2 = {
      column: {
          series1: '#3f51b5', // Temperature
          series2: '#00bcd4', // Humidity
          series3: '#ff5722', // Door
          series4: '#4caf50', // Flood
          series5: '#9c27b0', // PIR
          series6: '#ffc107', // Gas
          bg: '#e3f2fd' // Light Blue Background
      }
  };

  // Function to fetch data and render the chart for sub-admin
  function fetchDataAndRenderChart2(timeFilter) {
      const barChartsubEl = document.getElementById('barChartsub');
      if (!barChartsubEl) {
          console.error("Element with ID 'barChartsub' not found");
          return;
      }

      // Set loading state
      barChartsubEl.innerHTML = '<p>Loading...</p>';

      fetch(`/all_rooms_alertssub/?time_filter=${timeFilter}`)
          .then(response => response.json())
          .then(data => {
              console.log("Fetched data for barChartsub:", data); // Debug data

              const roomNames = data.map(room => room.name);
              const temperatureData = data.map(room => room.temperature_alerts);
              const humidityData = data.map(room => room.humidity_alerts);
              const doorData = data.map(room => room.door_alerts);
              const floodData = data.map(room => room.flood_alerts);
              const pirData = data.map(room => room.pir_alerts);
              const gasData = data.map(room => room.gas_alerts);

              const barChartConfig2 = {
                  chart: {
                      height: 400,
                      type: 'bar',
                      stacked: true,
                      parentHeightOffset: 0,
                      toolbar: {
                          show: false
                      },
                      animations: {
                          enabled: true,
                          easing: 'easeinout',
                          speed: 800
                      }
                  },
                  plotOptions: {
                      bar: {
                          columnWidth: '15%',
                          colors: {
                              backgroundBarColors: Array(6).fill(chartColors2.column.bg),
                              backgroundBarRadius: 10
                          }
                      }
                  },
                  dataLabels: {
                      enabled: false
                  },
                  legend: {
                      show: true,
                      position: 'top',
                      horizontalAlign: 'start',
                      labels: {
                          colors: legendColor,
                          useSeriesColors: false
                      }
                  },
                  colors: Object.values(chartColors2.column).slice(0, 6),
                  stroke: {
                      show: true,
                      colors: ['transparent']
                  },
                  grid: {
                      borderColor: borderColor
                  },
                  series: [
                      { name: 'Temperature Alerts', data: temperatureData },
                      { name: 'Humidity Alerts', data: humidityData },
                      { name: 'Door Alerts', data: doorData },
                      { name: 'Flood Alerts', data: floodData },
                      { name: 'PIR Alerts', data: pirData },
                      { name: 'Gas Alerts', data: gasData }
                  ],
                  xaxis: {
                      categories: roomNames,
                      labels: {
                          style: {
                              colors: labelColor,
                              fontSize: '12px'
                          }
                      }
                  },
                  yaxis: {
                      labels: {
                          style: {
                              colors: labelColor,
                              fontSize: '12px'
                          }
                      }
                  },
                  tooltip: {
                      y: {
                          formatter: function (val) {
                              return val + ' alerts';
                          }
                      }
                  }
              };

              // Destroy previous chart to avoid conflicts
              barChartsubEl.innerHTML = '';
              const barChart = new ApexCharts(barChartsubEl, barChartConfig2);
              barChart.render();
          })
          .catch(error => {
              console.error("Error fetching data for barChartsub:", error);
              barChartsubEl.innerHTML = '<p>Error loading data</p>';
          });
  }

  // Event listener for time filter
  document.getElementById('timeFilterSelect').addEventListener('change', function () {
      const selectedTimeFilter = this.value;
      document.getElementById('selectedTimeFilter').innerText = selectedTimeFilter.replace('h', ' hours').replace('min', ' minutes');
      fetchDataAndRenderChart2(selectedTimeFilter);
  });

  // Initial fetch
  fetchDataAndRenderChart2('24h');

  // // Debugging: Test a simple chart to check if barChartsub renders
  // const barChartsubEl = document.getElementById('barChartsub');
  // if (barChartsubEl) {
  //     const testChart = new ApexCharts(barChartsubEl, {
  //         chart: { type: 'bar', height: 400 },
  //         series: [{ name: 'Test Series', data: [10, 20, 30] }],
  //         xaxis: { categories: ['A', 'B', 'C'] }
  //     });
  //     testChart.render();
  // }

})();

(function () {
  // Set default color values based on theme
  let cardColor, headingColor, labelColor, borderColor, legendColor;

  if (isDarkStyle) {
      cardColor = config.colors_dark.cardColor;
      headingColor = config.colors_dark.headingColor;
      labelColor = config.colors_dark.textMuted;
      legendColor = config.colors_dark.bodyColor;
      borderColor = config.colors_dark.borderColor;
  } else {
      cardColor = config.colors.cardColor;
      headingColor = config.colors.headingColor;
      labelColor = config.colors.textMuted;
      legendColor = config.colors.bodyColor;
      borderColor = config.colors.borderColor;
  }

  const chartColors1 = {
      column: {
          series1: '#3f51b5', // Temperature
          series2: '#00bcd4', // Humidity
          series3: '#ff5722', // Door
          series4: '#4caf50', // Flood
          series5: '#9c27b0', // PIR
          series6: '#ffc107', // Gas
          bg: '#e3f2fd' // Light Blue Background
      }
  };

  // Function to fetch data and render the chart
  function fetchDataAndRenderChart1(timeFilter) {
      // Set loading state
      document.getElementById('barChart').innerHTML = '<p>Loading...</p>';

      fetch(`/all_rooms_alerts/?time_filter=${timeFilter}`)
          .then(response => response.json())
          .then(data => {
              const roomNames = data.map(room => room.name);
              const temperatureData = data.map(room => room.temperature_alerts);
              const humidityData = data.map(room => room.humidity_alerts);
              const doorData = data.map(room => room.door_alerts);
              const floodData = data.map(room => room.flood_alerts);
              const pirData = data.map(room => room.pir_alerts);
              const gasData = data.map(room => room.gas_alerts);

              const barChartEl = document.querySelector('#barChart');
              const barChartConfig1 = {
                  chart: {
                      height: 400,
                      type: 'bar',
                      stacked: true,
                      parentHeightOffset: 0,
                      toolbar: {
                          show: false
                      },
                      animations: {
                          enabled: true,
                          easing: 'easeinout',
                          speed: 800
                      }
                  },
                  plotOptions: {
                      bar: {
                          columnWidth: '15%',
                          colors: {
                              backgroundBarColors: Array(6).fill(chartColors1.column.bg),
                              backgroundBarRadius: 10
                          }
                      }
                  },
                  dataLabels: {
                      enabled: false
                  },
                  legend: {
                      show: true,
                      position: 'top',
                      horizontalAlign: 'start',
                      labels: {
                          colors: legendColor,
                          useSeriesColors: false
                      }
                  },
                  colors: Object.values(chartColors1.column).slice(0, 6),
                  stroke: {
                      show: true,
                      colors: ['transparent']
                  },
                  grid: {
                      borderColor: borderColor
                  },
                  series: [
                      { name: 'Temperature Alerts', data: temperatureData },
                      { name: 'Humidity Alerts', data: humidityData },
                      { name: 'Door Alerts', data: doorData },
                      { name: 'Flood Alerts', data: floodData },
                      { name: 'PIR Alerts', data: pirData },
                      { name: 'Gas Alerts', data: gasData }
                  ],
                  xaxis: {
                      categories: roomNames,
                      labels: {
                          style: {
                              colors: labelColor,
                              fontSize: '12px'
                          }
                      }
                  },
                  yaxis: {
                      labels: {
                          style: {
                              colors: labelColor,
                              fontSize: '12px'
                          }
                      }
                  },
                  tooltip: {
                      y: {
                          formatter: function (val) {
                              return val + ' alerts';
                          }
                      }
                  }
              };

              // Destroy previous chart to avoid conflicts
              if (barChartEl) {
                  barChartEl.innerHTML = '';
                  const barChart = new ApexCharts(barChartEl, barChartConfig1);
                  barChart.render();
              }
          })
          .catch(error => {
              document.getElementById('barChart').innerHTML = '<p>Error loading data</p>';
          });
  }

  // Event listener for time filter dropdown
  document.getElementById('timeFilterSelect').addEventListener('change', function () {
      const selectedTimeFilter = this.value;
      document.getElementById('selectedTimeFilter').innerText = selectedTimeFilter.replace('h', ' hours').replace('min', ' minutes');
      fetchDataAndRenderChart1(selectedTimeFilter);
  });

  // Initial fetch
  fetchDataAndRenderChart1('24h');
})();



// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




// (function () {
//   let cardColor, headingColor, labelColor, borderColor, legendColor;

//   if (isDarkStyle) {
//       cardColor = config.colors_dark.cardColor;
//       headingColor = config.colors_dark.headingColor;
//       labelColor = config.colors_dark.textMuted;
//       legendColor = config.colors_dark.bodyColor;
//       borderColor = config.colors_dark.borderColor;
//   } else {
//       cardColor = config.colors.cardColor;
//       headingColor = config.colors.headingColor;
//       labelColor = config.colors.textMuted;
//       legendColor = config.colors.bodyColor;
//       borderColor = config.colors.borderColor;
//   }

//   const chartColors2 = {
//       column: {
//           series1: '#3f51b5', // Temperature
//           series2: '#00bcd4', // Humidity
//           series3: '#ff5722', // Door
//           series4: '#4caf50', // Flood
//           series5: '#9c27b0', // PIR
//           series6: '#ffc107', // Gas
//           bg: '#e3f2fd' // Light Blue Background
//       }
//   };

//   // Function to fetch data and render the chart for sub-admin
//   function fetchDataAndRenderChart2(timeFilter) {
//       document.getElementById('barChartsub').innerHTML = '<p>Loading...</p>';

//       fetch(`/all_rooms_alertssub/?time_filter=${timeFilter}`)
//           .then(response => response.json())
//           .then(data => {
//               const roomNames = data.map(room => room.name);
//               const temperatureData = data.map(room => room.temperature_alerts);
//               const humidityData = data.map(room => room.humidity_alerts);
//               const doorData = data.map(room => room.door_alerts);
//               const floodData = data.map(room => room.flood_alerts);
//               const pirData = data.map(room => room.pir_alerts);
//               const gasData = data.map(room => room.gas_alerts);

//               const barChartEl = document.querySelector('#barChartsub');
//               const barChartConfig2 = {
//                   chart: {
//                       height: 400,
//                       type: 'bar',
//                       stacked: true,
//                       parentHeightOffset: 0,
//                       toolbar: {
//                           show: false
//                       },
//                       animations: {
//                           enabled: true,
//                           easing: 'easeinout',
//                           speed: 800
//                       }
//                   },
//                   plotOptions: {
//                       bar: {
//                           columnWidth: '15%',
//                           colors: {
//                               backgroundBarColors: Array(6).fill(chartColors2.column.bg),
//                               backgroundBarRadius: 10
//                           }
//                       }
//                   },
//                   dataLabels: {
//                       enabled: false
//                   },
//                   legend: {
//                       show: true,
//                       position: 'top',
//                       horizontalAlign: 'start',
//                       labels: {
//                           colors: legendColor,
//                           useSeriesColors: false
//                       }
//                   },
//                   colors: Object.values(chartColors2.column).slice(0, 6),
//                   stroke: {
//                       show: true,
//                       colors: ['transparent']
//                   },
//                   grid: {
//                       borderColor: borderColor
//                   },
//                   series: [
//                       { name: 'Temperature Alerts', data: temperatureData },
//                       { name: 'Humidity Alerts', data: humidityData },
//                       { name: 'Door Alerts', data: doorData },
//                       { name: 'Flood Alerts', data: floodData },
//                       { name: 'PIR Alerts', data: pirData },
//                       { name: 'Gas Alerts', data: gasData }
//                   ],
//                   xaxis: {
//                       categories: roomNames,
//                       labels: {
//                           style: {
//                               colors: labelColor,
//                               fontSize: '12px'
//                           }
//                       }
//                   },
//                   yaxis: {
//                       labels: {
//                           style: {
//                               colors: labelColor,
//                               fontSize: '12px'
//                           }
//                       }
//                   },
//                   tooltip: {
//                       y: {
//                           formatter: function (val) {
//                               return val + ' alerts';
//                           }
//                       }
//                   }
//               };

//               if (barChartEl) {
//                   barChartEl.innerHTML = '';
//                   const barChart = new ApexCharts(barChartEl, barChartConfig2);
//                   barChart.render();
//               }
//           })
//           .catch(error => {
//               document.getElementById('barChartsub').innerHTML = '<p>Error loading data</p>';
//           });
//   }

//   // Event listener for time filter
//   document.getElementById('timeFilterSelect').addEventListener('change', function () {
//       const selectedTimeFilter = this.value;
//       document.getElementById('selectedTimeFilter').innerText = selectedTimeFilter.replace('h', ' hours').replace('min', ' minutes');
//       fetchDataAndRenderChart2(selectedTimeFilter);
//   });

//   // Initial fetch
//   fetchDataAndRenderChart2('24h');
// })();
























/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







// line chart code for dashboard humidity and temperature displaying 


// (function () {
//   let cardColor, headingColor, labelColor, borderColor, legendColor;

//   if (isDarkStyle) {
//     cardColor = config.colors_dark.cardColor;
//     headingColor = config.colors_dark.headingColor;
//     labelColor = config.colors_dark.textMuted;
//     legendColor = config.colors_dark.bodyColor;
//     borderColor = config.colors_dark.borderColor;
//   } else {
//     cardColor = config.colors.cardColor;
//     headingColor = config.colors.headingColor;
//     labelColor = config.colors.textMuted;
//     legendColor = config.colors.bodyColor;
//     borderColor = config.colors.borderColor;
//   }

//   // Fetch data from the server for the last hour
//   fetch('/fetch_room_data_tem/')
//     .then(response => response.json())
//     .then(data => {
//       let seriesData = [];
//       let categories = [];

//       data.room_data.forEach((room) => {
//         seriesData.push({
//           name: `${room.room_name} Temperature`,
//           data: room.temperature
//         });
//         seriesData.push({
//           name: `${room.room_name} Humidity`,
//           data: room.humidity
//         });

//         // Use timestamps from one room as the categories
//         if (!categories.length) {
//           categories = room.timestamps;
//         }
//       });

//       // Line chart configuration
//       const lineChartAl = document.querySelector('#lineChartCompAlert'),
//         lineChartCompConfigAlert = {
//           series: seriesData,
//           chart: {
//             height: 400,
//             type: 'line',
//             parentHeightOffset: 0,
//             zoom: {
//               enabled: false
//             },
//             toolbar: {
//               show: false
//             }
//           },
//           markers: {        
//             strokeWidth: 1,
//             strokeOpacity: 1,
//             strokeColors: [cardColor],
//             colors: [config.colors.warning]
//           },
//           dataLabels: {
//             enabled: false
//           },
//           stroke: {
//             curve: 'straight',
//             width: [2, 2]
//           },
//           colors: [config.colors.warning, config.colors.success, '#00cfe8'],
//           grid: {
//             borderColor: borderColor,
//             xaxis: {
//               lines: {
//                 show: true
//               }
//             },
//             padding: {
//               top: -20
//             }
//           },
//           tooltip: {
//             custom: function ({ series, seriesIndex, dataPointIndex, w }) {
//               return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '</span>' + '</div>';
//             }
//           },
//           xaxis: {      
//             categories: categories,
//             title: {
//               text: 'Time'
//             },
//             axisBorder: {
//               show: true
//             },
//             axisTicks: {
//               show: true
//             },        
//             labels: {
//               style: {
//                 colors: labelColor,
//                 fontSize: '13px'
//               }
//             }
//           },
//           yaxis: {
//             labels: {
//               style: {
//                 colors: labelColor,
//                 fontSize: '13px'
//               }
//             },
//             title: {
//               text: "Values",
//               style: {
//                 color: labelColor,
//                 fontSize: '13px'
//               }
//             }        
//           }
//         };

//       if (typeof lineChartAl !== undefined && lineChartAl !== null) {
//         const lineChartCompAlert = new ApexCharts(lineChartAl, lineChartCompConfigAlert);
//         lineChartCompAlert.render();
//       }
//     })
//     .catch(error => console.error('Error fetching room data:', error));
// })();





(function () {
  let cardColor, headingColor, labelColor, borderColor, legendColor;
  let lineChartCompAlert; // Declare the chart instance outside

  // Set colors based on the theme
  if (isDarkStyle) {
    cardColor = config.colors_dark.cardColor;
    headingColor = config.colors_dark.headingColor;
    labelColor = config.colors_dark.textMuted;
    legendColor = config.colors_dark.bodyColor;
    borderColor = config.colors_dark.borderColor;
  } else {
    cardColor = config.colors.cardColor;
    headingColor = config.colors.headingColor;
    labelColor = config.colors.textMuted;
    legendColor = config.colors.bodyColor;
    borderColor = config.colors.borderColor;
  }

  // Function to fetch data and update the chart
  function fetchDataAndUpdateChart() {
    fetch('/fetch_room_data_tem/')
      .then(response => response.json())
      .then(data => {
        let seriesData = [];
        let categories = [];

        data.room_data.forEach((room) => {
          seriesData.push({
            name: `${room.room_name} Temperature`,
            data: room.temperature
          });
          seriesData.push({
            name: `${room.room_name} Humidity`,
            data: room.humidity
          });

          // Use timestamps from one room as the categories
          if (!categories.length) {
            categories = room.timestamps;
          }
        });

        // Update the chart configuration
        const lineChartAl = document.querySelector('#lineChartCompAlert');
        const lineChartCompConfigAlert = {
          series: seriesData,
          chart: {
            height: 400,
            type: 'line',
            parentHeightOffset: 0,
            zoom: {
              enabled: false
            },
            toolbar: {
              show: false
            }
          },
          markers: {
            strokeWidth: 1,
            strokeOpacity: 1,
            strokeColors: [cardColor],
            colors: [config.colors.warning]
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            curve: 'smooth', // Changed to 'smooth' for better appearance
            width: [2, 2]
          },
          colors: [config.colors.warning, config.colors.success, '#00cfe8'],
          grid: {
            borderColor: borderColor,
            xaxis: {
              lines: {
                show: true
              }
            },
            padding: {
              top: -20
            }
          },
          tooltip: {
            custom: function ({ series, seriesIndex, dataPointIndex, w }) {
              return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '</span>' + '</div>';
            }
          },
          xaxis: {
            categories: categories,
            title: {
              text: 'Time'
            },
            axisBorder: {
              show: true
            },
            axisTicks: {
              show: true
            },
            labels: {
              style: {
                colors: labelColor,
                fontSize: '13px'
              }
            }
          },
          yaxis: {
            labels: {
              style: {
                colors: labelColor,
                fontSize: '13px'
              }
            },
            title: {
              text: "Values",
              style: {
                color: labelColor,
                fontSize: '13px'
              }
            }
          }
        };

        // Render or update the chart
        if (!lineChartCompAlert) {
          // If the chart instance doesn't exist, create a new one
          lineChartCompAlert = new ApexCharts(lineChartAl, lineChartCompConfigAlert);
          lineChartCompAlert.render(); // Render the new instance
        } else {
          // If it exists, update the options
          lineChartCompAlert.updateOptions(lineChartCompConfigAlert); // Update options if it already exists
        }
      })
      .catch(error => console.error('Error fetching room data:', error));
  }

  // Initial fetch
  fetchDataAndUpdateChart();
  // Update every 5 seconds (5000 milliseconds)
  setInterval(fetchDataAndUpdateChart, 5000);
})();
