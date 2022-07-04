import tkinter as tk

from services.commands.command_invoker import CommandInvoker
from models.resolution import Resolution
from services.algorithm_service import AlgorithmService
from services.image_service import ImageService
from services.algorithm_runner import AlgorithmRunner
from controllers.runner_controller import RunnerController
from controllers.params_controller import ParamsController
from view.algorithm_view import AlgorithmView
from controllers.algorithm_controller import AlgorithmController
from view.params_view import ParamsView
from view.components_view import ComponentView
from controllers.image_controller import ImageController
from view.image_view import ImageView
from view.main_view import MainView


def setup():
    commandInvoker = CommandInvoker()
    resolution = Resolution(height=10, width=10)
    algorithmService = AlgorithmService(invoker=commandInvoker)

    imageService = ImageService(resolution=resolution)
    algorithmRunner = AlgorithmRunner(
        invoker=commandInvoker, image_service=imageService)
    runnerController = RunnerController(algorithmRunner=algorithmRunner)

    paramsController = ParamsController(
        algorithmService=algorithmService)
    algorithmView = AlgorithmView(paramsController, runnerController)

    algorithmController = AlgorithmController(
        algorithmView=algorithmView, algorithmService=algorithmService)

    paramsView = ParamsView(algorithmController=algorithmController)
    componentView = ComponentView(algorithmController=algorithmController)
    imageController = ImageController(imageService=imageService)
    imageView = ImageView(imageController=imageController)

    mainwindow = MainView(algorithmView=algorithmView, componentView=componentView,
                          imageView=imageView, paramsView=paramsView)

    return mainwindow


if __name__ == '__main__':
    window = tk.Tk()
    print('setup')
    mainwindow = setup()
    mainwindow.create_main_view(window)
    print('dupa')
    window.mainloop()
    print('nic ci nie pokaze')
