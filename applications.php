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
<h3 style="color:rgb(255,255,255)">Search for applications (only fill in one box):</h3>
<form style="color:rgb(255,255,255)" action="applications.php" method="post">
    Search by Major: <input type="text" name="major"><br>
    Search by StudentID: <input type="text" name="sid"><br>
    Search by JobID: <input type="text" name="jid"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $major = escapeshellarg($_POST[major]);
    $sid = escapeshellarg($_POST[sid]);
    $jid = escapeshellarg($_POST[jid]);

    $command = 'python3 applications.py ' . $major . ' ' . $sid . ' ' . $jid;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<div style='color:rgb(255,255,255)'>";
    echo "<p>command: $command <p>"; 

    // run applications.py
    system($escaped_command);           
}
?>


