let vehicle_array = []; // Collection of vehicle objects populated by VIN decode

// When the page is ready, bind the decode button to API call.
$(document).ready(function(){
    $('#vin-decode-button').on('click', function(e){
        var vin = $('#vin-entry').val();
        e.stopImmediatePropagation();
        decodeVIN(vin);
    });

    $('#send-vehicles-button').on('click', function(){
        sendVehicles();
    });
});


// Takes in an object representing the results of a
// VIN decode.
function addToTable(vehObj){
    vehicle_array.push(vehObj);

    let retStr = `<tr><td>${vehObj.vin}</td>`;
    retStr += `<td>${vehObj.make}</td>`;
    retStr += `<td>${vehObj.model}</td>`;
    retStr += `<td>${vehObj.series}</td>`;
    retStr += `<td>${vehObj.year}</td>`;
    retStr += `<td>${vehObj.trim}</td>`;
    retStr += `<td>${vehObj.cylinders}</td>`;
    retStr += `<td><input type="checkbox" id="saveVehicle" checked></td></tr>`;

    $('#potential-inventory-body').append(retStr);
}


// Makes the API call to NHTSA VIN Decode API and uses the response
// to populate an object representing a vehicle. 
function decodeVIN(vin){
    var url = "https://vpic.nhtsa.dot.gov/api//vehicles/DecodeVin/";
    url += vin + "?format=json";
    var make = null;
    var year = null;
    var model = null;
    var series = null;
    var trim = null;
    var body = null;
    var doors = null;
    var drive = null;
    var cylinders = null;
    var err = null;
    var vehicle = {};

    $.ajax({
        'url': url,
        success: function(data){

            let results = data['Results'];
            for(var entry in results){

                if(results[entry]['Variable'] == 'Error Code'){
                    err = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Make'){
                    make = results[entry]['Value'];
                }
                
                if(results[entry]['Variable'] == 'Model'){
                    model = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Model Year'){
                    year = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Trim'){
                    trim = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Series'){
                    series = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Body Class'){
                    body = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Doors'){
                    doors = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Drive Type'){
                    drive = results[entry]['Value'];
                }

                if(results[entry]['Variable'] == 'Engine Number of Cylinders'){
                    cylinders = results[entry]['Value'];
                }
            }

            if(err === "0" || err === 0){
                vehicle.make = make;
                vehicle.year = year;
                vehicle.model = model;
                vehicle.series = series;
                vehicle.trim = trim;
                vehicle.body = body;
                vehicle.doors = doors;
                vehicle.drive = drive;
                vehicle.cylinders = cylinders;
                vehicle.vin = vin;

                addToTable(vehicle);
            }else{
                let msg = `Incorrect VIN  ${vin} . Check VIN and try again.`;
                let a = generateAlert('danger', msg);
                $('#alert-space').append(a);
            }
        },
        error: function(){
            console.log("Error during API call");
            let msg = "Error with NHTSA API";
            let a = generateAlert("danger", msg);
            $('#alert-space').append(a);
        },
    });
}



// https://docs.djangoproject.com/en/2.2/ref/csrf/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function sendVehicles(){
    let obj = vehicleArrayToJSON();
    let token = getCookie('csrftoken');

    $.ajaxSetup({
      beforeSend: function(xhr){
        xhr.setRequestHeader('X-CSRFToken', token);
      }
    });

    $.ajax({
      'url': 'http://127.0.0.1:8000/seller_portal/',
      'type': 'POST',
      'dataType': 'json',
      'contentType': 'application/json; charset=utf-8',
      data: obj,
      success: function(data){
            let val = parseInt(data['status']);

            if(val > 0){
                let msg = `Added ${val} Vehicle(s) To Inventory.`;
                let a = generateAlert('success', msg);
                $('#alert-space').append(a);
            }else{
                let msg = 'Failed To Upload Changes To Inventory!';
                let a = generateAlert('danger', msg);
                $('#alert-space').append(a);
            }
            console.log(data);
      },
      error: function(){
            console.log("Something went wrong POSTing");
            let msg = 'Failed To Upload Changes To Inventory!';
            let a = generateAlert('danger', msg);
            $('#alert-space').append(a);
      },
    });
}



// Converts the array of vehicles the buyer wants to add into
// a JSON string.
function vehicleArrayToJSON(){
    let vehObjs = [];
    let count = 0;

    for(var entry in vehicle_array){
        let obj = {
        "make": vehicle_array[entry].make,
        "model": vehicle_array[entry].model,
        "year": vehicle_array[entry].year,
        "series": vehicle_array[entry].series,
        "trim": vehicle_array[entry].trim,
        "body": vehicle_array[entry].body,
        "doors": vehicle_array[entry].doors,
        "drive": vehicle_array[entry].drive,
        "cylinders": vehicle_array[entry].cylinders,
        "vin": vehicle_array[entry].vin,
        }
        vehObjs.push(obj);
        ++count;
    }

    let ret = {"vehicles": vehObjs,
            "count": count,};

    return JSON.stringify(ret);
}


// Alert type is a bootstrap alert class, msg is the message to be displayed
// in the alert. Returns HTML to generate alert.
function generateAlert(alertType, msg){
    let retStr = `
    <div id="addPostsAlert" class="alert alert-${alertType} alert-dismissible fade show" role="alert">
      ${msg}
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    `;
  
    return retStr;
}