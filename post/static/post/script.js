//Loader Fade out
$(document).ready(function(){
  $(".loader").fadeOut();
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

  //See more and See less functionality
  $(".see-more").click(function(){
    var id;            
    id = $(this).attr("data-catid");
    $("#post-text-sliced"+id).hide();
    $("#post-text-full"+id).show();
    var see_more_div = document.getElementById("see-more"+id);
    see_more_div.textContent=""
    var see_less_div = document.getElementById("see-less"+id);
    see_less_div.textContent="See less"
});

$(".see-less").click(function(){
    var id;            
    id = $(this).attr("data-catid");
    $("#post-text-sliced"+id).show();
    $("#post-text-full"+id).hide();
    var see_more_div = document.getElementById("see-more"+id);
    see_more_div.textContent="See more"
    var see_less_div = document.getElementById("see-less"+id);
    see_less_div.textContent=""
});

//Search bar functionality
function searchBar(obj){
  if(obj.value.length==0){
      $("#search-results").hide();
  }
  else $("#search-results").show();

  var search_text = obj.value
  $.ajax( 
  { 
      type:"GET", 
      url: "{% url 'users:search' %}", 
      data:{
          'search_text' : search_text
      },
      success: function(data){
          document.getElementById("search-results").innerHTML = data;
      }
  }) 

}