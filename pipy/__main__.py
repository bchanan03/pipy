from pipy.pipy_config import config

if __name__ == '__main__':

    pipy = config.PipyConfig()
    print("==========================")
    print("Before any installation")
    print("==========================")
    print(pipy.installed())


    print("\n--------------------------")
    print("Installing packages")
    print("--------------------------")
    pipy.install("p4==1.0.0")

    print("\n==========================")
    print("After installing packages")
    print("==========================")
    print(pipy.installed())

