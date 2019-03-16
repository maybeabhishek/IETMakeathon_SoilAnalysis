
var tempData = null;
var phData = null;
var moistureData = null;
var humidityData = null;
function getSensor(){
  $.ajax({
    url:"/getSensor",
    success: function(data){
      Object.keys(data.values).forEach((element) => {
        document.getElementById(element).innerText=data.values[element];
        if(element == 'temperatureValue')
          tempData = data.values[element];
        else if(element == 'phValue')
          phData = data.values[element];
        else if(element == 'moistureValue')
          moistureData = data.values[element]
        else if(element == 'humidityValue')
          humidityData = data.values[element]
      });
    }
  })
}
setInterval(getSensor, 1000);