[![Badge](https://img.shields.io/badge/version-v3.5%E2%80%90alpha-blue.svg?logo=linkedin)](https://github.com/hitesh-temp-account/Breach/blob/main/gradle.properties#L18)\
[![example workflow](https://github.com/hitesh-temp-account/Breach/actions/workflows/spandan.yml/badge.svg)](https://github.com/hitesh-temp-account/Breach/actions/workflows/spandan.yml)\
[![myTest workflow](https://github.com/hitesh-temp-account/Breach/actions/workflows/myTest.yml/badge.svg)](https://github.com/hitesh-temp-account/Breach/actions/workflows/myTest.yml)\
[![hitesh workflow](https://github.com/hitesh-temp-account/Breach/actions/workflows/hiteshWorkflow.yml/badge.svg)](https://github.com/hitesh-temp-account/Breach/actions/workflows/hiteshWorkflow.yml)\
![hitesh workflow](https://img.shields.io/maven-central/v/xstream/xstream)
![Coverage](https://img.shields.io/badge/coverage-35.19%25-green.svg)
[![Known Vulnerabilities](https://snyk-widget.herokuapp.com/badge/pip/hitesh-temp-account/Breach/badge.svg)](https://snyk.io/test/github/hitesh-temp-account/Breach)

Chart trial:
<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Mushrooms', 3],
          ['Onions', 1],
          ['Olives', 1],
          ['Zucchini', 1],
          ['Pepperoni', 2]
        ]);

        // Set chart options
        var options = {'title':'How Much Pizza I Ate Last Night',
                       'width':400,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div>
  </body>
</html>
