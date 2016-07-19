/**
 * Created by ethan on 3/23/15.
 */
var my_form = document.forms.ContactUs;
var btnSubmit = document.getElementById('btnSubmit');
var linkRetry = document.getElementById('tryAgain');

linkRetry.addEventListener('click', function(evt) {
    document.body.removeClassName("success");
    evt.preventDefault();
    return false;
}, false);

btnSubmit.addEventListener('click', validateThenSubmit, false);

function validateThenSubmit(evt) {
    var targetForm = evt.target.form;
    var isValid = true;
    targetForm.resetErrorState();

    evt.preventDefault();

    isValid = readForms(targetForm);

    if (isValid) {
        sendRequest(JSON.stringify(isValid));
        // targetForm.submit()
    }
}



function readForms(in_form) {

    var my_result = {};
    var my_els = in_form.elements;

    if (in_form.checkValidity() !== true) {
        return false;
    }

    if (checkValid(my_els.email, "^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-z]+$") === false) {
        return false;
    }

    if (checkValid(my_els.message, "^([a-zA-Z$,' -]){6,}$") === false) {
        return false;
    }


    my_result.name = my_els.name.value;
    my_result.email = my_els.email.value;
    my_result.phone = my_els.phone.value;
    my_result.status = my_els.status.value;
    if (my_els.newsletter.checked) {
        my_result.newsletter = "on";
    }
    my_result.type = my_els.type.value;
    my_result.message = my_els.message.value;

    console.log(my_result.name);
    console.log(my_result.email);
    console.log(my_result.phone);
    console.log(my_result.status);
    //console.log(my_result.newsletter);
    console.log(my_result.type);
    console.log(my_result.message);


    return my_result;
}

function sendRequest(content) {
    var req = new XMLHttpRequest();
    req.open("POST", "http://wirehopper.net/ajax-submit.php", true);
    req.setRequestHeader("Content-Type", "application/json;charset=UTF-8;");
    req.addEventListener("load", function (evt) {
        var resp = JSON.parse(req.responseText);
        if (req.status !== 200 || resp['status'] === "error") {
            var errorBanner = document.getElementById("cu-SubmissionError");
            errorBanner.addClassName("error");
        }
        else {
            document.body.addClassName("success");
        }
        console.log("Done:", req.status);
        console.log(req.responseText);
    });
    req.send(content);
}