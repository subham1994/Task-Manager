$(document).ready(function(){
	// set the height of cards to equal lengths
	function equalizeCardHeights() {
		var maxHeight    = 0;
	    var cardContents = $(".card .card-content");
	    cardContents.each(function(){
	        if ($(this).height() > maxHeight) { maxHeight = $(this).height(); }
	    });
	    cardContents.height(maxHeight);
	}

	equalizeCardHeights();

	// sidebar
	$('.button-collapse').sideNav({
	    closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
	  }
	);
	      

});