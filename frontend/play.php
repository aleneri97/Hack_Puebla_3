<!DOCTYPE html>
<html lang="en">

<head>
  <!-- TODO: subir div.mood-->
  <!-- TODO: ponerle diferentes íconos a cada mood -->
  <!-- TODO: hacer texto mood más opaco -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">

  <title>T.Beat</title>

  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="css/main.css">

</head>

<body>
  <header>
    <h1>T·Beat</h1>
    <p>Lorem Ipsum Dolore</p>
  </header>
  <div class="main">
    <div class="box">
      <p class="text">¿Cómo te sientes?</p>
      <div class="mood-box">

        <form action="play.php" method="post">
          <label>
              <input type="radio" name="mood" value="" />
              <img src="images/happy.jpg">
          </label>

          <label>
            <input type="radio" name="mood" value="big"/>
            <img src="images/happy.jpg">
          </label>

          <label>
            <input id="" type="radio" name="mood" value="med" />
            <img src="images/happy.jpg">
          </label>

          <label>
            <input id="" type="radio" name="mood" value="long" />
            <img src="images/happy.jpg">
          </label>
          <label>
              <input type="radio" name="mood" value="small" />
              <img src="images/happy.jpg">
          </label>

          <label>
            <input type="radio" name="mood" value="big"/>
            <img src="images/happy.jpg">
          </label>
          <textarea placeholder="Escribe tu canción..." name="" id="" cols="20" rows="3"></textarea>
          <span class="btn-send">
            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
          </span>
        </form>
      </div>
    </div>
  </div>


  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
</body>

</html>
