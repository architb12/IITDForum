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
$(document).on("click",".see-more",function(){
    var id;            
    id = $(this).attr("data-catid");
    $("#post-text-sliced"+id).hide();
    $("#post-text-full"+id).show();
    var see_more_div = document.getElementById("see-more"+id);
    see_more_div.textContent=""
    var see_less_div = document.getElementById("see-less"+id);
    see_less_div.textContent="See less"
});

$(document).on("click",".see-less",function(){
    var id;            
    id = $(this).attr("data-catid");
    $("#post-text-sliced"+id).show();
    $("#post-text-full"+id).hide();
    var see_more_div = document.getElementById("see-more"+id);
    see_more_div.textContent="See more"
    var see_less_div = document.getElementById("see-less"+id);
    see_less_div.textContent=""
});