$(document).ready(function(){

    $('#testButton').on('click', function(){
        $.ajax({
            'url': 'https://127.0.0.1:8000/api/datasets/allMakes/',
            success:function(data){
                console.log(data);
            },
            error: function(){
                console.log("requset failed");
            },
        });
    });

});