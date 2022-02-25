<?php session_start(); ?>
<html>

<head>
    <title>Departments</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="../css/departStyle.css">
</head>

<body>

    <div>
    <form method="POST" action="searchAttendance.php">
        
    <label for="startDate">Start Date:</label>
    <input type="date" name="startDate">
    <label for="startDate">End Date:</label>
    <input type="Date" name="endDate">

    <?php

    include 'connectToDb.php';

    if (!$sqldb->select_db('sas')) 
    {
        die("not connected to database");
    }
    $getSubjectQuery = "SELECT scode,name from subject";
    ?>
    <label for="subject">Subject:</label>
    <select name="subject">
    <?php
    if($subjects = $sqldb->query($getSubjectQuery))
    {
         if (mysqli_num_rows($subjects) > 0)
         {
             while ($subjects_row = mysqli_fetch_assoc($subjects))
             {
                ?>
                <option value ="<?php echo $subjects_row['scode'];?>" >
                    <?php echo $subjects_row['name'];?>
                </option>
                <?php
             }
         }
    }
    else
    {
        echo "Error running query for fetching subjects";
    }
    ?>
    


</select>
</div>
    <?php

    $username = $_SESSION["username"];
    $dID = $_GET["dID"];
    
    $getclassQuery = "SELECT cID,name from class";// WHERE dID = '$dID' and `sem`!=0";
    if($class = $sqldb->query($getclassQuery))
    {
        if (mysqli_num_rows($class) > 0)
        {

            while ($class_row = mysqli_fetch_assoc($class)) 
            {
                // $dId = $class_row['dID'];
                $className = $class_row['name'];
                $cID = $class_row['cID'];
        
                ?>

                <div class="bg-image">
                    <div class="card-holder">
                    <div class="card">
                        <div class="box">
                                <input type="submit" value ="<?php echo $className?>" ></div>                   
                        </div>
                    </div>
                
                <?php
            }
        }
    }    
    else
    {
        echo "Error running fetch class query";
    }
?>
</form>
</body>
</html>