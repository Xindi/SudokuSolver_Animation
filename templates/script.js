jQuery(document).ready(function(){
    'use strict';
    jQuery('.load').click(function(){   
        var val = jQuery('.load').attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                var count = 1;
                jQuery.each(data, function(key,value) {
                    if(value != '.'){
                        var header = '.cell' + count;
                        jQuery(header).html(value);
                        jQuery(header).addClass('ini');
                    }
                    count++;
                });
            },
        });
        return false;
    });


    jQuery('.bf').click(function(){
        var val = jQuery('.bf').attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                jQuery.each(data, function(key,item) {

                    setTimeout(function(){ 
                        
                        var count = 1;
                        jQuery.each(item, function(key,value) {
                            if(value != '.'){
                                var header = '.cell' + count;
                                jQuery(header).html(value);
                            }
                            count++;                    
                        });

                    },500);
                    
                });
            },
        });
        return false;
    });

    jQuery('.sa').click(function(){
        var val = jQuery('.sa').attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                jQuery.each(data, function(key,item) {
                    
                    setTimeout(function(){ 
                        
                        var count = 1;
                        jQuery.each(item, function(key,value) {
                            if(value != '.'){
                                var header = '.cell' + count;
                                jQuery(header).html(value);
                            }
                            count++;                    
                        });

                    },500);
                    
                });
            },
        });
        return false;
    });
});