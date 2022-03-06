var map;

function initMap() {



	var locations = [
		["Los Angeles", 34.052235, -118.243683],
		["Santa Monica", 34.024212, -118.496475],
		["Redondo Beach", 33.849182, -118.388405],
		["Newport Beach", 33.628342, -117.927933],
		["Long Beach", 33.77005, -118.193739],
	];
    var src1 = document.getElementById("myVar").value;
    var data = JSON.parse(src1);
    var center = { lat: 43.161030, lng: -77.610924 };
    var map = new google.maps.Map(document.getElementById("map"), {
		zoom: 10,
		center: center,
	});
	var marker = new google.maps.Marker({
		position: center,
		map: map,
	});
     for(var x in data){
       if(data[x].type == "Zone"){
            marker = new google.maps.Circle({
	        strokeColor: "#FF0000",
            strokeOpacity: 0.8,
            strokeWeight: 2,
          fillColor: "#FF0000",
          fillOpacity: 0.35,
          map,
          center: { lat: data[x].lat, lng: data[x].long },
          radius:  1000,
             });

            }
//	    }else if(data[x].type == "Zone"){
	     else {
	     var image  = ""
	     if(data[x].type == "Shelter"){
	        image= "http://maps.google.com/mapfiles/kml/shapes/ranger_station.png"
	     }else if(data[x].type == "Transport"){
	        image= "http://maps.google.com/mapfiles/kml/shapes/bus.png"
	     }else{
	        image= "http://maps.google.com/mapfiles/kml/pal3/icon46.png"
	     }
	     marker = new google.maps.Marker({
                position: new google.maps.LatLng(
                    data[x].lat,
                    data[x].long
                ),
                map: map,
                title: data[x].type,
                icon: image,
            });
	    }
		google.maps.event.addListener(
			marker,
			"click",
			(function (marker, count) {
				return function () {
					var infoWindow = new google.maps.InfoWindow({
						content: data[x].type,
					});

					infowindow.open(map, marker);
				};
			})(marker, count)
		);
    }

	var marker, count;

}
