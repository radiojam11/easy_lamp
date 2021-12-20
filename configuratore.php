<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Casetta Buonanotte - Configuratore - Invio i dati</title>
</head>
<body>

Benvenuto <?php echo $_GET["name"]; ?><br>
Il MAC Address della Lampada da configurare è: <?php echo $_GET["macadd"]; ?>

<form action="registra_mio_mac.php" method="get" name="datiUtenti">
<h1>Casetta Buonanotte - Configuratore</h1>
<h3>Scegli il colore della tua Lampada Principale  </h3>
<h4>Valori da 0 (nessun colore) a 255 (massima concentrazione di colore) 
rispettivamente per Rosso Verde Blue  </h4>
Esempio: </br>
- Se tutto a 0 la Lampada (quando verra' accesa) rimarra' buia. 
- Se tutto a 255 la Lampada (quando verra' accesa) fara' luce bianca (somma dei colori) alla sua massima potenza.</br>
- Se Rosso 255 Verde 0 Blue 0 - Quando la Lampada verra' accesa fara' una luce Rossa alla sua massima potenza. (0-255-0 Luce Verde -- 0-0-255 Luce Blue)</br>
- Se Rosso 195 Verde 125 Blue 0 - Quando la Lampada verra' accesa fara' una luce Giallo Oro.</br>
Puoi scegliere qualsiasi combinazione di colore per contrassegnare le tue Lampade Collegate.</br>
Puoi cambiare i colori quante volte vuoi sempre da questa schermata.</br>

<h3 style="color: red">***scorri la pagina e premi il tasto "invio" quando terminato***</h3>
<h1>Lampada Principale</h1>
<?php // $_GET["macadd"]; ?>
Il Mac della Lampada principale non va modificato - se non è corretto c'è qualcosa che non funziona - forse è stato scritto male nella Form della Pagina Precedente</br>
Mac Lamapada Principale: <input type="text" maxlength=2 minlength=2 name="macadd_1" value=<?php echo substr($_GET["macadd"],0,2); ?> /> - <input type="text" maxlength=2 minlength=2 name="macadd_2" value=<?php echo substr($_GET["macadd"],3,2);?> /> - <input type="text" maxlength=2 minlength=2 name="macadd_3" value=<?php echo substr($_GET["macadd"],6,2);?> /> - <input type="text" maxlength=2 minlength=2 name="macadd_4" value=<?php echo substr($_GET["macadd"],9,2);?> /> - <input type="text" maxlength=2 minlength=2 name="macadd_5" value=<?php echo substr($_GET["macadd"],12,2);?> /> - <input type="text" maxlength=2 minlength=2 name="macadd_6" value=<?php echo substr($_GET["macadd"],15,2); ?> /></br>
Scegli il Colore : Rosso <input type="text" name="r_lamp" value=255 /> - Verde <input type="text" name="v_lamp" value=255 /> - Blue <input type="text" name="b_lamp" value=255 /></br>
</br>
Quante Lampade Collegate alla Principale hai? : <select name="num_fg">
<option value="0" selected="selected">0</option>
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5">5</option>
</option>
</select>
</br>
<h1>Lampade Collegate</h1>
<h3>Inserisci i dati delle tue Lampade Collegate</h3>
</br>
<h4>Prima Lampada Collegata</h4>
Mac Prima Lamapada Collegata: <input type="text" maxlength=2 minlength=2 name="mac1_1" /> - <input type="text" maxlength=2 minlength=2 name="mac1_2" /> - <input type="text" maxlength=2 minlength=2 name="mac1_3" /> - <input type="text" maxlength=2 minlength=2 name="mac1_4" /> - <input type="text" maxlength=2 minlength=2 name="mac1_5" /> - <input type="text" maxlength=2 minlength=2 name="mac1_6" /></br>

Scegli il Colore : Rosso <input type="text" maxlength=3 name="r_fg1" /> - Verde <input type="text" maxlength=3 name="v_fg1" /> - Blue <input type="text" maxlength=3 name="b_fg1" /></br>
</br>
<h4>Seconda Lampada Collegata</h4>
Mac Seconda Lamapada Collegata: <input type="text" maxlength=2 minlength=2 name="mac2_1" /> - <input type="text" maxlength=2 minlength=2 name="mac2_2" /> - <input type="text" maxlength=2 minlength=2 name="mac2_3" /> - <input type="text" maxlength=2 minlength=2 name="mac2_4" /> - <input type="text" maxlength=2 minlength=2 name="mac2_5" /> - <input type="text" maxlength=2 minlength=2 name="mac2_6" /></br>

Scegli il Colore : Rosso <input type="text" maxlength=3 name="r_fg2" /> - Verde <input type="text" maxlength=3 name="v_fg2" /> - Blue <input type="text" maxlength=3 name="b_fg2" /></br>
</br>
<h4>Terza Lampada Collegata</h4>
Mac Terza Lamapada Collegata: <input type="text" maxlength=2 minlength=2 name="mac3_1" /> - <input type="text" maxlength=2 minlength=2 name="mac3_2" /> - <input type="text" maxlength=2 minlength=2 name="mac3_3" /> - <input type="text" maxlength=2 minlength=2 name="mac3_4" /> - <input type="text" maxlength=2 minlength=2 name="mac3_5" /> - <input type="text" maxlength=2 minlength=2 name="mac3_6" /></br>

Scegli il Colore : Rosso <input type="text" maxlength=3 name="r_fg3" /> - Verde <input type="text" maxlength=3 name="v_fg3" /> - Blue <input type="text" maxlength=3 name="b_fg3" /></br>
</br>
<h4>Quarta Lampada Collegata</h4>
Mac Quarta Lamapada Collegata: <input type="text" maxlength=2 minlength=2 name="mac4_1" /> - <input type="text" maxlength=2 minlength=2 name="mac4_2" /> - <input type="text" maxlength=2 minlength=2 name="mac4_3" /> - <input type="text" maxlength=2 minlength=2 name="mac4_4" /> - <input type="text" maxlength=2 minlength=2 name="mac4_5" /> - <input type="text" maxlength=2 minlength=2 name="mac4_6" /></br>

Scegli il Colore : Rosso <input type="text" maxlength=3 name="r_fg4" /> - Verde <input type="text" maxlength=3 name="v_fg4" /> - Blue <input type="text" maxlength=3 name="b_fg4" /></br>
</br>
<h4>Quinta Lampada Collegata</h4>
Mac Quinta Lamapada Collegata: <input type="text" maxlength=2 minlength=2 name="mac5_1" /> - <input type="text" maxlength=2 minlength=2 name="mac5_2" /> - <input type="text" maxlength=2 minlength=2 name="mac5_3" /> - <input type="text" maxlength=2 minlength=2 name="mac5_4" /> - <input type="text" maxlength=2 minlength=2 name="mac5_5" /> - <input type="text" maxlength=2 minlength=2 name="mac5_6" /></br>

Scegli il Colore : Rosso <input type="text" maxlength=3 name="r_fg5" /> - Verde <input type="text" maxlength=3 name="v_fg5" /> - Blue <input type="text" maxlength=3 name="b_fg5" /></br>
</br>
<input type="submit" />
</form>
</body>
</html>
