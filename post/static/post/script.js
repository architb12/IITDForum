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

  //Auto expanding textareas
  var autoExpand = function(field){
    field.style.height = 'inherit';
    var style = window.getComputedStyle(field);
    var height =  parseInt(style.getPropertyValue('border-top-width'),10)
                  + parseInt(style.getPropertyValue('padding-top'),10)
                  + field.scrollHeight
                  + parseInt(style.getPropertyValue('padding-bottom'),10)
                  + parseInt(style.getPropertyValue('border-bottom-width'),10);
    field.style.height = height + 'px';
  };

  //Event listener for textarea
  document.addEventListener('input', function(event){
    if(event.target.tagName.toLowerCase() !== 'textarea') return;
    autoExpand(event.target);
  },false);