<?php session_start(); ?>
<html>

<head>
    <title>Departments</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="../css/departStyle.css">
</head>

<body>
    <?php
    include 'connectToDb.php';

    $username = $_SESSION["username"];

    if (!$sqldb->select_db('sas')) 
    {
        die("not connected to database");
    }
    $getDepartmentsQuery = "SELECT name,dID from department WHERE 1";
    if($departments = $sqldb->query($getDepartmentsQuery))
    {
        if (mysqli_num_rows($departments) > 0)
        {

            while ($departments_row = mysqli_fetch_assoc($departments)) 
            {
                $dID = $departments_row['dID'];
                $departName = $departments_row['name'];
        
                ?>

                <div class="bg-image">
                    <div class="card-holder">
                    <div class="card">
                        <div class="box">
                            <a href="bct.php?dID=<?php echo $dID;?>" >
                                <div class="text"><?php echo $departName?></div>                   
                            </a>
                        </div>
                    </div>
                
                <?php
            }
        }
    }    
    else
    {
        echo "Error running fetch department query";
    }
?>
</body>
</html>