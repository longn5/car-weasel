$(document).ready(function(){

    $('#testButton').on('click', function(){
        $.ajax({
            'url': '127.0.0.1:8000/portal/api/datasets/allMakes/',
            success:function(data){
                console.log(data);
            },
            error: function(){
                console.log("requset failed");
            },
        });
    });

});