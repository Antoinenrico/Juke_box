

function send_Gcode_to_motor(sens){
    if(sens=="gauche"){

        let req = new XMLHttpRequest();
        req.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200) {
                console.log("ok send")
                let zone_text = document.getElementById("msg")
                zone_text.innerText=this.responseText
            } else if (this.readyState == 4) {
                console.log("Unable to fetch data... Error ", this.status);
            }
        }
        req.open('POST', '/API', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        req.send("sens=" + sens);
    }
}