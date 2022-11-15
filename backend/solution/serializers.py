from rest_framework import serializers
from .models import Solution
import sys

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"
        depth = 1

class SolutionSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"

    def get_solution_code(self, solution):
        return solution

    def set_result(self, solution):
        try:
            # todo: how to implement another compiler beside python

            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')

            #execute code
            exec(solution)  #example =>   print("hello world")

            sys.stdout.close()
            sys.stdout = original_stdout  
            output = open('file.txt', 'r').read()
            return output
        except Exception as e:
            # to return error in the code   
            sys.stdout = original_stdout
            output = e