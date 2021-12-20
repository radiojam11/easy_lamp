<?php
// configuratoreBE.php
// Questo file viene richiamato da configuratore.php per registrare le scelte di configurazione operate dall'utente sul server cloud
$chiave_stabilita = 'XXXXXXXXXXXXXXXXXXXXX';
	$api_key = "";
	
$macadd = $_GET["macadd"];
$api_key = $_GET["api_key"];

$macadd_1 = $_GET["macadd_1"];
$macadd_2 = $_GET["macadd_2"];
$macadd_3 = $_GET["macadd_3"];
$macadd_4 = $_GET["macadd_4"];
$macadd_5 = $_GET["macadd_5"];
$macadd_6 = $_GET["macadd_6"];

$r_lamp = $_GET["r_lamp"];
$v_lamp = $_GET["v_lamp"];
$b_lamp = $_GET["b_lamp"];

$num_fg = $_GET["num_fg"];

$mac1_1 = $_GET["mac1_1"];
$mac1_2 = $_GET["mac1_2"];
$mac1_3 = $_GET["mac1_3"];
$mac1_4 = $_GET["mac1_4"];
$mac1_5 = $_GET["mac1_5"];
$mac1_6 = $_GET["mac1_6"];

$r_fg1 = $_GET["r_fg1"];
$v_fg1 = $_GET["v_fg1"];
$b_fg1 = $_GET["b_fg1"];


$mac2_1 = $_GET["mac2_1"];
$mac2_2 = $_GET["mac2_2"];
$mac2_3 = $_GET["mac2_3"];
$mac2_4 = $_GET["mac2_4"];
$mac2_5 = $_GET["mac2_5"];
$mac2_6 = $_GET["mac2_6"];

$r_fg2 = $_GET["r_fg2"];
$v_fg2 = $_GET["v_fg2"];
$b_fg2 = $_GET["b_fg2"];

$mac3_1 = $_GET["mac3_1"];
$mac3_2 = $_GET["mac3_2"];
$mac3_3 = $_GET["mac3_3"];
$mac3_4 = $_GET["mac3_4"];
$mac3_5 = $_GET["mac3_5"];
$mac3_6 = $_GET["mac3_6"];

$r_fg3 = $_GET["r_fg3"];
$v_fg3 = $_GET["v_fg3"];
$b_fg3 = $_GET["b_fg3"];


$mac4_1 = $_GET["mac4_1"];
$mac4_2 = $_GET["mac4_2"];
$mac4_3 = $_GET["mac4_3"];
$mac4_4 = $_GET["mac4_4"];
$mac4_5 = $_GET["mac4_5"];
$mac4_6 = $_GET["mac4_6"];

$r_fg4 = $_GET["r_fg4"];
$v_fg4 = $_GET["v_fg4"];
$b_fg4 = $_GET["b_fg4"];

$mac5_1 = $_GET["mac5_1"];
$mac5_2 = $_GET["mac5_2"];
$mac5_3 = $_GET["mac5_3"];
$mac5_4 = $_GET["mac5_4"];
$mac5_5 = $_GET["mac5_5"];
$mac5_6 = $_GET["mac5_6"];

$r_fg5 = $_GET["r_fg5"];
$v_fg5 = $_GET["v_fg5"];
$b_fg5 = $_GET["b_fg5"];

$mac6_1 = $_GET["mac6_1"];
$mac6_2 = $_GET["mac6_2"];
$mac6_3 = $_GET["mac6_3"];
$mac6_4 = $_GET["mac6_4"];
$mac6_5 = $_GET["mac6_5"];
$mac6_6 = $_GET["mac6_6"];

$r_fg6 = $_GET["r_fg6"];
$v_fg6 = $_GET["v_fg6"];
$b_fg6 = $_GET["b_fg6"];

$macadd = $macadd_1 . ":" . $macadd_2 . ":" . $macadd_3 . ":" . $macadd_4 . ":" . $macadd_5 . ":" . $macadd_6;
$mac1 = $mac1_1 . ":" . $mac1_2 . ":" . $mac1_3 . ":" . $mac1_4 . ":" . $mac1_5 . ":" . $mac1_6;
$mac2 = $mac2_1 . ":" . $mac2_2 . ":" . $mac2_3 . ":" . $mac2_4 . ":" . $mac2_5 . ":" . $mac2_6;
$mac3 = $mac3_1 . ":" . $mac3_2 . ":" . $mac3_3 . ":" . $mac3_4 . ":" . $mac3_5 . ":" . $mac3_6;
$mac4 = $mac4_1 . ":" . $mac4_2 . ":" . $mac4_3 . ":" . $mac4_4 . ":" . $mac4_5 . ":" . $mac4_6;
$mac5 = $mac5_1 . ":" . $mac5_2 . ":" . $mac5_3 . ":" . $mac5_4 . ":" . $mac5_5 . ":" . $mac5_6;

$color_lamp = $r_lamp . ":" . $v_lamp . ":" . $b_lamp;

$color_fg1 = $r_fg1 . ":" . $v_fg1 . ":" . $b_fg1;
$color_fg2 = $r_fg2 . ":" . $v_fg2 . ":" . $b_fg2;
$color_fg3 = $r_fg3 . ":" . $v_fg3 . ":" . $b_fg3;
$color_fg4 = $r_fg4 . ":" . $v_fg4 . ":" . $b_fg4;
$color_fg5 = $r_fg5 . ":" . $v_fg5 . ":" . $b_fg5;

