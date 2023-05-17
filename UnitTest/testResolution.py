import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from resolutionAlgorithm import Resolution
from testGenerator import TestGenerator
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser

class TestResolution(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     testGenerator = TestGenerator()
    #     testGenerator.generateHornCase("testcases/horns/")

    def test(self):
        for i in range(50):
            print(i)
            env = Environment()
            env.readFile("testcases/horns/horn" + str(i) + ".txt")
            resolution = Resolution()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))
            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))


            self.assertEqual(resolution.solve(env.knowledgeBase, env.query),
                             entails(query, kb))