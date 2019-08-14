$(document).ready(function(){

    $('#vin-decode').on('click', function(){
        var vin = $('#vin-entry').val();
        decodeVIN(vin);
    });




});



// $('#vin-decode').on('click', function(){
//     var vin = $('#vin-entry').val();
//     decodeVIN(vin);
// });



function decodeVIN(vin){
    var url = "https://vpic.nhtsa.dot.gov/api//vehicles/DecodeVin/";
    url += vin + "?format=json";
    var make = "";
    var year = "";
    var model = "";
    var series = "";
    var trim = "";
    var body = "";
    var doors = "";
    var drive = "";
    var cylinders = "";
    var vehicle = {};

    $.ajax({
        'url': url,
        success: function(data){
            if(parseInt(data['Count']) > 0){
                var results = data['Results'];

                for(var entry in results){
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

                vehicle.make = make;
                vehicle.year = year;
                vehicle.model = model;
                vehicle.series = series;
                vehicle.trim = trim;
                vehicle.body = body;
                vehicle.doors = doors;
                vehicle.drive = drive;
                vehicle.cylinders = cylinders;

                console.log(vehicle);
                $('#look-up-results').html(vehicle);
            }else{
                console.log("Something doesn't seen right...");
            }
        },
        error: function(){
            console.log("Error during API call");
        },
    });
}