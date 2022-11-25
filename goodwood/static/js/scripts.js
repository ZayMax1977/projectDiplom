document.addEventListener("DOMContentLoaded", cleaner_checkbox_reg);
document.addEventListener("DOMContentLoaded", cleaner_checkbox_log);
 // ---------------обнуление check-box на регистрации при перезагрузке страницы---------------
function cleaner_checkbox_reg() {

    var checkBox_ag = document.getElementById('reg_check');
    var button_reg = document.getElementById('button_reg');

    if (checkBox_ag.checked = true) {
        checkBox_ag.checked = false;

        }
    if (button_reg.hidden = true) {
        checkBox_ag.checked = false;

        }
    button_reg.hidden = true;

  }
// ---------------появление и изчезание кнопки регистрации,----------------------
//----------------при нажатии на checkbox(ознакомление с парвилами)  при регистрации---------------

function reg_button_hidden() {
    var button_reg = document.getElementById('button_reg');
    var reg_check = document.getElementById('reg_check');

    if (button_reg.hidden == true){
        button_reg.hidden = false;
    }
    else{
        button_reg.hidden = true;
        }
}
// ---------------появление и изчезание  полей: ввода логина, ввода телефона; кнопки----------------------
//----------------востановления пароля при нажатии на checkbox(восстановить пароль)---------------

 function recover_password() {
    var phone_for_recover = document.getElementById('phone_for_recover1');
    var phone_for_recover = document.getElementById('phone_for_recover2');

    if (phone_for_recover1.hidden == true)  {
            phone_for_recover1.hidden = false;
    }
    if (phone_for_recover2.hidden == true)  {
       phone_for_recover2.hidden = false;
    }

    else{
        phone_for_recover1.hidden = true;
        phone_for_recover2.hidden = true;


        }
}

 //---------------обнуление check-box на входе  при перезагрузке страницы---------------

function cleaner_checkbox_log() {

    var phone_for_recover = document.getElementById('phone_for_recover');
    var check_recover = document.getElementById('check_recover');

    if (check_recover.checked = true) {
        check_recover.checked = false;

        }
    if (phone_for_recover.hidden = true) {
        check_recover.checked = false;

        }
    phone_for_recover.hidden = true;

  }