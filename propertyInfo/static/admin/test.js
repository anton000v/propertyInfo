window.onload = function(){
 var main1 = document.querySelector('#MAIN1');

  var onchanged = function(){
    var this_ = this;
    var value = this_.value;
    var main2 = document.querySelector("#MAIN2");
    var alloption = main2.querySelectorAll('optgroup[label*="PRODUCT"]')
    var getByLabel = main2.querySelector('[label="'+value+'"]');

    alloption.forEach(function(element){
     element.style.display = "none";
    });

    getByLabel.style.display = "block";

  };

 main1.onchange = onchanged;

};

// Jquery Version.

/*
$(document).ready(function(){
  $('#MAIN1').on('change',function(){
    var this_ = $(this);
    var value = this_.val();
    var main2 = $("#MAIN2");
    var alloption = main2.find('optgroup[label*="PRODUCT"]')
    var getByLabel = main2.find('[label="'+value+'"]');

    alloption.hide()
    getByLabel.show()

  });
});

*/