
def form_page():
  """Form credenziali di accesso """
  html = """<!DOCTYPE html>
<html>
  <head>
    <title>Casetta della Buonanotte</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <style>
      html, body {
      display: flex;
      justify-content: center;
      font-family: Roboto, Arial, sans-serif;
      font-size: 15px;
      }
      form {
      border: 5px solid #f1f1f1;
      }
      input[type=text], input[type=password] {
      width: 100%;
      padding: 16px 8px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
      }
      button {
      background-color: #8ebf42;
      color: white;
      padding: 14px 0;
      margin: 10px 0;
      border: none;
      cursor: grabbing;
      width: 100%;
      }
      h1 {
      text-align:center;
      fone-size:18;
      }
      button:hover {
      opacity: 0.8;
      }
      .formcontainer {
      text-align: left;
      margin: 24px 50px 12px;
      }
      .container {
      padding: 16px 0;
      text-align:left;
      }
      span.psw {
      float: right;
      padding-top: 0;
      padding-right: 15px;
      }
      /* Change styles for span on extra small screens */
      @media screen and (max-width: 300px) {
      span.psw {
      display: block;
      float: none;
      }
    </style>
  </head>
  <body>
    <form action="/action_page.php">
      <h1>scrivi qui le Credenziali del Router</h1>
      <div class="formcontainer">
      <hr/>
      <div class="container">
        <label for="uname"><strong>Utente</strong></label>
        <input type="text" placeholder="Enter Utente" name="uname" required>
        <label for="psw"><strong>Password</strong></label>
        <input type="password" placeholder="Enter Password" name="psw" required>
      </div>
      <button type="submit">Salva</button>
      <div class="container" style="background-color: #eee">
        
      </div>
    </form>
  </body>
</html>"""
  return html
  
def menu():
    """Menu di scelta"""
    html = """<!DOCTYPE html>
<html>
  <head>
    <title>Casetta della Buonanotte</title>
    <style>
      html, body {
      display: flex;
      justify-content: center;
      font-family: Roboto, Arial, sans-serif;
      font-size: 15px;
      }
      form {
      border: 5px solid #f1f1f1;
      }
      input[type=text], input[type=password] {
      width: 100%;
      padding: 16px 8px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
      }
      button {
      background-color: #8ebf42;
      color: white;
      padding: 14px 0;
      margin: 10px 0;
      border: none;
      cursor: grabbing;
      width: 100%;
      }
      h1 {
      text-align:center;
      fone-size:18;
      }
      button:hover {
      opacity: 0.8;
      }
      .formcontainer {
      text-align: left;
      margin: 24px 50px 12px;
      }
      .container {
      padding: 16px 0;
      text-align:left;
      }
      span.psw {
      float: right;
      padding-top: 0;
      padding-right: 15px;
      }
      /* Change styles for span on extra small screens */
      @media screen and (max-width: 300px) {
      span.psw {
      display: block;
      float: none;
      }
    </style>
  </head>
  <body>
    <h2>Cosa Puoi Fare?</h2><br>
    <br>
    <br>
    <div class="container">
    <p>
    <a href="/">Questo Menu</a><br>
    <a href="/pagina_form.php">Cambia impostazioni Router</a><br>
    <a href="/mod_colore.php">Modifica il colore della Lampada</a><br>
    </p>
    </div>
    <div class="container" style="background-color: #eee"> </div>
  </body>
</html> """
    return html
    
def mod_colore():
    """Pagina web per il form di scelta dei colori della lampada principale - serve solo in AP mode """
    html = """<!DOCTYPE html>
<html>
  <head>
    <title>Casetta della Buonanotte</title>
  </head>
  <body>
    <form action="/color_page.php">
      <h1>Modifica qui il colore delle lamapde</h1>
      <div class="formcontainer">
      <hr/>
      <div class="container">
        <label for="nrosso"><strong>Rosso</strong></label>
        <input type="text" placeholder="da 0 a 255" name="nrosso" required>
        <label for="nverde"><strong>Verde</strong></label>
        <input type="text" placeholder="da 0 a 255" name="nverde" required>
        <label for="nblu"><strong>Blu</strong></label>
        <input type="text" placeholder="da 0 a 255" name="nblu" required>
      </div>
      <button type="submit">Salva</button>
    <br>
    <br>
    <a href="/">Menu Pricipale</a>
  </body>
</html> """
    return html
    
def registrato():
    """Pagina di cortesia che avverte la corretta conclusione della registrazione dei dati di configurazione """
    html = """<!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <h1>Registrato Credenziali nuovo Router - Grazie</h1>
        <br>
        <br>
        <h3>Adesso mi resetto - puoi tornare all tua normale connessione WiFi</h3>
        </body>
        </html> """
    return html
