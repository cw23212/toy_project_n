<?php
$conn=mysqli_connect("127.0.0.1","remote","1111","class");
if(!$conn){
    die("sql error");
}
$user=$_POST['userid'];
$pass=$_POST['password'];
$qu="select ind from user where id=".$user." AND passwd=".$pass;
$res=mysqli_query($conn,$qu);
$sh=mysqli_fetch_array($res);
if(!isset($sh)){
    $logfp=fopen("log/faillog.txt","a");
    fwrite($logfp,Date("c")." id:".$user." passwd:".$pass." ip:".$_SERVER['REMOTE_ADDR']."\n");    
    fclose($logfp);
    echo("<script>alert(\"incorrect Id or passwd\");
     window.location.href=\"login.html\";</script>");
}
else{
    $logfp=fopen("log/log.txt","a");
    fwrite($logfp,Date("c")." id:".$user." ip:".$_SERVER['REMOTE_ADDR']."\n");    
    fclose($logfp);
    setcookie("index",$sh['ind']);
    header("Location:floor.html");
}
?>
