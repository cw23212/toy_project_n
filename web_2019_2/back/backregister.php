<?php
$str=$_POST['json'];
$ar = json_decode($str);
$class = $ar->class;
$ar = $ar->time;
$conn = mysqli_connect("127.0.0.1", "remote", "1111", "class");
$qu="select * from class where class =\"" . $class ."\"" ;
$res = mysqli_query($conn, $qu);
$sh = mysqli_fetch_row($res);
for($i=0;$i<26;$i++){
    if($ar[$i]=="1"&&$sh[$i+1]=="1"){
        $logfp=fopen("../log/reglog.txt","a");
        fwrite($logfp, Date("c") . " json: " . json_encode($ar) . " ip:" . $_SERVER['REMOTE_ADDR'] . " succes: fail\n");
        fclose($logfp);
        echo('<script>alert("error");window.location.href=document.referrer;</script>');
        return -1;
    }
}
$qur="";
$flg=-1;
for ($i = 18; $i < 26 + 18; $i++) {
    if($ar[$i-18]=="0")
        continue;
    if ($i % 2 != 0) {
        $tim = (string) (int) ($i / 2);
        $tim = "h" . (string) $tim . "_5";
    } else {
        $tim = (string) (int) ($i / 2);
        $tim = "h" . (string) $tim;
    }
    if ($flg != -1){
        $qur .= ",";
    }
    $flg=1;
    $qur .= $tim . "=" . $ar[$i-18];
}
//$qu ="select ". $qur." from " . $floor . " where class=" . $class;
/*$res = mysqli_query($conn, $qu);
$sh = mysqli_fetch_row($res);
for ($i = 0; $i < 24; $i++) {
    if ($ar[$i+1] == 1 && $sh[$i] == 1)
        echo ("error");
}*/
$qu="UPDATE class SET ".$qur." where class=\"".$class."\"";
$res = mysqli_query($conn, $qu);
$logfp=fopen("../log/reglog.txt","a");
fwrite($logfp,Date("c")." json: ".json_encode($ar)." ip:".$_SERVER['REMOTE_ADDR']." success: ".$res."\n");    
fclose($logfp);
echo('<script>alert("success");window.location.href=document.referrer;</script>');
?>
