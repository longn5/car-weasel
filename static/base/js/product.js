$(document).ready(function(){
    $('#navlink-about').on('click', function(){
        location.href = "/about";
    });

    $('#navlink-home').on('click', function(){
        location.href = "/";
    });

    $('#navlink-contact').on('click', function(){
        location.href = "/contact";
    });

    $('#navlink-tryit').on('click', function(){
        location.href = "/tryit";
    });

    $('#navlink-register').on('click', function(){
        location.href = "/register";
    });

    $('#navlink-sellerlogin').on('click', function(){
        location.href = "/login/seller";
    });

    $('#navlink-buyerlogin').on('click', function(){
        location.href = "/login/buyer";
    });
});