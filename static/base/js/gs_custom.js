$(document).ready(function(){
    $('#buyer_login_button').on('click', function(){
        location.href = "/login/buyer";
    });

    $('#seller_login_button').on('click', function(){
        location.href = "/login/seller";
    });

    $('#login_portal_button').on('click', function(){
        location.href = "/login";
    });
});