function verifynewuser()
{
//text data of new user
var fname = document.getElementById('fname').value;
var lname = document.getElementById('lname').value;
var dob = document.getElementById('dob').value;
var email = document.getElementById('email').value;
var passw = document.getElementById('passw').value;
var passwc = document.getElementById('passwc').value;
var length = 5;
var bool = "true";


//password check for function
//var numbers = /^[0-9]+$/;
checkdob = /^([0-9]{2})\/([0-9]{2})\/([0-9]{4})$/;
re = /[0-9]/;
cre = /[A-Z]/;
//lre = /[a-z]/;
echeck = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/; 



//check for first name validation 
if(fname == "")
{
document.getElementById('req').style.visibility = "visible";
bool = "false";
}



//last name validation
if(lname === "")
{
document.getElementById('req1').style.visibility = "visible";
bool = "false";
}
else
{
document.getElementById('req1').style.visibility = "hidden";
}



//date of birth validation
if(dob === "")
{
document.getElementById('req2').style.visibility = "visible";
bool = "false";
}
else if(!checkdob.test(dob))
{
document.getElementById('req2').style.visibility = "visible";
bool = "false";
}


//email validation 
if(!echeck.test(email))
{
document.getElementById('req4').style.visibility = "visible";
bool = "false";
}
else 
{
document.getElementById('req4').style.visibility = "hidden";
}


//password validation
if(passw === "")
{
document.getElementById('req5').style.visibility = "visible";
bool = "false";
}
else if(!re.test(passw) || !cre.test(passw))
{
document.getElementById('req5').style.visibility = "visible";
bool = "false";
}
else if(passw.length <= length)
{
document.getElementById('req5').style.visibility = "visible";
bool = "false";
}
else if(passwc != passw)
{
document.getElementById('req6').style.visibility = "visible";
bool = "false"
}
else
{
document.getElementById('req5').style.visibility = "hidden";
document.getElementById('req6').style.visibility = "visible";
}

//check if form is ready to send
if (bool == "false")
{
alert("Some input needs to be fixed");
return false;
}
else
{
alert("Form Sent");
window.location.href = "useq2.html";
return true;
}
//else{
//alert("Password matches");
//return true;
//}
}
