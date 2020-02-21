# TUTO_GRAPH

## Echarts


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
        
Source -> https://www.echartsjs.com/examples/en/index.html

## Fusioncharts

### Steps 1: Template HTML

    <div class="card">
    <div class="card-body">
        <h4 class="mt-0 header-title">Statistique </h4>
        <!-- Container div by id 'chart-1' -->
        <div id="chart-1" dir="ltr"></div>
        <!-- dumping JavaScript code here -->
        {{ output|safe }}
    </div>
    </div>
    
 ### Steps 2: Application views
 
    from collections import OrderedDict
     ............
     
    def fusionchart(request):
    
        # ----declaration des dict contaner des data ----#
        dataSource = OrderedDict()
        chartConfig = OrderedDict()
        
        # ---- Enregistrement des configuration ----#
        chartConfig["caption"] = "Superficie des pays"
        chartConfig["subcaption"] = "Stats"
        chartConfig["showvalues"] = "1"
        chartConfig["showpercentintooltip"] = "0"
        chartConfig["numberprefix"] = "Personnes: "
        chartConfig["enablemultislicing"] = "1"
        chartConfig["theme"] = "candy"

        dataSource["chart"] = chartConfig
        
            
        # ---- Enregistrement des données ----#
        dataSource["data"] = []
        dataSource["data"].append({"label": 'Cote d'Ivooire', "value": "322462" })
        dataSource["data"].append({"label": 'Benin', "value": "57382728"})
        dataSource["data"].append({"label": 'Madascacar', "value": "36587"})
        
        # ---- Objet charts ----#
        chartObj = FusionCharts( 'pie3d', 'ex1', '550', '400', 'chart-1', 'json', dataSource )
        data = {
            'output': chartObj.render(),
        }
        
        return render(request, 'ma_page', data)
       
