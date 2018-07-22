define(function(){

    function load_ipython_extension(){
        console.info('this is the abc extension');
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
