function updateView() {    
    var table = document.getElementById("table");
    var barChart = document.getElementById("barChart");
    var pieChart = document.getElementById("pieChart");
    var selectView = document.getElementById('selectView');
    var option = selectView.options[selectView.selectedIndex];
    if (option.value === "barChartView") {
        table.style.display = "none";
        barChart.style.display = "block";
        pieChart.style.display = "none";
    }
    else if (option.value === "pieChartView") {
        table.style.display = "none";
        barChart.style.display = "none";
        pieChart.style.display = "block";
    }
    else {
        table.style.display = "block";
        barChart.style.display = "none";
        pieChart.style.display = "none";
    }
}
updateView();