<!DOCTYPE html>
<html>
<body>
<?php

//get the variables we need

$fname = $_REQUEST['fname'];
$lname = $_REQUEST['lname'];
$uname = $_REQUEST['uname'];
$dob =  $_REQUEST['dob'];
$dob_new = str_replace('/','-',$dob);
$dob_fr = date('Y-m-d', strtotime($dob_new));
$passw = $_REQUEST['passw'];
$email = $_REQUEST['email'];

//gets the sever data to use for connection 
$mydb = new mysqli('192.168.56.102','admin','admin','losemycals');

if ($mydb->errno != 0)
{
	echo "failed to connect to database: ". $mydb->error . PHP_EOL;
	exit(0);
}

echo "successfully connected to databse".PHP_EOL;

$query = "INSERT INTO Userinfo(LastName,FirstName,passw,DOB,Username,email) VALUES('$lname','$fname','$passw','$dob_fr','$uname','$email')";

$response = $mydb->query($query);
if($mydb->errno != 0)
{
	echo "failed to execute query:".PHP_EOL;
	echo __FILE__.':'.__LINE__.":error: ".$mydb->error.PHP_EOL;
	exit(0);
}
else
{
echo"success";
}


/*the queries we will need to pass to mysql

$uinfo = "INSERT INTO Userinfo(FirstName,LastName,passw,Username,email) VALUES ('$fname','$lname','$passw','$uname','$email')";
//$querycheck = "SELECT CONCAT(FirstName, '',LastName) AS User_Name,Password,DOB, Username, email FROM Userinfo"; 


//execute the query 
$result = mysqli_query($jdb, $uinfo);
if (!$result)
{
print "Error: the query could not be exectued" . mysqli_error();
exit;
}
else
{
echo "success"
}
*/
?>
</body>
</html>
