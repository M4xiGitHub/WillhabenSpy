var config;
var json = {};

$.getJSON("data.json", function(json) {

    var keys = Object.keys(json)
    keys.shift()
    var dataset = []

    json["Products"].forEach(value => {
        dataset.push({
            label: value,
            data: [],
            borderColor: ['#' + Math.random().toString(16).substr(2, 6)],
            borderWidth: 1
        })
    });

    keys.forEach(value => {
        var i = 0;
        while (i < json[value].length) {
            dataset[i]["data"].push(json[value][i]);
            console.log(dataset[i]["data"])
            i++;
        }
    });



    config = {
        type: 'line',
        data: {
            labels: keys,
            datasets: dataset
        },
        options: {
            legend: {
                labels: {
                    fontColor: "white",
                    fontSize: 18
                }
            },
            responsive: true,
            title: {
                display: true,
                text: "WillhabenSpy",
                fontColor: "white",
                fontSize: 25
            },
            tooltips: {
                mode: 'label',
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },

            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        display: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Zeitpunkt',
                        fontColor: "white",
                        fontSize: 18
                    },
                    ticks: {
                        fontColor: "white",
                        fontSize: 14,
                        stepSize: 1,
                        beginAtZero: true
                    }
                }],
                yAxes: [{
                    display: true,

                    scaleLabel: {
                        display: true,
                        labelString: 'Preis',
                        fontColor: "white",
                        fontSize: 18
                    },
                    ticks: {
                        fontColor: "white",
                        fontSize: 14,
                        stepSize: 100,
                        beginAtZero: true
                    },
                    gridLines: {
                        color: "#002d43"
                    }
                }]


            },
            plugins: {
                zoom: {

                    zoom: {
                        enabled: true,

                        mode: 'xy',
                    }
                }
            }

        }

    };
    var ctx = document.getElementById("myChart").getContext("2d");
    window.myLine = new Chart(ctx, config);

});