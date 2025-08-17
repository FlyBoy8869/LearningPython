import subprocess

commands = [["clear"], ["figlet", "NewBrews"]]


def main():
    for command in commands:
        subprocess.run(command)


if __name__ == "__main__":
    main()
