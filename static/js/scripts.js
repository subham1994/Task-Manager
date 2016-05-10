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

    // function to get a csrfTokenVal to be passed into the headers
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    // opens the modal pop up window
    function openModal(modalSelector) {
        $(modalSelector).openModal({
		    dismissible: false, // Modal can be dismissed by clicking outside of the modal
		    opacity: .7, // Opacity of modal background
		    in_duration: 400, // Transition in duration
		    out_duration: 300, // Transition out duration
    	});
    }

    function makeAjaxRequest(url, type, data, dataType, async, csrftoken, success_callback) {
		$.ajax({
	        url: url,
	        type: type,
	        data: data || null,
	        dataType: dataType,
	        async: async,
	        success: function (response) {
	            success_callback(response);
	        },
         	headers: {
                'X-CSRFToken': csrftoken
            }
		});
    }

    function doCommonPostWork(response, selector) {
    	var msg = JSON.parse(response);
    	if (msg.error) {
    		var errorArea = $(selector);
    		errorArea.html('')
    		$.each(msg.error, function(errName, description) {
    			errorArea.append(
    				'<p style="color: #b71c1c" class="news-title">\
    				 <i class="ion-close-circled"></i> ' + errName + ': ' + description[0] + '</p>'
    			);
    		});
    	} else {
    		window.location.href = msg.redirect_to;      
    	}
    }
		      
    // load add to-do form to modal dynamically
    $("a.fixed-element").click(function (event) {
    	event.preventDefault();
    	openModal('#modal1');
    	makeAjaxRequest('/add_todo/', 'get', {}, 'html', true, null, function(response) {
    		$('.modal-content').html(response);
    		post_todo_form();
    	});
    });
    
    // post the form data
    function post_todo_form() {
    	$("#add_todo_form").submit(function (event) {
    		event.preventDefault();
    		var data = { title: $("#id_title").val(), desc: $("#id_desc").val() }
    		makeAjaxRequest('/add_todo/', 'post', data, null, true, csrftoken, function(response) {
    			doCommonPostWork(response, '.error-area');
		});
	});
    	
    }
    
    // load edit to-do form to modal dynamically
    $(".edit-todo").click(function (event) {
    	event.preventDefault();
    	var todo_id = $(this).data("id");
        openModal('#modal1');
        makeAjaxRequest('/edit_todo/', 'get', {id: todo_id}, 'html', true, null, function(response) {
        	$('.modal-content').html(response);
        	edit_todo_form(todo_id);
        });
    });

    // post the form data
    function edit_todo_form(todo_id) {
    	$("#edit_todo_form").submit(function (event) {
    		event.preventDefault();
    		var data = { id: todo_id, title: $("#id_title").val(), desc: $("#id_desc").val() }
    		makeAjaxRequest('/edit_todo/', 'post', data, null, true, csrftoken, function(response) {
    			doCommonPostWork(response, '.error-area');
    		});
    	});
    }


});
