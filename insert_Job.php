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
<h3 style="color:rgb(255,255,255)">Enter information about a job to add to the database:</h3>

<form style="color:rgb(255,255,255)" action="insert_Job.php" method="post">
    Job ID: <input type="text" name="jid"><br>
    Company Name: <input type="text" name="name"><br>
    Job Title: <input type="text" name="title"><br>
    Salary: <input type="text" name="salary"><br>
    Desired Major: <select name="major" id="major">
        <option name = "CSCE" value="CSCE">CSCE</option>
        <option name = "MEEG" value="MEEG">MEEG</option>
        <option name = "ELEG" value="ELEG">ELEG</option>
        <option name = "CVEG" value="CVEG">CVEG</option>
        <option name = "INEG" value="INEG">INEG</option>
        <option name = "CHEG" value="CHEG">CHEG</option>
        <option name = "BMEG" value="BMEG">BMEG</option>
    </select>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $jid = escapeshellarg($_POST[jid]);
    $name = escapeshellarg($_POST[name]);
    $title = escapeshellarg($_POST[title]);
    $salary = escapeshellarg($_POST[salary]);
    $major = escapeshellarg($_POST[major]);

    $command = 'python3 insert_Job.py ' . $jid . ' ' . $name . ' ' . $title . ' ' . $salary . ' ' . $major;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<div style='color:rgb(255,255,255)'>";
    echo "<p>command: $command <p>"; 

    // run insert_Job.py
    system($escaped_command);           
}
?>


