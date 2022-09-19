/*Start Admin Login*/
$(document).ready(function(e) {
    $('#adminLogin').on('submit', (function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: 'includes/auth.php',
            data: formData,
            cache: false,
            dataType: 'json',
            contentType: false,
            processData: false,
            beforeSend: function() {
              $(".submitButton").html("Validating...");
              $(".submitButton").attr('disabled', 'disabled');
            },
            success: function(data) {
                console.log(data);
                if (data.response.code == '1') {
                    $(".submitButton").html("Redirecting...");
                    $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    })
                    setTimeout(function() {
                        window.location = data.response.url;
                    }, 2000);
                }
                if (data.response.code == '0') {
                    $(".submitButton").html("SIGN IN");
                    $(".submitButton").removeAttr('disabled');
                    $.toast({
                        heading: "Oh Snap!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#bf441d;",
                        icon: "error",
                        hideAfter: 3e3,
                        stack: 1
                    })
                }
            },
            error: function(data) {
                console.log("error");
                console.log(data);
            }
        });
    }));
});
/*End Admin Login*/

/*Start Country To State Fetch*/

$(".country").change(function(event) {
    var countryName=$(this).val();
    $.ajax({
        url: 'includes/auth.php',
        type: 'POST',
        dataType: 'html',
        data: {countryName:countryName},
    })
    .done(function(data) {
        $("#state").html(data);
        $("#city").html('<select class="form-control show-tick city" name="city" required autocomplete="off"><option value="">Select City</option></select>');
        //console.log(data);
    });
});

/*End Country To State Fetch*/

/*Start State To City Fetch*/

$("body").on("change",".state",function(event) {
    var stateName=$(this).val();
    $.ajax({
        url: 'includes/auth.php',
        type: 'POST',
        dataType: 'html',
        data: {stateName:stateName},
    })
    .done(function(data) {
        $("#city").html(data);
        //console.log(data);
    });
});

/*End State To City Fetch*/

/*Start Change All Status in One Php And Ajax*/
$("body").on("click",".changeStatus",function() {
    var token = $(this).data("token");
    var tablename = $(this).data("tablename");
    var statusChange = 'statusChange';
    $.ajax({
        url: 'includes/auth.php',
        type: 'POST',
        dataType: 'json',
        data: {statusChange: statusChange,token:token,tablename:tablename},
    })
    .done(function(data) {
        if (data.response.code == '1') {
            if (data.response.status == '1') {
                $(".changeStatus" + token).html('<i class="material-icons effectStatus">thumb_up</i>');
            }
            if (data.response.status == '0') {
                $(".changeStatus" + token).html('<i class="material-icons effectStatus">thumb_down</i>');
            }
        }
        if (data.response.code == '0') {
            $.toast({
                heading: "Oh Snap!",
                showHideTransition: "slide",
                text: data.response.msg,
                position: "top-right",
                loaderBg: "#bf441d;",
                icon: "error",
                hideAfter: 3e3,
                stack: 1
            })
        }
    })
    .fail(function() {
        //console.log("error");
        //console.log(data);
    })
});
/*End Change All Status in One Php And Ajax*/


/*Start Delete Row In Table in One Php And Ajax*/
$("body").on("click",".deleteRow",function() {
    var token = $(this).data("token");
    var tablename = $(this).data("tablename");
    var deleteRow = 'deleteRow';
swal({
        title: "Are you sure?",
        text: "Want to Delete this Thing!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((willDelete) => {
        if (willDelete) {
            $.ajax({
                url: 'includes/auth.php',
                type: 'POST',
                dataType: 'json',
                data: {deleteRow: deleteRow,token:token,tablename:tablename},
            })
            .done(function(data) {
                console.log(data);
                if (data.response.code == '1') {
                    $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    })
                    $(".hidediv" + token).hide("slow");
                }
                if (data.response.code == '0') {
                    $.toast({
                        heading: "Oh Snap!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#bf441d",
                        icon: "error",
                        hideAfter: 3e3,
                        stack: 1
                    })
                }
            })
            .fail(function(data){
                console.log("error");
                console.log(data);
            })
    } else {
         $.toast({
                heading: "Oh Snap!",
                showHideTransition: "slide",
                text: "Your Imaginary File is Safe!",
                position: "top-right",
                loaderBg: "#bf441d",
                icon: "error",
                hideAfter: 3e3,
                stack: 1
            })
        }
    });
});
/*End Delete Row In Table in One Php And Ajax*/

/*Start Add freelancer*/
$(document).ready(function(e) {
    $('#freelancersignup').on('submit', (function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: 'includes/auth.php',
            data: formData,
            cache: false,
            dataType: 'json',
            contentType: false,
            processData: false,
            beforeSend: function() {
              $(".submitButton").html("Validating...");
              $(".submitButton").attr('disabled', 'disabled');
              $(".page-loader-wrapper").css('display','block');
            },
            success: function(data) {
                //console.log(data);
                if (data.response.code == '1') {
                    $(".submitButton").html("Redirecting...");
                    $(".page-loader-wrapper").css('display','none');
                    $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    })
                    setTimeout(function() {
                        window.location = data.response.url;
                    }, 2000);
                }
                if (data.response.code == '0') {
                    $(".submitButton").html("Submit");
                    $(".submitButton").removeAttr('disabled');
                    $.toast({
                        heading: "Oh Snap!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#bf441d;",
                        icon: "error",
                        hideAfter: 3e3,
                        stack: 1
                    })
                }
            },
            error: function(data) {
                //console.log("error");
                //console.log(data);
            }
        });
    }));
});
/*End Add freelancer*/

/*Start freelancer Login*/
$(document).ready(function(e) {
    $('#freelancerLogin').on('submit', (function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            type: 'POST',
            url: 'includes/auth.php',
            data: formData,
            cache: false,
            dataType: 'json',
            contentType: false,
            processData: false,
            beforeSend: function() {
              $(".submitButton").html("Validating...");
              $(".submitButton").attr('disabled', 'disabled');
            },
            success: function(data) {
                console.log(data);
                if (data.response.code == '1') {
                    $(".submitButton").html("Redirecting...");
                    $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    })
                    setTimeout(function() {
                        window.location = "my-projects.php";
                    }, 2000);
                }
                if (data.response.code == '0') {
                    $(".submitButton").html("SIGN IN");
                    $(".submitButton").removeAttr('disabled');
                    $.toast({
                        heading: "Oh Snap!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#bf441d;",
                        icon: "error",
                        hideAfter: 3e3,
                        stack: 1
                    })
                }
            },
            error: function(data) {
                console.log("error");
                console.log(data);
            }
        });
    }));
});
/*End freelancer Login*/


/*Start contact us */

 $(document).ready(function(){
       $("#contact_page").submit(function(e){
       e.preventDefault();
        var formData = new FormData(this);
        $.ajax({
          url :'includes/auth.php',
          type :'POST',
            data : formData,
            cache: false,
            dataType: 'json',
            contentType: false,
            processData: false,
             beforeSend: function() {
              $(".getSubmitButton").html("Validating...");
              $(".getSubmitButton").attr('disabled', 'disabled');
            },

              success:function(data){
                console.log(data);
              if(data.response.code == '1')
              {
                 $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    });
                 
                    setTimeout(function() {
                        window.location = "contact-us.php";
                    }, 2000);

              }
              if(data.response.code == '0')
              {
                 $.toast({
                        heading: "warning!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "warning",
                        hideAfter: 3e3,
                        stack: 1
                    });

              }
              
          },
              error:function(data) {
                console.log("error");
                console.log(data);
            }
         
         
          });
            
    });

});
 /*End contact Login*/


/*Start business inquire */

       $(document).ready(function(){
       $("#business_inquiry").submit(function(e){
  e.preventDefault();
  var formData = new FormData(this);
        $.ajax({
          url :'includes/auth.php',
          type :'POST',
            data : formData,
            cache: false,
            dataType: 'json',
            contentType: false,
            processData: false,
             beforeSend: function() {
              $(".getSubmitButton").html("Validating...");
              $(".getSubmitButton").attr('disabled', 'disabled');
            },

              success:function(data){
                console.log(data);
              if(data.response.code == '1')
              {
                 $.toast({
                        heading: "Success!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "success",
                        hideAfter: 3e3,
                        stack: 1
                    });
                 
                    setTimeout(function() {
                        window.location = "business_inquire.php";
                    }, 2000);

              }
              if(data.response.code == '0')
              {
                 $.toast({
                        heading: "warning!",
                        showHideTransition: "slide",
                        text: data.response.msg,
                        position: "top-right",
                        loaderBg: "#5ba035",
                        icon: "warning",
                        hideAfter: 3e3,
                        stack: 1
                    });

              }
              
          },
              error:function(data) {
                console.log("error");
                console.log(data);
            }
         
         
          });
            
    });

});
       /*End business inqueries*/