<?php
class readLog{
	function getLog(){
		header('Content-Type: application/json');
	
		$file = file_get_contents('humid.txt');
		$lengthOfFile = strlen($file)-2;
		$subFile = substr($file, 0, $lengthOfFile);
		$res ="[";
		$res .= $subFile;
		$res .="]";
		echo $res;
	}
}
?>