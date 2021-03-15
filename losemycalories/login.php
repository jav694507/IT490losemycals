#!/usr/bin/php
<?php
//registration info to pass on with a session 

session_start();

//need this library for methods
require_once('rabbitMQLib.inc');

//make ourselves a new client 
$client = new rabbitMQClient('testRabbitMQ.ini','testServer');

//get the variables we need to pass 


//give the session the email value to pass it onto the next page
$_SESSION['email'] = $_REQUEST['email'];
//pass the data to rabbit queue
$request = array();
$request['type'] = 'login'; 
$request['passw'] = $_REQUEST['passw'];
$request['email'] = $_REQUEST['email'];
$response = $client->send_request($request);

if($response == 1)
{
header('Location: http://www.losemycalories.com/userpage.html');
exit();
}
else 
{
header('Location: http://www.losemycalories.com/index.html');
}
/*
if ($response == 1)
{
//redirects after sending info to rabbitmq
header('Location: http://www.losemycalories.com/userpage.html');
}
else
{
exit('Account does not exist');
return false;
}
*/
?>
