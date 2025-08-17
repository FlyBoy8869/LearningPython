from config import config
import json
import matplotlib.pyplot as plt


def main():
    with open("baseline_flow_data_2008", mode="rb") as fp:
        baseline_flow_data = json.load(fp)
    with open("uut_flow_data", mode="rb") as fp:
        uut_flow_data = json.load(fp)

    pressures = config['PLOT']['pressures'].split(" ")

    plt.plot(baseline_flow_data["flow data"], pressures, "bD", label=baseline_flow_data["legend key"])
    plt.plot(uut_flow_data["flow data"], pressures, "ro", label=uut_flow_data["legend key"])
    plt.title(config["PLOT"]["title"])
    plt.xlabel(config["PLOT"]["xLabel"])
    plt.ylabel(config["PLOT"]["yLabel"])
    if config["PLOT"]["minorTickMarks"] == "true":
        plt.minorticks_on()
    plt.grid(True, which="both", axis=config["PLOT"]["axis"], linestyle="--")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
