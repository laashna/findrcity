!function(o){"use strict";o('a.js-scroll-trigger[href*="#"]:not([href="#"])').click((function(){if(location.pathname.replace(/^\//,"")==this.pathname.replace(/^\//,"")&&location.hostname==this.hostname){var a=o(this.hash);if((a=a.length?a:o("[name="+this.hash.slice(1)+"]")).length)return o("html, body").animate({scrollTop:a.offset().top-71},1e3,"easeInOutExpo"),!1}})),o(document).scroll((function(){o(this).scrollTop()>100?o(".scroll-to-top").fadeIn():o(".scroll-to-top").fadeOut()})),o(".js-scroll-trigger").click((function(){o(".navbar-collapse").collapse("hide")})),o("body").scrollspy({target:"#mainNav",offset:80});var a=function(){o("#mainNav").offset().top>100?o("#mainNav").addClass("navbar-shrink"):o("#mainNav").removeClass("navbar-shrink")};a(),o(window).scroll(a),o((function(){o("body").on("input propertychange",".floating-label-form-group",(function(a){o(this).toggleClass("floating-label-form-group-with-value",!!o(a.target).val())})).on("focus",".floating-label-form-group",(function(){o(this).addClass("floating-label-form-group-with-focus")})).on("blur",".floating-label-form-group",(function(){o(this).removeClass("floating-label-form-group-with-focus")}))}));var t=L.map("city-map").setView([39.381266,-97.922211],3);L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",{attribution:'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',maxZoom:18,id:"mapbox/streets-v11",tileSize:512,zoomOffset:-1,accessToken:"pk.eyJ1IjoiYWFzaG5hbGFraG5pIiwiYSI6ImNrODlsMzNxMDAwNDgza2wyMG4xYWs2Z3cifQ.WqySAawN-Nk0wnzKu7Unfw"}).addTo(t)}(jQuery);