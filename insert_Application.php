<html>
<style>
    <?php
    $image = "image.png"
    ?>
      body {
        background-image: url('<?php echo $image;?>');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
        background-position: center; 
      }
</style>
<body>
<button onclick="main_menu()">Main menu</button>
<br><br>
<script>
        function main_menu(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/main_menu.php"
        }
</script>
<h3 style="color:rgb(255,255,255)">Enter information about an application to add to the database:</h3>

<form style="color:rgb(255,255,255)" action="insert_Application.php" method="post">
    Student ID: <input type="text" name="sid"><br>
    Job ID: <input type="text" name="jid"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $sid = escapeshellarg($_POST[sid]);
    $jid = escapeshellarg($_POST[jid]);

    $command = 'python3 insert_Application.py ' . $sid . ' ' . $jid;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<div style='color:rgb(255,255,255)'>";
    echo "<p>command: $command <p>"; 

    // run insert_Application.py
    system($escaped_command);           
}
?>


