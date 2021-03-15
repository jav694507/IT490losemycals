<?php
//registration info to pass on with a session 

session_start();

//need this library for methods
require_once('rabbitMQLib.inc');

//make ourselves a new client 
$client = new rabbitMQClient('testRabbitMQ.ini','testServer');

//get the variables we need

$fname = $_REQUEST['fname'];
$lname = $_REQUEST['lname'];
$dob =  $_REQUEST['dob'];
$dob_new = str_replace('/','-',$dob);
$dob_fr = date('Y-m-d', strtotime($dob_new));
$passw = $_REQUEST['passw'];
$email = $_REQUEST['email'];

//give the session the email value to pass it onto the next page
$_SESSION['email'] = $email;
//pass the data to rabbit queue
$request = array();
$request['type'] = 'register';
$request['LastName'] = $lname;
$request['FirstName'] = $fname;
$request['passw'] = $passw;
$request['DOB'] = $dob_fr;
$request['email'] = $email;
//$response = $client->send_request($request);
$response = $client->publish($request);

//redirects after sending info to rabbitmq
header('Location: http://www.losemycalories.com/useq2.html');
exit();
?>

