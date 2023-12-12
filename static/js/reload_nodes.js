setInterval(function(){$.ajax({
    url: '/update',
    type: 'POST',
    success: function(response) {
        for (let i=0; i<=response[-1]; i++){
            console.log('time' + i, response[i]["node_uptime"]);
            $("#time"+i).html(response[i]["node_uptime"]); 
        }
    },
    error: function(error) {
        console.log(error);
    }
})}, 800);

setTimeout(function(){

    location.reload();

}, 1000);