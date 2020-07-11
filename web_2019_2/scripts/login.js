window.addEventListener("load", function(){
    let inputs = document.querySelectorAll(".login");
    let button = document.querySelector(".login_button");

    for(let input of inputs){
        input.addEventListener("focus", inputFocus);
        input.addEventListener("focusout", inputFocusout);
    }

    button.addEventListener("click", checkValidity);
});

function inputFocus(event){
    let inputBox = event.target.parentElement;

    inputBox.style.border = "1px solid #900";
}

function inputFocusout(event){
    let inputBox = event.target.parentElement;

    inputBox.style.border = "1px solid #F2F2F2";
}

function checkValidity(event){
    let formBox = event.target.parentElement;
    let idInput = formBox.querySelector("input[name = 'userid']");
    let pwInput = formBox.querySelector("input[name = 'password']");
    let onlyNumPattern = /^[0-9]+$/g;

    if((onlyNumPattern.exec(idInput.value) != null && idInput.value.length == 8) && pwInput.value.length > 0){
       formBox.submit();
    }
    else alert("Invalid ID or PW");
}