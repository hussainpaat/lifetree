
function forform(form, msg){
    let er = form.find('.error');
    let scs = form.find('.success');
    er.html("");
    scs.html("");
    let btn = true;
    form.find('[vali="yes"]').each(function(){
        if($(this).val() == ""){
            $(this).css("border" ,"1px solid red");
            btn = false;
            er.html("Please fill the form");
        }
        else{
            $(this).css("border" ,"1px solid #ccc");
        }
    });
    if(btn == true)
    {
        let url = form.attr("data");
        let fbtn = form.find('button');
        fbtn.attr("disabled", true);
        fbtn.html("PleaseWait...");
        $.post(url, form.find(":input").serializeArray(),
            function (data) {
                console.log(data)
                fbtn.attr("disabled", false);
                fbtn.html("Send Message");
                // if(data == "done"){
                // }
                // else{
                //     er.html(data);
                // }
            }
        );
    }
}

$(document).ready(function () {
    var url = window.location.pathname;
    var filename = url.substring(url.lastIndexOf('/')+1);
    if(filename == ""){filename = "Lifetree-Healthcare-And-Diagnostics";}
    var ul = $('.nav li a[href="/'+filename+'"]');   
    ul.parent().addClass('active');

    // let get = $(window).width();
    // if(get < 600)
    //     $('.leftMob').addClass('service-block-two');

    $(window).load(function() {
        var hash = location.hash.replace(/^#/, '');
        if(hash)
            history.replaceState(null, null, ' ');
    });
    $(window).on('hashchange', function (e) {
        var hash = location.hash.replace(/^#/, '');
        if (hash == '')
            $('#AppointMent').hide();
        else
            $('#'+hash).show();
    });
    $('.close').click(function(){
        window.history.back();
    });
    $('.formSubmi').submit(function(){
        let msg = $(this).attr("sus");
        forform($(this), msg);
        return false;
    });
});