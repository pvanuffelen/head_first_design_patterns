from mallard_duck import MallardDuck


def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()


def main():
    mini_duck_simulator()


if __name__ == '__main__':
    main()
