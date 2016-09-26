<?php
	function clean($string){
		return json_decode(rtrim(trim($string),','),true);
	}

	function getLog(){
		$logLines = file('../../../home/shares/flower_hum/humid.log');
		$entries = array_map("clean",$logLines);
		$finalOutput = ['log'  => $entries];
		$json = json_encode($finalOutput);
		return $json;
	}
?>

<html>
	<head>
		<script src="script.js" type="text/javascript"></script>
		<script src="sorttable.js" type="text/javascript"></script>
		<link rel="stylesheet" type="text/css" href="style.css">
		<meta charset="UTF-8">
		<title>Antgus</title>
	</head>
	<body>
		<h2>Humidity and temperature log</h2>
		<button type="button" onclick='createTable(<?php echo getLog(); ?>)'>Generate log</button>
		<br><br>
		<div id="logDiv"></div>
	</body>
</html>
