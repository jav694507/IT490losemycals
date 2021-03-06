#!/usr/bin/php
<?php
$mydb = new mysqli('192.168.56.101','testUser','12345','testdb');

if ($mydb->errno != 0)
{
	echo "failed to connect to database: ". $mydb->error . PHP_EOL;
	exit(0);
}

echo "successfully connected to databse".PHP_EOL;

$query = "INSERT INTO Userinfo(LastName,FirstName,passw,DOB,Username,email) VALUES('lol','lol','lolipi','2012/08/08','lols1','lol@gmail.com')";

$response = $mydb->query($query);
if($mydb->errno != 0)
{
	echo "failed to execute query:".PHP_EOL;
	echo __FILE__.':'.__LINE__.":error: ".$mydb->error.PHP_EOL;
	exit(0);
}
/*
$numrows = mysqli_num_rows($response);

echo "we got $numrows from the query".PHP_EOL;

while ($row = $response->fetch_row())
{
	print_r($row);
}
*/
echo "test complete".PHP_EOL;
?>
