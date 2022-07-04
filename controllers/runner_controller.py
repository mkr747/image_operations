from services.algorithm_runner import AlgorithmRunner


class RunnerController:
    def __init__(self, algorithmRunner: AlgorithmRunner):
        self.__algorithmRunner = algorithmRunner

    def play(self):
        self.__algorithmRunner.run()
