


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





//////////////////////////////////////////////////////////// overview

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
// Heat map chart
  // --------------------------------------------------------------------
  const heatMapEl = document.querySelector('#heatMapChart'),
    heatMapChartConfig = {
      chart: {
        height: 350,
        type: 'heatmap',
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      plotOptions: {
        heatmap: {
          enableShades: false,

          colorScale: {
            ranges: [
              {
                from: 0,
                to: 10,
                name: '0-10',
                color: '#90B3F3'
              },
              {
                from: 11,
                to: 20,
                name: '10-20',
                color: '#7EA6F1'
              },
              {
                from: 21,
                to: 30,
                name: '20-30',
                color: '#6B9AEF'
              },
              {
                from: 31,
                to: 40,
                name: '30-40',
                color: '#598DEE'
              },
              {
                from: 41,
                to: 50,
                name: '40-50',
                color: '#4680EC'
              },
              {
                from: 51,
                to: 60,
                name: '50-60',
                color: '#3474EA'
              }
            ]
          }
        }
      },
      dataLabels: {
        enabled: false
      },
      grid: {
        show: false
      },
      legend: {
        show: true,
        position: 'top',
        horizontalAlign: 'start',
        labels: {
          colors: legendColor,
          useSeriesColors: false
        },
        markers: {
          offsetY: 0,
          offsetX: -3
        },
        itemMargin: {
          vertical: 3,
          horizontal: 10
        }
      },
      stroke: {
        curve: 'smooth',
        width: 4,
        lineCap: 'round',
        colors: [cardColor]
      },
      series: [
        {
          name: 'SUN',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'MON',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'TUE',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'WED',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'THU',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'FRI',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        },
        {
          name: 'SAT',
          data: generateDataHeat(24, {
            min: 0,
            max: 60
          })
        }
      ],
      xaxis: {
        labels: {
          show: false,
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        },
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        }
      },
      yaxis: {
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        }
      }
    };
  if (typeof heatMapEl !== undefined && heatMapEl !== null) {
    const heatMapChart = new ApexCharts(heatMapEl, heatMapChartConfig);
    heatMapChart.render();
  }
})();  










