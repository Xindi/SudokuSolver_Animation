$(document).ready(function(){
    'use strict';
    $('.load').click(function(){   
        var val = $('.load').attr('id');
        $.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                var count = 1;
                $.each(data, function(key,value) {
                    if(value != '.'){
                        var header = '.cell' + count;
                        $(header).html(value);
                        $(header).addClass('ini');
                    }
                    count++;
                });
            },
        });
        return false;
    });


    $('.bf').click(function(){
        var val = $('.bf').attr('id');
        $.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                $.each(data, function(key,item) {

                    setTimeout(function(){ 
                        
                        var count = 1;
                        $.each(item, function(key,value) {
                            if(value != '.'){
                                var header = '.cell' + count;
                                $(header).html(value);
                            }
                            count++;                    
                        });

                    },500);
                    
                });
            },
        });
        return false;
    });

    $('.sa').click(function(){
        var val = $('.sa').attr('id');
        $.ajax({
            type: 'POST',
            data: {'action' : val},
            success: function(data) {
                $.each(data, function(key,item) {
                    
                    setTimeout(function(){ 
                        
                        var count = 1;
                        $.each(item, function(key,value) {
                            if(value != '.'){
                                var header = '.cell' + count;
                                $(header).html(value);
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