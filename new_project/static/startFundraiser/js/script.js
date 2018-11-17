
 // $('h1').slideUp(1000).slideDown(1000);
 // $('#main').css({
 //    color: 'red',
 //    fontSize: 25
 // });


// $('p').click(function() {
//     $(this).hide();
// })

 // Preloader
 $(window).on('load', function() {
     $('#status').fadeOut();
     $('#preloader').delay(350).fadeOut('slow');
 }); //anonymous function