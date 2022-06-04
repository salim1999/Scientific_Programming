function sendRequest(){
var array = new Array ();
var drone = document.getElementById("drone");
var aircraft = document.getElementById("aircraft");
var tank = document.getElementById("tank");
var helicopter = document.getElementById("helicopter");


if (drone.checked){
drone="true";
}else{
drone="false"
}

if (aircraft.checked){
aircraft="true";
}else{
aircraft="false"
}

if (tank.checked){
tank="true";
}else{
tank="false"
}

if (helicopter.checked){
helicopter="true";
}else{
helicopter="false"
}
var d = new Date().getTime();
$.ajax({
    url: '/type',
    type: 'GET',
    data : {drone: drone, aircraft: aircraft,helicopter:helicopter,tank: tank},
    success: function(response){
        $("#chart").attr("src", "static/Output.jpg?"+d);
     },
    error: function(error){
      console.log(error)
    }
});

}