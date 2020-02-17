# TUTO_GRAPH

## Echarts

site officielle[]

### Steps 1: HTML

Create a div where displays echart in your HTML

    <div id="main" style="width:100%; height:400px;">
    
### Steps 2 : Javasscript

<script type="text/javascript">
    
        // based on prepared DOM, initialize echarts instance
        var myChart = echarts.init(document.getElementById('main'));
        
        
        // specify chart configuration item and data
        var option = {
            title: {
                text: 'ECharts entry example'
            },
            tooltip: {},
            legend: {
                data:['Sales']
            },
            xAxis: {
                data: ["shirt","cardign","chiffon shirt","pants","heels","socks"]
            },
            yAxis: {},
            series: [{
                name: 'Sales',
                type: 'line',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };

       

        // use configuration item and data specified to show chart
        myChart.setOption(option);
        
Source[https://www.echartsjs.com/examples/en/index.html]
       
