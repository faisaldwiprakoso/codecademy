import sys
import os
import subprocess
from subprocess import run, PIPE, CalledProcessError
from rest_framework import serializers
from .models import Solution


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"
        depth = 1

class SolutionSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"

    def set_result(self, solution, file_extension):
        result = ''
        try:
            ext_file = file_extension.split(".")
            if ext_file[-1] == "java":
                result = self.executeJava(solution, file_extension)
            elif ext_file[-1] == "cpp":
                result = self.executeCpp(solution, file_extension)
            elif ext_file[-1] == "c":
                result = self.executeC(solution, file_extension)
            elif ext_file[-1] == "py":
                result = self.executePython(solution, file_extension)

            return result

        except Exception as e:
            # to return error in the code   
            # sys.stdout = original_stdout
            output = e
            return output

    def executeC(self, solution, file_extension):
        try:
            f = open(file_extension, 'w')
            f.write(solution)
            f.close()
            execute = (f"gcc ./{file_extension} -o out")
            subprocess.check_output(f"gcc {file_extension} -o out1;./out1", shell = True)
            os.system(execute)
            result = run(["./out"], stdout=PIPE).stdout.decode("UTF-8")
            return result
        
        except CalledProcessError as result:
            return result   
  
    def executeCpp(self, solution, file_extension):
        # create a pipe to a child process
        data, temp = os.pipe()
    
        # write to STDIN as a byte object(convert string
        # to bytes with encoding utf8)
        os.write(temp, bytes("5 10\n", "utf-8"));
        os.close(temp)
    
        # store output of the program as a byte string in s
        s = subprocess.check_output("g++ HelloWorld.cpp -o out2;./out2", stdin = data, shell = True)
    
        # decode s to a normal string
        return s.decode("utf-8")
  
    def executeJava(self, solution, file_extension):
        try:
            f = open(file_extension, 'w')
            f.write(solution)
            f.close()
            file_name = file_extension.split(".")[0]            
            subprocess.check_output(f"javac {file_extension}", shell=True)
            result = subprocess.check_output(f"java {file_name}", shell=True)
            return result.decode("UTF-8")
        
        except CalledProcessError as result:
            return result


    def executePython(self, solution, file_extension):
        original_stdout = sys.stdout
        sys.stdout = open(file_extension, 'w')

        #execute code
        exec(solution)  #example =>   print("hello world")

        sys.stdout.close()
        sys.stdout = original_stdout  
        result = open(file_extension, 'r').read()
        return result
  