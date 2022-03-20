jQuery(document).ready(function ($) {
    get_homepage_surgical_procedures(cat_surgical_procedures_slug);
    get_homepage_medical_procedures(cat_medical_procedures_slug);
	get_homepage_medicalcamps('upcoming');
	get_featured_medicalcamp('upcoming');
	get_homepage_running_campaigns(cat_surgical_procedures_slug);
	
});

function get_homepage_surgical_procedures(category){

    jQuery.post({
        url:AJAX_URI,
        type:'POST',
        data : {
            category : category,
            action  : 'get_campaigns_by_category'
        },
        success: function(response){
            jQuery('#surg-procedure').html(response);
        }
    });
}

function get_homepage_medical_procedures(category){
	
	jQuery.post({	
		url:AJAX_URI,
		type:'POST',
		data : {
			category : category,
			action  : 'get_campaigns_by_category'
		},
		success: function(response){
            jQuery('#medical-procedure').html(response);
		}
	});
}

function get_homepage_medicalcamps(category){
	
	jQuery.post({	
		url:AJAX_URI,
		type:'POST',
		data : {
			category : category,
			action  : 'get_homepage_medicalcamps'
		},
		success: function(response){
			jQuery('#med-camps').html(response);
		}
	});
}

function get_featured_medicalcamp(category){
	
	jQuery.post({	
		url:AJAX_URI,
		type:'POST',
		data : {
			category : category,
			action  : 'get_featured_medicalcamp'
		},
		success: function(response){
			jQuery('#upcoming-medical-camp').html(response);
		}
	});
}

function get_homepage_running_campaigns(category){
	
	jQuery.post({	
		url:AJAX_URI,
		type:'POST',
		data : {
            category : category,
			action  : 'get_homepage_running_campaigns'
		},
		success: function(response){
			jQuery('#homepage-running-campaigns').html(response);
		}
	});
}

