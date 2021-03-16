#!/usr/bin/php
<?php

//rabbitmq library and database connection 
require_once('path.inc');
require_once('get_host_info.inc');
require_once('rabbitMQLib.inc');
require_once('dbconnect.php');

//verifies the login for user in db
function doLogin($email,$passw)
{
$mydb = dbconnect();

//create query to check if client exists in db
$query_login = "Select * from Userinfo where email = '$email' and passw = '$passw'";
$response = $mydb->query($query_login);
if (!$response) //($mydb->errno != 0)
{
        echo "failed to execute query:".PHP_EOL;
        echo __FILE__.':'.__LINE__.':error:'.$mydb->error.PHP_EOL;
        exit(0);
}
//check if the record exists in db
$num_rows = mysqli_num_rows($response);
if ($num_rows > 0){
//echo "user exists";
return true;
}
else
{
//echo 'user does not exist';
return false;
}
}

//creates a new user 
function newUser($lname, $fname, $passw, $dob, $email)
{
$mydb = dbconnect();
//switch date format so it can match db requirements
$dob_format = str_replace('/','-',$dob);
$dob_new = date('Y-m-d',strtotime($dob_format));

$query_register = "insert into Userinfo(LastName, FirstName, passw, DOB, email) values('$lname','$fname','$passw','$dob_new','$email')";

$response = $mydb->query($query_register);
if($mydb->errno != 0)
{
	echo "failed to execute the register query:".PHP_EOL;
	echo __FILE__.':'.__LINE__.':error:'.$mydb->error.PHP_EOL;
	exit(0);
}
else
{
return true;
echo "new user registered";
}
}

function requestProcessor($request)
{
  echo "received request".PHP_EOL;
  var_dump($request);
  if(!isset($request['type']))
  {
    return "ERROR: unsupported message type";
  }
  switch ($request['type'])
  {
    case "login":
      $msg = doLogin($request['email'],$request['passw']);
      break;
    case "validate_session":
      return doValidate($request['sessionId']);
    case "register":
      return newUser($request['LastName'],$request['FirstName'],$request['passw'],$request['DOB'],$request['email']);
  }
echo $msg;
return $msg;
 //return array("returnCode" => '0', 'message'=>"Server received request and processed");
}

$server = new rabbitMQServer("testRabbitMQ.ini","testServer");

echo "Database BEGIN".PHP_EOL;
$server->process_requests('requestProcessor');
echo "Database END".PHP_EOL;
exit();
?>

