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
<h3 style="color:rgb(255,255,255)">Search for students:</h3>
<form style="color:rgb(255,255,255)" action="student_Majors.php" method="post">
    Major: <select name="major" id="major">
        <option name = "CSCE" value="CSCE">CSCE</option>
        <option name = "MEEG" value="MEEG">MEEG</option>
        <option name = "ELEG" value="ELEG">ELEG</option>
        <option name = "CVEG" value="CVEG">CVEG</option>
        <option name = "INEG" value="INEG">INEG</option>
        <option name = "CHEG" value="CHEG">CHEG</option>
        <option name = "BMEG" value="BMEG">BMEG</option>
        <option name = "ALL" value="ALL">ALL</option>
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
    $major = escapeshellarg($_POST[major]);

    $command = 'python3 student_Majors.py ' . $major;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<div style='color:rgb(255,255,255)'>";
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>


