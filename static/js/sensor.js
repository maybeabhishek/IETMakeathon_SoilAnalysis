
function getSensor(){
  $.ajax({
    url:"/getSensor",
    success: function(data){
      Object.keys(data.values).forEach((element) => {
        document.getElementById(element).innerText=data.values[element];
      });
    }
  })
}
setInterval(getSensor, 1000);