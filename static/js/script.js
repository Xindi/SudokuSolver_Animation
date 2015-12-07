jQuery(document).ready(function(){
    'use strict';
    jQuery('.load').click(function(){   
        var val = jQuery(this).attr('id');

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
        var val = jQuery(this).attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            url: '/test',
            dataType: 'json',
            success: function(data) {
                var c = 0;
                jQuery.each(data, function(key,item) { 
                    c++;
                    var count = 1;
                    setInterval(function(){
                    jQuery.each(item, function(key,value) { 
                        for(var i in value){
                            if(value[i] != '.'){
                                addToDom(value[i], count);
                            }
                            else{
                                addToDom('', count);
                            }
                            count++;
                        } 
                    });
                    }, 100*c);
                });
                
            },
        });
        return false;
    });

    jQuery('.sa').click(function(){
        var val = jQuery(this).attr('id');
        jQuery.ajax({
            type: 'POST',
            data: {'action' : val},
            url: '/test',
            dataType:'json',
            success: function(data) {
                var c = 0;
                jQuery.each(data, function(key,item) { 
                    c++;
                    var count = 1;
                    setInterval(function(){
                    jQuery.each(item, function(key,value) { 
                        for(var i in value){
                            if(value[i] != '.'){
                                addToDom(value[i], count);
                            }
                            else{
                                addToDom('', count);
                            }
                            count++;
                        } 
                    });
                    }, 100*c);
                });
            },
        });
        return false;
    });
});