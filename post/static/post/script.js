//Loader Fade out
$(document).ready(function(){
  $(".loader").delay(500).fadeOut();
});

//Changing Navbar on scrolling
$(window).on("scroll", function() {
  if($(window).scrollTop()) {
        $('.navbar').addClass('nav-scroll');
        $('.navbar').removeClass('nav-top');
  }

  else {
        $('.navbar').removeClass('nav-scroll');
        $('.navbar').addClass('nav-top');
  }
})

//Smooth Scroll
$(function() {
    $('a[href*=#]:not([href=#])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html,body').animate({
            scrollTop: target.offset().top
          }, 1000);
          return false;
        }
      }
    });
  });

//Changing Collapse Button
$(document).ready(function(){

    $("#collapse-btn").click(function(){
  
      if($("#navicon").hasClass("fa-bars")){
        $("#navicon").removeClass("fa-bars");
        $("#navicon").addClass("fa-times");
      }
      else if($("#navicon").hasClass("fa-times")){
        $("#navicon").removeClass("fa-times");
        $("#navicon").addClass("fa-bars");
      }
  
    });
  
  });

  //Tooltips
  $(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
  });