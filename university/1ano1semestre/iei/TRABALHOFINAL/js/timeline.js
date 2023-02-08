
// function to toggle the visibility of the timeline-content element
function showContent(header) {
    var content = header.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  }
  
  // Get all the timeline-header elements
  var headers = document.getElementsByClassName("timeline-header");
  
  // loop through the headers and add the click event listener
  for (var i = 0; i < headers.length; i++) {
    headers[i].addEventListener("click", function() {
      showContent(this);
    });
  }
  
  // hide all the timeline-content elements by default
  var contents = document.getElementsByClassName("timeline-content");
  for (var i = 0; i < contents.length; i++) {
    contents[i].style.display = "none";
  }
  