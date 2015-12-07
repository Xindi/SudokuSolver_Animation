jQuery(document).ready(function(){
    'use strict';
    jQuery('.load').click(function(){   
        var val = jQuery('.load').attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            url: '/test',
            dataType: 'json',
            success: function(data) {
                var count = 1;
                jQuery.each(data, function(key,value) {
                    for(var i in value){
                        if(value[i] != '.'){
                            var header = '#cell' + count;
                            jQuery(header).html(value[i]);
                            jQuery(header).addClass('ini');
                        }
                        count++;
                    }
                });
            },
        });
        return false;
    });


    function addToDom(val, count){
        var header = '#cell' + count;
        jQuery(header).html(val);
    }

    jQuery('.bf').click(function(){
        var val = jQuery('.bf').attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            url: '/test',
            dataType: 'json',
            success: function(data) {
                jQuery.each(data, function(key,item) {    
                    var count = 1;
                    jQuery.each(item, function(key,value) {
                        for(var i in value){
                            if(val != '.'){
                                setTimeout(addToDom(value[i]), 200);
                            }
                            count++; 
                        }                   
                    });
                    
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
            url: '/test',
            dataType:'json',
            success: function(data) {
                jQuery.each(data, function(key,item) {
                   var count = 1;
                   jQuery.each(item, function(key,value) {
                        for(var i in value){
                            if(val != '.'){
                                setTimeout(addToDom(value[i]), 200);
                            }
                            count++; 
                        }                   
                    });
                });
            },
        });
        return false;
    });
});