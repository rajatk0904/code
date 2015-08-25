To implement ftpm.py as ftpm command run the following command:
    $alias ftpm="python ~/"+path+"/ftpm.py"
    e.g:$alias ftpm="python ~/Downloads/assignment1/ftpm.py"
The structure of the command would be then:
    $ftpm <options> server file1 file2 file3 .... email
    i.e:$ftpm -l -a -m  172.20.176.233 a.txt b.txt pandark@cse.iitk.ac.in
In case you want to specify a path for uploading the command would be
    $ftpm <options> server:path file1 file2 ... email
    i.e:$ftpm -l -a -m -s -p 172.20.176.233:Downloads a.txt b.txt pandark@cse.iitk.ac.in