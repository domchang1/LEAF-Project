<?php
$server = "localhost";
$username = "root";
$password = "";
$dbname = "insert";

$conn = mysqli_connect($server, $username, $password, $dbname);

if(isset($_POST['submit'])){

    if(!empty($_POST['nitrogen']) && !empty($_POST['phosphorus'])&& !empty($_POST['potassium']) && !empty($_POST['moisture'])&& !empty($_POST['time'])){
        $nitrogen = $_POST['nitrogen'];
        $phosphorus = $_POST['phosphorus'];
        $potassium = $_POST['potassium'];
        $moisture = $_POST['moisture'];
        $time = $_POST['time'];

        $query = "insert into form(nitrogen,phosphorus,potassium,moisture,time) values('$nitrgoen', '$phosphorus', '$potassium', '$moisture', '$time')";

        $run = mysqli_query($conn,$query) or die(mysqli_error());

        if($run){
            echo "form submitted successfully";
        }
        else{
            echo "form not submitted";
        }

    }
}