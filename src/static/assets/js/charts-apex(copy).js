/**
 * Charts Apex
 */

'use strict';

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

  // Color constant
  const chartColors = {
    column: {
      series1: '#826af9',
      series2: '#d2b0ff',
      bg: '#f8d3ff'
    },
    donut: {
      series1: '#fee802',
      series2: '#3fd0bd',
      series3: '#826bf8',
      series4: '#2b9bf4'
    },
    area: {
      series1: '#29dac7',
      series2: '#60f2ca',
      series3: '#a5f8cd'
    }
  };

  // Heat chart data generator
  function generateDataHeat(count, yrange) {
    let i = 0;
    let series = [];
    while (i < count) {
      let x = 'w' + (i + 1).toString();
      let y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

      series.push({
        x: x,
        y: y
      });
      i++;
    }
    return series;
  }

  function changeRange(range) {    
    var options = {
      data: [3, 6, 1, 13, 5, 8, 2, 2]
    };
    var options1 = {
      data: [5, 6, 8, 6, 5, 8, 2, 2]
    };
    var options2 = {
      data: [8, 6, 4, 16, 5, 8, 2, 2]
    };
    //var chart = new ApexCharts(document.querySelector("#verticalBarChart"), options);

    // if (range === 'Today') {    
    //     var chart = new ApexCharts(document.querySelector("#verticalBarChart"), options);
    // } else if (range === 'month') {
    //     var chart = new ApexCharts(
    //         document.querySelector("#verticalBarChart"),
    //         options1
    //     );
    // } else if (range === 'partner30') {
    //     var chart = new ApexCharts(
    //         document.querySelector("#verticalBarChart"),
    //         options2
    //     );
    // } else if (range === 'partnermonth') {
    //     var chart = new ApexCharts(
    //         document.querySelector("#verticalBarChart"),
    //         options2
    //     );
    // }

   // chart.render();
 } 


  // Line Area Chart
  // --------------------------------------------------------------------
  const areaChartEl = document.querySelector('#lineAreaChart'),
    areaChartConfig = {
      chart: {
        height: 400,
        type: 'area',
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        show: false,
        curve: 'straight'
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
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: true
          }
        }
      },
      colors: [chartColors.area.series3, chartColors.area.series2, chartColors.area.series1],
      series: [
        {
          name: 'Visits',
          data: [100, 120, 90, 170, 130, 160, 140, 240, 220, 180, 270, 280, 375]
        },
        {
          name: 'Clicks',
          data: [60, 80, 70, 110, 80, 100, 90, 180, 160, 140, 200, 220, 275]
        },
        {
          name: 'Sales',
          data: [20, 40, 30, 70, 40, 60, 50, 140, 120, 100, 140, 180, 220]
        }
      ],
      xaxis: {
        categories: [
          '7/12',
          '8/12',
          '9/12',
          '10/12',
          '11/12',
          '12/12',
          '13/12',
          '14/12',
          '15/12',
          '16/12',
          '17/12',
          '18/12',
          '19/12',
          '20/12'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      },
      fill: {
        opacity: 1,
        type: 'solid'
      },
      tooltip: {
        shared: false
      }
    };
  if (typeof areaChartEl !== undefined && areaChartEl !== null) {
    const areaChart = new ApexCharts(areaChartEl, areaChartConfig);
    areaChart.render();
  }






  // Bar Chart
  // --------------------------------------------------------------------
  const barChartEl = document.querySelector('#barChart'),
    barChartConfig = {
      chart: {
        height: 400,
        type: 'bar',
        stacked: true,
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '15%',
          colors: {
            backgroundBarColors: [
              chartColors.column.bg,
              chartColors.column.bg,
              chartColors.column.bg,
              chartColors.column.bg,
              chartColors.column.bg
            ],
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
      colors: [chartColors.column.series1, chartColors.column.series2],
      stroke: {
        show: true,
        colors: ['transparent']
      },
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: true
          }
        }
      },
      series: [
        {
          name: 'Apple',
          data: [90, 120, 55, 100, 80, 125, 175, 70, 88, 180]
        },
        {
          name: 'Samsung',
          data: [85, 100, 30, 40, 95, 90, 30, 110, 62, 20]
        }
      ],
      xaxis: {
        categories: ['7/12', '8/12', '9/12', '10/12', '11/12', '12/12', '13/12', '14/12', '15/12', '16/12'],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      },
      fill: {
        opacity: 1
      }
    };
  if (typeof barChartEl !== undefined && barChartEl !== null) {
    const barChart = new ApexCharts(barChartEl, barChartConfig);
    barChart.render();
  }





  
  // Scatter Chart
  // --------------------------------------------------------------------
  const scatterChartEl = document.querySelector('#scatterChart'),
    scatterChartConfig = {
      chart: {
        height: 400,
        type: 'scatter',
        zoom: {
          enabled: true,
          type: 'xy'
        },
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: true
          }
        }
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
      colors: [config.colors.warning, config.colors.primary, config.colors.success],
      series: [
        {
          name: '1 hour',
          data: [
            [5.4, 170],
            [5.4, 100],
            [5.7, 110],
            [5.9, 150],
            [6.0, 200],
            [6.3, 170],
            [5.7, 140],
            [5.9, 130],
            [7.0, 150],
            [8.0, 120],
            [9.0, 170],
            [10.0, 190],
            [11.0, 220],
            [12.0, 170],
            [13.0, 230]
          ]
        },
        {
          name: '2 Hour',
          data: [
            [14.0, 220],
            [15.0, 280],
            [16.0, 230],
            [18.0, 320],
            [17.5, 280],
            [19.0, 250],
            [20.0, 350],
            [20.5, 320],
            [20.0, 320],
            [19.0, 280],
            [17.0, 280],
            [22.0, 300],
            [18.0, 120]
          ]
        },
        {
          name: '3 hour',
          data: [
            [14.0, 290],
            [13.0, 190],
            [20.0, 220],
            [21.0, 350],
            [21.5, 290],
            [22.0, 220],
            [23.0, 140],
            [19.0, 400],
            [20.0, 200],
            [22.0, 90],
            [20.0, 120]
          ]
        }
      ],
      xaxis: {
        tickAmount: 10,
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          formatter: function (val) {
            return parseFloat(val).toFixed(1);
          },
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
        }
      }
    };
  if (typeof scatterChartEl !== undefined && scatterChartEl !== null) {
    const scatterChart = new ApexCharts(scatterChartEl, scatterChartConfig);
    scatterChart.render();
  }

  // Line Chart - Live Report
  // --------------------------------------------------------------------
  const lineChartEl = document.querySelector('#lineChart'),
    lineChartConfig = {
      series: [
        {
          data: [0, 280, 200, 220, 180, 270, 250, 70, 90, 200, 150, 160, 100, 150, 100, 50, 270, 250, 70, 90, 200, 150, 200, 150, 80]
        }
      ],
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
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: [config.colors.warning]
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: [config.colors.warning],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '0',
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
          '10',
          '11',
          '12',
          '13',
          '14',
          '15',
          '16',
          '17',
          '18',
          '19',
          '20',          
          '21',
          '22',
          '23',
          '24'
        ],        
        title: {
          text: 'Hours'
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
        },
        title: {
          text: "Hours (Today)  ",
          style: {
            color: labelColor,
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
          text: "# Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }        
      }
    };
  if (typeof lineChartEl !== undefined && lineChartEl !== null) {
    const lineChart = new ApexCharts(lineChartEl, lineChartConfig);
    lineChart.render();
  }


  

  // Line Chart - Last 3 days Comparison Alert 
  // --------------------------------------------------------------------
  const lineChartAl = document.querySelector('#lineChartCompAlert'),
    lineChartCompConfigAlert = {
      series: [
        {
          name: "Series A",
          data: [0, 80, 200, 220, 180, 270, 250, 230]
        },
        {
          name: "Series B",
          data: [0, 180, 100, 120, 80, 170, 150, 120]
        },
        {
          name: "Series C",
          data: [0, 280, 300, 320, 280, 370, 350, 200]
        }
      ],
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
        curve: 'straight',
        width: [2, 2, 2]
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '16/5',
          '17/5',
          '18/5',
          '19/5',
          '20/5',          
          '21/5',
          '22/5',
          '23/5'
        ],        
        title: {
          text: 'Date'
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
        },
        title: {
          text: "Hours",
          style: {
            color: labelColor,
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
          text: "# Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }        
      }
    };
  if (typeof lineChartAl !== undefined && lineChartAl !== null) {
    const lineChartCompAlert = new ApexCharts(lineChartAl, lineChartCompConfigAlert);
    lineChartCompAlert.render();
  }
   
 
  

    // vertical Bar Chart - Last 7 days Alerts
  // --------------------------------------------------------------------
  



  // Line Chart - Last 30 days report
  // --------------------------------------------------------------------
 


  
  
    // Line Chart - Loitering
  // --------------------------------------------------------------------
  const lineloisChartEl = document.querySelector('#lineloisChart'),
    lineloisChartConfig = {
      series: [
        {
          data: [0, 100, 20, 150, 100, 50, 270, 250, 70, 90, 200, 150, 200, 150, 80]
        }
      ],
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
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: ['#e5df33']
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: ['#e5df33'],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '0',
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
          '10',
          '11',
          '12',
          '13',
          '14',
          '15',
          '16',
          '17',
          '18',
          '19',
          '20',          
          '21',
          '22',
          '23',
          '24'
        ],        
        title: {
          text: 'Hours'
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
        },
        title: {
          text: "Hours (Today)  ",
          style: {
            color: labelColor,
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
          text: "# Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }        
      }
    };
  if (typeof lineloisChartEl !== undefined && lineloisChartEl !== null) {
    const lineloisChart = new ApexCharts(lineloisChartEl, lineloisChartConfig);
    lineloisChart.render();
  }



    // Loitering Bar Chart - Last 3 days
  // --------------------------------------------------------------------
  const loisBarChartEl = document.querySelector('#loisBarChart'),
  loisBarChartConfig = {
      chart: {
        height: 385,
        type: 'bar',
        toolbar: {
          show: false
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '20%',
          vertical: true,
          barHeight: '10%',
          startingShape: 'rounded',
          borderRadius: 8
        }
      },
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: false
          }
        },
        padding: {
          top: -20,
          bottom: -12
        }
      },
      colors: config.colors.info,
      dataLabels: {
        enabled: false
      },
      colors: ['#ea5455'],
      series: [
        {
          data: [33, 78, 40, 91, 16, 41, 66, 25, 75, 68, 22, 42]
        }
      ],
      xaxis: {
        categories: ['1/12', '2/12', '3/12', '4/12', '5/12', '6/12', '7/12', '8/12', '9/12', '10/12', '11/12', '12/12'],
        title: {
          text: "",
        },   
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        },
        title: {
          text: "",
          style: {
            color: labelColor,
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
          text: "Loitering Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }
      }
    };
  if (typeof loisBarChartEl !== undefined && loisBarChartEl !== null) {
    const loisBarChart = new ApexCharts(loisBarChartEl, loisBarChartConfig);
    loisBarChart.render();
  }


      // Line Chart - Loistering Last 30 days
  // --------------------------------------------------------------------
  const lois30dChartEl = document.querySelector('#lois30dChart'),
  lois30dChartConfig = {
      series: [
        {
          data: [220, 100, 70, 100, 100, 140, 150, 100, 240, 90, 180 , 90, 390, 100, 20, 150, 100, 150, 100, 240, 90, 180 , 240, 90, 180 , 150, 100, 100, 70, 100, 410]
        }
      ],
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
        strokeWidth: 5,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: ['#03a59d']
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth'
      },
      colors: ['#03a59d'],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '0',
          '1/12',
          '2/12',
          '3/12',
          '4/12',
          '5/12',
          '6/12',
          '7/12',
          '8/12',
          '9/12',
          '10/12',
          '11/12',
          '12/12',
          '13/12',
          '14/12',
          '15/12',
          '16/12',
          '17/12',
          '18/12',
          '19/12',
          '20/12',          
          '21/12',
          '22/12',
          '23/12',
          '24/12',
          '25/12',
          '26/12',
          '27/12',
          '28/12',
          '29/12',
          '30/12',
        ],        
        title: {
          text: ''
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
        },
        title: {
          text: " ",
          style: {
            color: labelColor,
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
          text: "#Loitering Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }        
      }
    };
  if (typeof lois30dChartEl !== undefined && lois30dChartEl !== null) {
    const lois30dChart = new ApexCharts(lois30dChartEl, lois30dChartConfig);
    lois30dChart.render();
  }



    
  // Intrusion Custom Selection Chart
  // --------------------------------------------------------------------
  const loiteringChartCl = document.querySelector('#loiteringChart'),
  loiteringChartConfig = {
      series: [
        {
          name: "Series A",
          data: [0, 80, 200, 220, 180, 270, 250, 70, 90, 200, 150, 160, 100, 150, 100, 50, 270, 250, 70, 90, 20, 60, 80, 50, 110]
        },
        {
          name: "Series B",
          data: [0, 180, 100, 120, 80, 170, 150, 170, 190, 300, 50, 240, 40, 50, 10, 50, 170, 150, 70, 210, 300, 150, 270, 350, 470]
        },
        {
          name: "Series C",
          data: [0, 280, 300, 320, 280, 370, 350, 370, 390, 590, 300, 350, 360, 300, 350, 450, 150, 370, 450, 470, 190, 300, 250, 300, 250]
        }
      ],
      chart: {
        height: 410,
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
        colors: ['#ffe800']
      },
      dataLabels: {
        enabled: false
      },
      markers: {
          size: 1,
      },
      stroke: {
        curve: 'straight',
        dashArray: 0,
        width: [3, 3, 3]
      },
      colors: ['#e5df33', '#ce4f53', '#0a9491'],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '0',
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
          '10',
          '11',
          '12',
          '13',
          '14',
          '15',
          '16',
          '17',
          '18',
          '19',
          '20',          
          '21',
          '22',
          '23',
          '24'
        ],        
        title: {
          text: 'Hours'
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
        },
        title: {
          text: "Time Resolution",
          style: {
            color: labelColor,
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
          text: "#Loitering Count",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }        
      }
    };
  if (typeof loiteringChartCl !== undefined && loiteringChartCl !== null) {
    const loiteringChart = new ApexCharts(loiteringChartCl, loiteringChartConfig);
    loiteringChart.render();
  }

    


  // Dwelltime Custom Selection Chart
  // --------------------------------------------------------------------
  const dwellChartCl = document.querySelector('#dwellChart'),
  dwellChartConfig = {
      series: [
        {
          name: "Series A",
          data: ['1 Min', '2 Min','3 Min','7 Min','5 Min','10 Min','15 Min','20 Min','25 Min','30 Min','40 Min','50 Min','60 Min']
        },
        {
          name: "Series B",
          data: ['20', '140','90','140','70','20','150','480','70','20','150','290','40']
        } 
      ],
      chart: {
        height: 410,
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
        colors: ['#ffe800']
      },
      dataLabels: {
        enabled: false
      },
      markers: {
          size: 1,
      },
      stroke: {
        curve: 'smooth',
        dashArray: '1',
        width: [3, 3]
      },
      colors: ['#e5df33', '#ce4f53'],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {      
        categories: [
          '0',
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
          '10',
          '11',
          '12',
          '13',
          '14',
          '15',
          '16',
          '17',
          '18',
          '19',
          '20',          
          '21',
          '22',
          '23',
          '24'
        ],        
        title: {
          text: 'Hours'
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
        }, 
        title: {
          text: "Hours",
          style: {
            color: labelColor,
            fontSize: '13px'
          }
        }
      },
      yaxis: [
        {
          seriesName: "Series A",
          labels: {
            style: {
              colors: labelColor,
              fontSize: '13px'
            }
          }, 
          title: {
            text: "#Avg Dwell Time",
            style: {
              color: labelColor,
              fontSize: '13px'
            }
          }        
        },
        {
          seriesName: "Series B",
          opposite: true,
          labels: {
            style: {
              colors: labelColor,
              fontSize: '13px'
            }
          }, 
          title: {
            text: "#Avg Dwell Count",
            style: {
              color: labelColor,
              fontSize: '13px'
            }
          },
          stroke: {
            curve: 'straight',
            dashArray: '0',
            width: [3, 3]
          },      
        }
      ]
    };
  if (typeof dwellChartCl !== undefined && dwellChartCl !== null) {
    const dwellChart = new ApexCharts(dwellChartCl, dwellChartConfig);
    dwellChart.render();
  }


    // Line Chart
  // --------------------------------------------------------------------
  const lineChartzEl = document.querySelector('#lineChartz'),
    lineChartzConfig = {
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
      
      series: [
        {
          data: [180, 100,  180, 270, 250, 70, 90, 200, 150,  100, 50]
        }
      ],
      markers: {
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: [config.colors.success]
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: [config.colors.success],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {
        categories: [
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
          '10',
          '11',
          '12',
          '13',
          '14',
          '15',
          '16',
          '17',
          '18',
          '19',
          '20',          
          '21',
          '22',
          '23',
          '24'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      }
    };
  if (typeof lineChartzEl !== undefined && lineChartzEl !== null) {
    const lineChartz = new ApexCharts(lineChartzEl, lineChartzConfig);
    lineChartz.render();
  }


        // Line Chart
  // --------------------------------------------------------------------
  const queueChartEl = document.querySelector('#queueChart'),
  queueChartConfig = {
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
      
      series: [
        {
          data: [20, 70,  180, 270, 250, 70, 90, 200, 150,  100, 50]
        }
      ],
      markers: {
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: [config.colors.info]
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: [config.colors.info],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {
        categories: [
          '1/12',
          '2/12',
          '3/12',
          '4/12',
          '5/12',
          '6/12',
          '7/12',
          '8/12',
          '9/12',
          '10/12',
          '11/12',
          '12/12',
          '13/12',
          '14/12',
          '15/12'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      }
    };
  if (typeof queueChartEl !== undefined && queueChartEl !== null) {
    const queueChart = new ApexCharts(queueChartEl, queueChartConfig);
    queueChart.render();
  }


      // Line Chart
  // --------------------------------------------------------------------
  const queueChartzEl = document.querySelector('#queueChartz'),
  queueChartzConfig = {
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
      
      series: [
        {
          data: [20, 70,  180, 270, 250, 70, 90, 200, 150,  100, 50]
        }
      ],
      markers: {
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: [config.colors.danger]
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: [config.colors.danger],
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
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {
        categories: [
          '1/12',
          '2/12',
          '3/12',
          '4/12',
          '5/12',
          '6/12',
          '7/12',
          '8/12',
          '9/12',
          '10/12',
          '11/12',
          '12/12',
          '13/12',
          '14/12',
          '15/12'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      }
    };
  if (typeof queueChartzEl !== undefined && queueChartzEl !== null) {
    const queueChartz = new ApexCharts(queueChartzEl, queueChartzConfig);
    queueChartz.render();
  }

  
   
  



   
  // vertical Bar Chart
  // --------------------------------------------------------------------
  const verticalzBarChartEl = document.querySelector('#verticalzBarChart'),
  verticalzBarChartConfig = {
      chart: {
        height: 400,
        type: 'bar',
        toolbar: {
          show: false
        }
      },
      plotOptions: {
        bar: {
          columnWidth: '25%',
          vertical: true,
          barHeight: '20%',
          startingShape: 'rounded',
          borderRadius: 8
        }
      },
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: false
          }
        },
        padding: {
          top: -20,
          bottom: -12
        }
      },
      colors: config.colors.info,
      dataLabels: {
        enabled: false
      },
      series: [
        {
          data: [700, 350, 480, 600, 210, 550, 150]
        }
      ],
      xaxis: {
        categories: ['1/12', '2/12', '3/12', '4/12', '5/12', '6/12', '7/12', '8/12', '9/12', '10/12'],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
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
        }
      }
    };
  if (typeof verticalzBarChartEl !== undefined && verticalzBarChartEl !== null) {
    const verticalzBarChart = new ApexCharts(verticalzBarChartEl, verticalzBarChartConfig);
    verticalzBarChart.render();
  }


  // Candlestick Chart
  // --------------------------------------------------------------------
  const candlestickEl = document.querySelector('#candleStickChart'),
    candlestickChartConfig = {
      chart: {
        height: 410,
        type: 'candlestick',
        parentHeightOffset: 0,
        toolbar: {
          show: false
        }
      },
      series: [
        {
          data: [
            {
              x: new Date(1538778600000),
              y: [150, 170, 50, 100]
            },
            {
              x: new Date(1538780400000),
              y: [200, 400, 170, 330]
            },
            {
              x: new Date(1538782200000),
              y: [330, 340, 250, 280]
            },
            {
              x: new Date(1538784000000),
              y: [300, 330, 200, 320]
            },
            {
              x: new Date(1538785800000),
              y: [320, 450, 280, 350]
            },
            {
              x: new Date(1538787600000),
              y: [300, 350, 80, 250]
            },
            {
              x: new Date(1538789400000),
              y: [200, 330, 170, 300]
            },
            {
              x: new Date(1538791200000),
              y: [200, 220, 70, 130]
            },
            {
              x: new Date(1538793000000),
              y: [220, 270, 180, 250]
            },
            {
              x: new Date(1538794800000),
              y: [200, 250, 80, 100]
            },
            {
              x: new Date(1538796600000),
              y: [150, 170, 50, 120]
            },
            {
              x: new Date(1538798400000),
              y: [110, 450, 10, 420]
            },
            {
              x: new Date(1538800200000),
              y: [400, 480, 300, 320]
            },
            {
              x: new Date(1538802000000),
              y: [380, 480, 350, 450]
            }
          ]
        }
      ],
      xaxis: {
        type: 'datetime',
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        }
      },
      yaxis: {
        tooltip: {
          enabled: true
        },
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        }
      },
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
      plotOptions: {
        candlestick: {
          colors: {
            upward: config.colors.success,
            downward: config.colors.danger
          }
        },
        bar: {
          columnWidth: '40%'
        }
      }
    };
  if (typeof candlestickEl !== undefined && candlestickEl !== null) {
    const candlestickChart = new ApexCharts(candlestickEl, candlestickChartConfig);
    candlestickChart.render();
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

  // Radial Bar Chart
  // --------------------------------------------------------------------
  const radialBarChartEl = document.querySelector('#radialBarChart'),
    radialBarChartConfig = {
      chart: {
        height: 380,
        type: 'radialBar'
      },
      colors: [chartColors.donut.series1, chartColors.donut.series2, chartColors.donut.series4],
      plotOptions: {
        radialBar: {
          size: 185,
          hollow: {
            size: '40%'
          },
          track: {
            margin: 10,
            background: config.colors_label.secondary
          },
          dataLabels: {
            name: {
              fontSize: '2rem',
              fontFamily: 'Public Sans'
            },
            value: {
              fontSize: '1.2rem',
              color: legendColor,
              fontFamily: 'Public Sans'
            },
            total: {
              show: true,
              fontWeight: 400,
              fontSize: '1.3rem',
              color: headingColor,
              label: 'Comments',
              formatter: function (w) {
                return '80%';
              }
            }
          }
        }
      },
      grid: {
        borderColor: borderColor,
        padding: {
          top: -25,
          bottom: -20
        }
      },
      legend: {
        show: true,
        position: 'bottom',
        labels: {
          colors: legendColor,
          useSeriesColors: false
        }
      },
      stroke: {
        lineCap: 'round'
      },
      series: [80, 50, 35],
      labels: ['Comments', 'Replies', 'Shares']
    };
  if (typeof radialBarChartEl !== undefined && radialBarChartEl !== null) {
    const radialChart = new ApexCharts(radialBarChartEl, radialBarChartConfig);
    radialChart.render();
  }

  // Radar Chart
  // --------------------------------------------------------------------
  const radarChartEl = document.querySelector('#radarChart'),
    radarChartConfig = {
      chart: {
        height: 350,
        type: 'radar',
        toolbar: {
          show: false
        },
        dropShadow: {
          enabled: false,
          blur: 8,
          left: 1,
          top: 1,
          opacity: 0.2
        }
      },
      legend: {
        show: true,
        position: 'bottom',
        labels: {
          colors: legendColor,
          useSeriesColors: false
        }
      },
      plotOptions: {
        radar: {
          polygons: {
            strokeColors: borderColor,
            connectorColors: borderColor
          }
        }
      },
      yaxis: {
        show: false
      },
      series: [
        {
          name: 'iPhone 12',
          data: [41, 64, 81, 60, 42, 42, 33, 23]
        },
        {
          name: 'Samsung s20',
          data: [65, 46, 42, 25, 58, 63, 76, 43]
        }
      ],
      colors: [chartColors.donut.series1, chartColors.donut.series3],
      xaxis: {
        categories: ['Battery', 'Brand', 'Camera', 'Memory', 'Storage', 'Display', 'OS', 'Price'],
        labels: {
          show: true,
          style: {
            colors: [labelColor, labelColor, labelColor, labelColor, labelColor, labelColor, labelColor, labelColor],
            fontSize: '13px',
            fontFamily: 'Public Sans'
          }
        }
      },
      fill: {
        opacity: [1, 0.8]
      },
      stroke: {
        show: false,
        width: 0
      },
      markers: {
        size: 0
      },
      grid: {
        show: false,
        padding: {
          top: -20,
          bottom: -20
        }
      }
    };
  if (typeof radarChartEl !== undefined && radarChartEl !== null) {
    const radarChart = new ApexCharts(radarChartEl, radarChartConfig);
    radarChart.render();
  }

  // Donut Chart
  // --------------------------------------------------------------------
  const donutChartEl = document.querySelector('#donutChart'),
    donutChartConfig = {
      chart: {
        height: 390,
        type: 'donut'
      },
      labels: ['Operational', 'Networking', 'Hiring', 'R&D'],
      series: [42, 7, 25, 25],
      colors: [
        chartColors.donut.series1,
        chartColors.donut.series4,
        chartColors.donut.series3,
        chartColors.donut.series2
      ],
      stroke: {
        show: false,
        curve: 'straight'
      },
      dataLabels: {
        enabled: true,
        formatter: function (val, opt) {
          return parseInt(val, 10) + '%';
        }
      },
      legend: {
        show: true,
        position: 'bottom',
        markers: { offsetX: -3 },
        itemMargin: {
          vertical: 3,
          horizontal: 10
        },
        labels: {
          colors: legendColor,
          useSeriesColors: false
        }
      },
      plotOptions: {
        pie: {
          donut: {
            labels: {
              show: true,
              name: {
                fontSize: '2rem',
                fontFamily: 'Public Sans'
              },
              value: {
                fontSize: '1.2rem',
                color: legendColor,
                fontFamily: 'Public Sans',
                formatter: function (val) {
                  return parseInt(val, 10) + '%';
                }
              },
              total: {
                show: true,
                fontSize: '1.5rem',
                color: headingColor,
                label: 'Operational',
                formatter: function (w) {
                  return '42%';
                }
              }
            }
          }
        }
      },
      responsive: [
        {
          breakpoint: 992,
          options: {
            chart: {
              height: 380
            },
            legend: {
              position: 'bottom',
              labels: {
                colors: legendColor,
                useSeriesColors: false
              }
            }
          }
        },
        {
          breakpoint: 576,
          options: {
            chart: {
              height: 320
            },
            plotOptions: {
              pie: {
                donut: {
                  labels: {
                    show: true,
                    name: {
                      fontSize: '1.5rem'
                    },
                    value: {
                      fontSize: '1rem'
                    },
                    total: {
                      fontSize: '1.5rem'
                    }
                  }
                }
              }
            },
            legend: {
              position: 'bottom',
              labels: {
                colors: legendColor,
                useSeriesColors: false
              }
            }
          }
        },
        {
          breakpoint: 420,
          options: {
            chart: {
              height: 280
            },
            legend: {
              show: false
            }
          }
        },
        {
          breakpoint: 360,
          options: {
            chart: {
              height: 250
            },
            legend: {
              show: false
            }
          }
        }
      ]
    };
  if (typeof donutChartEl !== undefined && donutChartEl !== null) {
    const donutChart = new ApexCharts(donutChartEl, donutChartConfig);
    donutChart.render();
  }
})();
