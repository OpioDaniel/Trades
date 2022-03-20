"use strict";
(function($){

    //--------check if ID exist - the proceed ---------//
    if ( $( "#homepage-running-campaigns__333" ).length ) {
        let owl = $('#homepage-running-campaigns');
        owl.owlCarousel({
            loop: false,
            margin: 20,
            nav: false,
            dots: true,
            responsive: {
                0: {
                    items: 1,
                    nav: false,
                    dots: true
                },
                768: {
                    items: 3,
                    nav: false,
                    dots: true
                },
                992: {
                    items: 3
                },
                1200: {
                    items: 3
                }
            }
        });

    }



    if ( $( "#homepage-testimonials" ).length ) {
        let owl3 = $('#homepage-testimonials');
        owl3.owlCarousel({
            margin: 20,
            nav: true,
            dots: false,
            autoplay: true,
            loop: true,
            responsive: {
                0: {
                    items: 1,
                    nav: false,
                    dots: true
                },
                768: {
                    items: 1,
                    nav: false,
                    dots: true
                },
                992: {
                    items: 1,
                    nav: false,
                    dots: true
                },
                1200: {
                    items: 1,
                    nav: false,
                    dots: true
                }
            }
        });
    }//if homepage-testimonials


    if ( $( "#carousel-payment" ).length ) {
        let owl = $('#carousel-payment');
        owl.owlCarousel({
            loop: false,
            margin: 40,
            nav: true,
            dots: false,
            responsive: {
                0: {
                    items: 2,
                    nav: false,
                    dots: true
                },
                768: {
                    items: 4,
                    nav: false,
                    dots: true
                },
                992: {
                    items: 4
                },
                1200: {
                    items: 5
                }
            }
        });
    }//if carousel-payment
})(jQuery);//ready state




	