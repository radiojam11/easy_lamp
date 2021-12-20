<?php
// Questo file viene richiamato ogni accenzione della Lampada principale, nel caso non  esista la cartella relativa al mac address della Lampada.
$chiave_stabilita = 'XXXXXXXXX';
	$api_key = "";
//  
// prendo il parametro macadd dalla get fatta dall'ESP32  e la APIKEY e costruisco la cartella
$macadd = $_GET["macadd"];
$api_key = $_GET["api_key"];
// mi prendo anche la variabile conf se esite!, altrimenti uso la configurazione di base : - ogni mac contiene ['mac', [colori], 'status', 'numero figli', 'numero_LED']
if(isset($_GET['conf'])) {
    $conf = $_GET["conf"];
}else {
	$conf = "{'conf': [['$macadd', [255, 255, 255], '0', '0', '8' ]]}";	
}

// Creo la struttura della directory -  siamo dentro casette, quindi parto da qui .
$struttura = './'. $macadd;
// se la apikey e giusta, creo la struttura, e ci creo dentro il file di configurazione
if ($api_key == $chiave_stabilita ) {
    if (!mkdir($struttura, 0755, false)) {
        die('La Lampada era già registrata sul server');
	}else {
			$fh = fopen($struttura ."/config.txt", 'w+') or die("can't open file");
			fwrite($fh, $conf);
			fclose($fh);
	
		echo "FATTO!";
    }
	
} else {
	echo "API_KEY non valida!";
}


// ...
?>
