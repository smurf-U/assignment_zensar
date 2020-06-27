$(document).ready(function(){
    $('input[type="radio"]').on('click', function(){
        console.info();
        if($(this).attr("value") == 'ip'){
            $('.search_by_host').hide();
            $('.search_by_ip').show();
        } else {
            $('.search_by_ip').hide();
            $('.search_by_host').show();
        }
    })


    $('.btn-search').on('click', function(e){
        var f_ipv4 = $('#f_ipv4').val();
        var t_ipv4 = $('#t_ipv4').val();
        if ((f_ipv4 != '' && t_ipv4 == '') || (f_ipv4 == '' && t_ipv4 != '')){
            alert("From IPv4 both To IPv4 required!")
        }
        var hostname = $('#hostname').val();

        var url = '/search_router/';
        console.info(f_ipv4, t_ipv4, hostname)
        fetch(url, {
            method: 'POST',
            headers: {
                'content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'hostname': hostname, 'f_ipv4': f_ipv4, 't_ipv4':t_ipv4})
        }).then((response) => {
            return response.json();
        }).then((datas) => {
            console.info(datas)
            template = ""
            if (datas.length > 0){
                $.each(datas, function(key,data){
                    template += '<tr><td>'+ data.sapid +'</td><td>'+ data.hostname +'</td><td>'+ data.loopback +'</td><td>'+ data.mac_address +'</td><td><a href="/detail/'+ data.id +'" class="btn btn-success">Details</a></td></tr>'
                });
            } else {
                template += "<tr><td colspan='4'>No data found</td></tr>"
            }
            $('tbody.table_data').html(template);
        });
    });
})