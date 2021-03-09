<?php 

session_start();
require_once('rabbitMQLib.inc');


//declare variables
$cals = $_REQUEST['bfastcals'];
$food = $_REQUEST['food'];
$email = $_SESSION['email']

//make ourselves a new client for rabbitmq
$client = new rabbitMQClient('testRabbitMQ.ini','testServer');

//create the request
$request = array();
$request['cals'] = $cals;
$request['food'] = $food;
$request['email']= $email;
$response = $client->send_request($request);
$_SESSION['response'] = $response;

header('Location: http://www.losemycalories.com/mealselection.html');
exit();
?>
