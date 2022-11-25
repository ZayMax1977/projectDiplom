var myVar = setInterval(move_left, 4000);

function stop_start(){
        const btn = document.getElementById('cross');
        if(btn.innerHTML === 'X'){
                btn.innerHTML = '<';
                clearInterval(myVar);

        }
        else{
                btn.innerHTML = 'X';
                myVar = setInterval(move_left, 4000);

        }
}


var count = 0;
function move_left(){

        if (count <= 4){
                var foto_1 = document.getElementById('ff-1');
                foto_1.src = "/static/media/vip-adv/foto-" +(count + 2) + ".jpg";

                var foto_2 = document.getElementById('ff-2');
                foto_2.src = "/static/media/vip-adv/foto-" + (count + 3) + ".jpg";

                var foto_3 = document.getElementById('ff-3');
                foto_3.src = "/static/media/vip-adv/foto-" + (count + 4) + ".jpg";

                var foto_4 = document.getElementById('ff-4');
                foto_4.src = "/static/media/vip-adv/foto-" + (count + 5) + ".jpg";

                count += 1;
        }else{
                count = -1;
        }

}
