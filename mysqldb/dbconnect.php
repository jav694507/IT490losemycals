<?php 
//make the db connection variables
function dbconnect(){
$hostip = '10.192.234.66';
$user = 'jackroot';
$passw = 'jav69';
$db = 'losemycals';


//start the connection
$mydb = new mysqli($hostip, $user, $passw, $db);


//reports error if not connected
if($mydb->errno != 0)
{

	echo "failed to connect to database: ". $mydb->error.PHP_EOL;
	echo __FILE__.':'.__LINE__.':error:'.$mydb->error.PHP_EOL;
	exit(0);
}

echo "Connected to databse losemycals".PHP_EOL;
return $mydb;
} 
?>
