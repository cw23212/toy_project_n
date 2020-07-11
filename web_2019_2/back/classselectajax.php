<?php
$con=mysqli_connect('127.0.0.1','remote','1111','class');
if(!$con){
die("eoor");}
$class=$_POST['class'];
//$class="B101";
$sql='select * from class where class = "'.$class.'"';
$res=mysqli_query($con,$sql);
 $res=mysqli_fetch_row($res);
echo(json_encode($res));
?>