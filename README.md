You can edit your .bashrc file to create them as alias commands. My .zshrc edit for these are:
alias cr_jdk="python3 ~/path/to/create_jdk_project.py"
alias co_jdk="python3 ~/path/to/compile_java.py"
alias exec_jdk="python3 ~/path/to/init_java_project/execute_java.py"
alias cexec_jdk="python3 ~/path/to/init_java_project/execute_java.py"

cr_jdk: create a java project (src/bin style) with a Main.java class
co_jdk: compile java project
exec_jdk: execute java project
cexec_jdk: co + exec

Be ware to run this commands inside the project

