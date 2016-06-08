ping_app = function(appId){

    var getQuery = {
        "url": "/ping",
        "data":{
            "appId": appId
        }
    }

    var update = function(response, app){

        row = $("#" + app)

        code = response.code
        status = "success"
        if (code != 200)
            status = "danger"


        row.children(".status").html('<span class="label label-'+ status +'">'+ code +'</span>')
    }

    var foo = function(){

        var id = appId

        var always = function(response){
            update(response, id)
        }

        var then = function(){
            setTimeout(foo, 5000)
        }

        $.get(getQuery)
            .always(always)
            .then(then)

    }

    foo()
}