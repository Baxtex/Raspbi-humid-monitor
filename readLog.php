<?php
class readLog{
	function getLog(){
		header('Content-Type: application/json');
		//$file = file_get_contents('../../../home/shares/flower_hum/humid.log');
		$file = file_get_contents('humid.log');
		$lengthOfFile = strlen($file)-2;
		$subFile = substr($file, 0, $lengthOfFile);
		$res ="[";
		$res .= $subFile;
		$res .="]";
		echo $res;
	}
}
?>