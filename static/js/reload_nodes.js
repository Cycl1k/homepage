setInterval(function(){$.ajax({
    url: '/update',
    type: 'POST',
    success: function(response) {
        for (let i=0; i<=response[-1]; i++){
            console.log('time' + i, response[i]["node_uptime"]);
            $("#node_uptime"+i).html(response[i]["node_uptime"]); 
            $("#node_core_load"+i).html(response[i]["node_core_load"]); 
            $("#node_core"+i).html(response[i]["node_core"]); 
            $("#node_ram_moment"+i).html(response[i]["node_ram_moment"]); 
            $("#node_ram_total"+i).html(response[i]["node_ram_total"]); 
            $("#node_os_disk_total"+i).html(response[i]["node_os_disk_total"]); 
            $("#node_os_disk_moment"+i).html(response[i]["node_os_disk_moment"]); 
            $("#node_status"+i).html(response[i]["node_status"]); 
        }
    },
    error: function(error) {
        console.log(error);
    }
})}, 800);

setTimeout(function(){

    location.reload();

}, 10000);