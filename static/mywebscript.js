
let performVison = ()=>{

    imagetocheck = document.getElementById("imagetocheck").value;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("Result").innerHTML = xhttp.responseText;
        }
    };
     xhttp.open("GET", "checking?imagetocheck"+"="+imagetocheck, true);
   xhttp.send();
}