#!/usr/bin/php
<?php
require_once('path.inc');
require_once('get_host_info.inc');
require_once('rabbitMQLib.inc');

/*
function doLogin($username,$password)
{
    // lookup username in databas
    // check password
    return true;
    //return false if not valid
}

function requestProcessor($request)
{
  echo "received request".PHP_EOL;
  var_dump($request);
  {
    return "ERROR: unsupported message type";
  }
  switch ($request['type'])
  {
    case "login":
      return doLogin($request['username'],$request['password']);
    case "validate_session":
      return doValidate($request['sessionId']);
  }
  return array("returnCode" => '0', 'message'=>"Server received request and processed");
}
*/

//create function that sends over data 
function sendUser($request)
{
$lname = $request['LastName'];
$fname = $request['FirstName'];
$passw = $request['passw'];
$DOB = $request['DOB'];
$email = $request['email'];

$mydb = new mysqli('192.168.56.102','rabbitmqserver','rabbitmqserver','losemycals');

if ($mydb->errno != 0)
{
        echo 'failed to connect to Mysql'. $mydb->error . PHP_EOL;
        exit(0);
}
else
{
echo 'connected to db'.PHP_EOL;
}
$query = "insert into Userinfo(LastName, FirstName, passw, DOB, email) values('$lname', '$fname', '$passw', '$DOB', '$email')";
$response = $mydb->query($query);
if ($response->errno != 0)
{
	echo 'Failed to execute query'.PHP_EOL;
	echo __FILE__.':'.__LINE__.':error:'.$mydb->error.PHP_EOL;
	exit(0);
}
else 
{
echo 'it has made it';
}
}

//function to call api when registering new user
function dietRecommend($cals, $food, $email)
{

function requestProcessor($request)
{
  echo "received request".PHP_EOL;
  var_dump($request);
  {
    return "ERROR: unsupported message type";
  }
  switch ($request['type'])
  {
    case "register":
     return registerUser($request);
    case "newuserdiet":
      return dietRecommend($request['cals'],$request['food']);
  }
  return array("returnCode" => '0', 'message'=>"Server received request and pr>
}

//load up server
$server = new rabbitMQServer('testRabbitMQ.ini','testServer');

//connect to databse as rootuser
//$mydb = new mysqli('192.168.56.102','rabbitmqserver','rabbitmqserver','losemycals');
/*
if ($mydb->errno() != 0)
{
	echo 'failed to connect to Mysql'. $mydb->error . PHP_EOL;
	exit(0);
}
else
{
echo 'connected to db'.PHP_EOL;
}
 */
echo 'testRabbitMQServer BEGIN'.PHP_EOL;
$server->process_requests('processRequest');
echo 'testRabbitMQServer END'.PHP_EOL;
exit();
?>
