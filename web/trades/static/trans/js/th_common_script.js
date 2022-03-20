var $ = jQuery.noConflict();
var template_directory_uri = object_name.templateUrl;
var cart_listing_url = object_name.cartListing;
var cart_checkout_url = object_name.cartCheckout;

jQuery(document).ready(function( $ ) {

    /*if ( typeof(Storage) !== 'undefined' && !localStorage.getItem('activeToggle') ) {
     var this_ = localStorage.getItem('activeToggle');
     $(this_).removeClass('th_theme_switch').siblings().addClass('th_theme_switch');
     localStorage.setItem('activeToggle', '');
     }*/


    $('#th_newsletter_btn').on('click', function(){


        var mailchimp_nonce = object_name.mailchimp_nonce;
        var email = $('#th_newsletter_subscriber').val();
        var fname = '';
        var lname = '';
        if(email ==''){
            $('#th_subscriber_status').css('color','red');
            $('#th_subscriber_status').html('Please enter a email address.');
        }else {

            if(isValidEmail(email)) {

                $.ajax({
                    type: "POST",
                    dataType: "json",
                    url: AJAX_URI,
                    data: {
                        email: email,
                        fname : fname,
                        lname : lname,
                        security: mailchimp_nonce,
                        action : 'th_newsletter_subscriber'
                    },
                    success: function (result) {
                        if (result.status == 'success') {
                            $('#th_newsletter_subscriber').val('');
                            $('#th_subscriber_status').css('color','green');
                            $('#th_subscriber_status').html(result.msg);
                            //$('#th_subscriber_status').delay(3000).fadeOut('slow');
                        } else {
                            $('#th_subscriber_status').css('color','red');
                            $('#th_subscriber_status').html(result.msg);
                        }

                    }//success
                });//ajax
            }else{
                $('#th_subscriber_status').css('color','red');
                $('#th_subscriber_status').html('Please enter a valid email address.');
            }

        }


    });

    $(document).on('click','.bucket-common-btn', function () {


        var post_id = $(this).attr('data-post_id');
        var post_selector = $("button[data-post_id='" + post_id +"']");

        //if bucket is completed then redirect
        var state_completed = $(this).hasClass('bucket-state-completed');
        if(state_completed==true){
            window.location.href = ""+cart_listing_url+"";
            return false;
        }

        $(post_selector).html('Processing');
        $(post_selector).attr("disabled", "disabled");
        $(post_selector).addClass('bucket-state-processing');

        $.ajax({
            type:"POST",
            dataType : "json",
            url: AJAX_URI,
            data : {
                post_id 	  : post_id,
                custom_action : 'add',
                action        : 'add_to_bucket'
            },
            success: function(data){
                if(data.status == 'added'){
                    $(".notification-bucket").html(data.count_item);
                    $(".summary-campaigns").html(data.count_item);
                    console.log('Item Added Successfully.');
                }else if(data.status == 'duplicate'){
                    console.log('Item Already Added.');
                }
                $(post_selector).removeAttr("disabled");
                $(post_selector).html('Check Out');
                $(post_selector).removeClass('bucket-state-processing');
                $(post_selector).addClass('bucket-state-completed');
            }//success
            ,
            error: function (response) {
                $(post_selector).removeAttr("disabled");
                $(post_selector).html('Donate Now');
                $(post_selector).removeClass('bucket-state-processing');
            }
        });//ajax


    });


    $('#th_currency_switch').flagStrap({
        countries: {
            "PK": "PAK (PKR)",
            "US": "USD ($)",
            "GB": "POUND (£)"
        },
        onSelect: function(country, element){
           if(country=='') {
                var country = 'PK';
            }
            $('#theme_switch_loading').show();
            $.ajax({
                type:"POST",
                url: AJAX_URI,
                data : {
                    country : country,
                    action : 'th_currency_switch'
                },
                success: function(result){
                    location.reload();
                },
                error: function(result){
                    $('#theme_switch_loading').hide();
                }//success
            });//ajax
        },
        selectedCountry: th_active_country,
        buttonSize: "btn-sm",
        buttonType: "btn-default",
        labelMargin: "10px",
        scrollable: false,
        scrollableHeight: "350px",
        placeholder: false,
    });


});// ready

jQuery(window).on('load', function() {
    //change iframe source
    //document.getElementById("ChildiframeID").src = "https://www.viralentertainmentguru.com/?embediframe=true";

});

// Email validation
function isValidEmail(emailText) {
    var pattern = new RegExp(/^[\w-]+(\.[\w-]+)*@([a-z0-9-]+(\.[a-z0-9-]+)*?\.[a-z]{2,6}|(\d{1,3}\.){3}\d{1,3})(:\d{4})?$/);
    return pattern.test(emailText);
};

function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}


