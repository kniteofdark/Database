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
<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $name = escapeshellarg($_POST[name]);

    // build the linux command that you want executed;  
    $command = 'python3 main_menu.py ' . $name;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "<p> command: $command <br>";
    system($command);           
}
?>

<h3 style="color:rgb(255, 255, 255)">Main menu</h3>
<div class="center">
   <button onclick="insert_Student()">Insert new Student</button>
   <br><br>
   <button onclick="insert_Job()">Insert new Job</button>
   <br><br>
   <button onclick="insert_Application()">Insert new Application</button>
   <br><br>
   <button onclick="student_Majors()">View Students based on Major</button>
   <br><br>
   <button onclick="job_Majors()">View Jobs based on Major</button>
   <br><br>
   <button onclick="applications()">View Applications</button>
   <br><br>
</div>

<script>
         function insert_Student(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/insert_Student.php"
         }
         function insert_Job(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/insert_Job.php"
         }
         function insert_Application(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/insert_Application.php"
         }
         function student_Majors(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/student_Majors.php"
         }
         function job_Majors(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/job_Majors.php"
         }
         function applications(){
            location="http://www.csce.uark.edu/~dpvaughn/project_python/applications.php"
         }
      </script>
<br><br>

</body>
</html>



