<?php

$chiave_stabilita = 'XXXXXXXX';
	$api_key = "";
//  
// prendo il parametro macadd dalla get fatta dall'ESP32  e la APIKEY e costruisco la cartella
$macadd = $_GET["macadd"];
$api_key = $_GET["api_key"];
// mi prendo anche la variabile conf se esite!, altrimenti uso la configurazione di base : - ogni mac contiene ['mac', [colori], 'status', 'numero figli', 'numero_LED']
if(isset($_GET['conf'])) {
    $conf = $_GET["conf"];
}else {
	$conf = "{'conf': [['$macadd', [255, 255, 255], '0', '0', '10']]}";	
}

// Creo la struttura della directory -  siamo dentro casette, quindi parto da qui .
$struttura = './'. $macadd;
// se la apikey e giusta, creo la struttura, e ci creo dentro il file di configurazione
if ($api_key == $chiave_stabilita ) {
    if (!mkdir($struttura, 0755, false)) {
        die('Failed to create directories...');
	}else {
			$fh = fopen($struttura ."/config.txt", 'w+') or die("can't open file");
			fwrite($fh, $conf);
			fclose($fh);
	
		echo "FATTO!";
    }
	
} else {
	echo "API_KEY non valida!";
}
// puo sempre servire!
// Here comes the added chmod:
// chmod($myFile, 0755);
// ...
?>
