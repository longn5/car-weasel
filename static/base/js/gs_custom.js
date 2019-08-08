$(document).ready(function(){
    $('#buyer_login_button').on('click', function(){
        location.href = "/buyer";
    });

    $('#seller_login_button').on('click', function(){
        location.href = "/seller";
    });

    $('#login_portal_button').on('click', function(){
        location.href = "/login";
    });

    $('#signup_button').on('click', function(){
        location.href = "/sign-up";
    });

    $('#what_link').on('click', function(){
        location.href = "/#what";
    });

    $('#how_link').on('click', function(){
        location.href = "/#how";
    });

    $('#contact_link').on('click', function(){
        location.href = "/#contact";
    });
    
});