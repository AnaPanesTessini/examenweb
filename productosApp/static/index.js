

document.addEventListener("DOMContentLoaded", function() {
    var lazyloadImages = document.querySelectorAll(".lazy-load");
  
    function lazyLoad() {
      lazyloadImages.forEach(function(img) {
        if (img.getBoundingClientRect().top
         <= window.innerHeight && img.getBoundingClientRect().bottom 
         >= 0 && getComputedStyle(img).display != "none") 
         {
          img.src = img.getAttribute("data-src");
          img.classList.remove("lazy-load");
        }
      });
    }
  
    lazyLoad();
    window.addEventListener("scroll", lazyLoad);
    window.addEventListener("resize", lazyLoad);
  
    console.log("El DOM ha sido cargado completamente.");
  
    document.body.style.backgroundColor = "#ffc7c7";
  });
  