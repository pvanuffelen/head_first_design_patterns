from mallard_duck import MallardDuck
from model_duck import ModelDuck
from fly_behavior import FlyRocketPowered


def mini_duck_simulator():
    mallard = MallardDuck()  # create the mallard duck object
    mallard.perform_quack()  # perform the quack method
    mallard.perform_fly()  # perform the fly method

    model = ModelDuck()  # create the model duck object
    model.perform_fly()  # perform the fly method of the model duck
    model.set_fly_behavior(FlyRocketPowered())  # set a new fly behavior for the model duck during run time
    model.perform_fly()  # perform the newly set fly behavior


def main():
    mini_duck_simulator()


if __name__ == '__main__':
    main()
