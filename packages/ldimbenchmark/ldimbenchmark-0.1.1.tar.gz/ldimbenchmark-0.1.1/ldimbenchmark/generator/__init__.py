from ldimbenchmark.constants import LDIM_BENCHMARK_CACHE_DIR
from ldimbenchmark.generator.dataset_generator import (
    DatasetGenerator,
    DatasetGeneratorConfig,
)
from ldimbenchmark.generator.poulakis_network import generatePoulakisNetwork
import wntr
import matplotlib.pyplot as plt
import os
import yaml
from math import sqrt
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import numpy as np
import math
from datetime import datetime
from itertools import repeat

import logging
from argparse import ArgumentParser
from functools import partial


# TODO: Move to main __init__.py
# parser = ArgumentParser()
# parser.add_argument(
#     "-o",
#     "--outputFolder",
#     dest="outputFolder",
#     default="./out",
#     help="the folder to generate the datasets in",
# )
# parser.add_argument(
#     "-c",
#     "--configurationFile",
#     dest="configurationFile",
#     default="dataset_configuration_evaluation.yml",
#     help="configuration file which will be used to generate the according dataset",
# )
# parser.add_argument(
#     "-n",
#     "--waterNetwork",
#     dest="waterNetwork",
#     default=None,
#     help="water network (.inp) file used to generate the dataset",
# )
# parser.add_argument(
#     "-v",
#     "--variations",
#     dest="variations",
#     default=None,
#     choices=["time", "junctions"],
#     help="ignore certain configurations and generate all variations of the property",
# )

# args = parser.parse_args()


# In[2]:

# Read input arguments from yalm file
# configuration_file_path = os.path.join(args.configurationFile)
# try:
#     with open(configuration_file_path, "r") as f:
#         config = yaml.safe_load(f.read())
# except:
#     print(f'"dataset_configuration" at {configuration_file_path} file not found.')
# sys.exit()

# yaml_example = """
# model:
#   startTime: 2022-01-01 00:00
#   endTime: 2022-03-01 00:00
#   timestep: 5min

# leakages:
#   - linkID: P-03
#     startTime: 2022-02-01 00:00
#     peakTime: 2022-02-15 12:00
#     endTime: 2022-03-01 00:00
#     leakDiameter: 0.011843  # (m)

# pressure_sensors: 'all'

# flow_sensors:
# - P-01

# level_sensors: []

# amrs:
# - J-03

# """
# config = yaml.safe_load(yaml_example)

# Just check if it is already valid
# DatasetGeneratorConfig(**config)
# water_network_model = wntr.network.WaterNetworkModel(
#     config['model']['filename'])

# In[3]:
# {'Nodes': 57, 'Links': 98
# for size in range(3, 8):
#     wn = generatePoulakisNetwork(size)
#     wn.write_inpfile(os.path.join(
#         results_folder, f"poulakis-{size}.inp"))
#     print(wn.describe())
#     fig, ax = plt.subplots(1, 1, figsize=(12, 10))
#     ax = wntr.graphics.plot_network(wn, ax=ax, title="Poulakis Network",
#                                     node_labels=True, link_labels=True,)  # node_attribute='elevation',)
#     fig.savefig(f"out/network_poulakis-{size}.png")


def generateDatasetForJunctionNumber(
    junctions: int, out_dir: str = LDIM_BENCHMARK_CACHE_DIR
):
    # print(junctions)
    results_folder = os.path.join(out_dir, "synthetic-j", f"synthetic-j-{junctions}/")
    if os.path.exists(results_folder):
        # print(f"Skipping {junctions} as it already exists")
        return
    os.makedirs(results_folder, exist_ok=True)

    wn = generatePoulakisNetwork(network_size=0, max_junctions=junctions)
    wn.write_inpfile(os.path.join(results_folder, f"poulakis-j-{junctions}.inp"))
    # print(wn.describe())
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax = wntr.graphics.plot_network(
        wn,
        ax=ax,
        title="Poulakis Network",
        node_labels=True,
        link_labels=True,
    )  # node_attribute='elevation',)
    fig.savefig(os.path.join(results_folder, f"network_poulakis-j-{junctions}.png"))

    yaml_example = """
    model:
      startTime: 2022-01-01 00:00
      endTime: 2022-03-01 00:00
      timestep: 5min

    leakages:
    - linkID: P-03
      startTime: 2022-02-01 00:00
      peakTime: 2022-02-15 12:00
      endTime: 2022-03-01 00:00
      leakDiameter: 0.011843  # (m)

    pressure_sensors: 'all'

    flow_sensors:
    - P-01

    level_sensors: []

    amrs:
    - J-03

    """
    config = yaml.safe_load(yaml_example)
    # Call leak dataset creator
    generator = DatasetGenerator(wn, config)
    # Create scenario one-by-one
    generator.generate()

    # wntr.graphics.plot_network(leak_wn, node_attribute=results.node['pressure'].loc[8000*300, :], link_attribute=results.link['flowrate'].loc[8000*300, :].abs(
    # ), node_size=100, node_colorbar_label='Pressure', link_colorbar_label="Flowrate")
    generator.write_generated_data(results_folder, f"synthetic-j-{junctions}")


def generateDatasetForTimeSpanDays(days: str, out_dir: str = LDIM_BENCHMARK_CACHE_DIR):
    results_folder = os.path.join(out_dir, "synthetic-days", f"synthetic-days-{days}/")
    if os.path.exists(results_folder):
        # print(f"Skipping {results_folder} as it already exists")
        return
    os.makedirs(results_folder, exist_ok=True)
    wn = generatePoulakisNetwork()

    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax = wntr.graphics.plot_network(
        wn,
        ax=ax,
        title="Poulakis Network",
        node_labels=True,
        link_labels=True,
    )  # node_attribute='elevation',)
    # fig.savefig(os.path.join(results_folder, "model.png"))

    startDate = np.datetime64("2022-01-01 00:00")
    endDate = startDate + np.timedelta64(days, "D")
    yaml_example = """
    model:
      startTime: 2022-01-01 00:00
      endTime: 2022-03-01 00:00
      timestep: 5min

    leakages:
    - linkID: P-03
      startTime: 2022-02-01 00:00
      peakTime: 2022-02-15 12:00
      endTime: 2022-03-01 00:00
      leakDiameter: 0.011843  # (m)

    pressure_sensors: 'all'

    flow_sensors:
    - P-01

    level_sensors: []

    amrs:
    - J-03

    """
    config = yaml.safe_load(yaml_example)
    config["model"]["startTime"] = str(startDate)
    config["model"]["endTime"] = str(endDate)

    leakfree_timespan = int((days * 24) / 2)
    config["leakages"][0]["startTime"] = str(
        startDate + np.timedelta64(leakfree_timespan, "h")
    )
    config["leakages"][0]["peakTime"] = str(
        startDate + np.timedelta64(leakfree_timespan + 1, "h")
    )
    config["leakages"][0]["endTime"] = str(endDate)

    # Call leak dataset creator
    generator = DatasetGenerator(wn, config)
    # Create scenario one-by-one
    generator.generate()

    # wntr.graphics.plot_network(leak_wn, node_attribute=results.node['pressure'].loc[8000*300, :], link_attribute=results.link['flowrate'].loc[8000*300, :].abs(
    # ), node_size=100, node_colorbar_label='Pressure', link_colorbar_label="Flowrate")
    generator.write_generated_data(results_folder, f"synthetic-days-{days}")


def generateDatasetsForJunctions(
    junction_count_low: int,
    junction_count_high: int,
    out_dir: str = LDIM_BENCHMARK_CACHE_DIR,
):
    parallel = True
    if parallel == True:
        days = range(junction_count_low, junction_count_high)
        with Pool(processes=cpu_count() - 1) as p:
            max_ = len(days)
            with tqdm(total=max_) as pbar:
                for result in p.starmap(
                    generateDatasetForJunctionNumber, zip(days, repeat(out_dir))
                ):
                    # p.imap_unordered(generateDatasetForJunctionNumber, ):
                    pbar.update()


def generateDatasetsForTimespan(
    days_low: int, days_high: int, out_dir: str = LDIM_BENCHMARK_CACHE_DIR
):
    parallel = True
    if parallel == True:
        days = range(1, 61)
        with Pool(processes=cpu_count() - 1) as p:
            max_ = len(days)
            with tqdm(total=max_) as pbar:
                for result in p.imap_unordered(
                    partial(generateDatasetForTimeSpanDays, out_dir=out_dir), days
                ):
                    # p.starmap(
                    #     generateDatasetForTimeSpanDays, zip(days, repeat(out_dir))
                    # ):
                    pbar.update()


# if args.variations == "junctions":
#     generateDatasetsForJunctions(4, 59)

# for pipes in range(3, 57):
#     wn = generatePoulakisNetwork(8, max_pipes=pipes)
#     wn.write_inpfile(os.path.join(
#         results_folder, f"poulakis-p-{pipes}.inp"))
#     print(wn.describe())
#     fig, ax = plt.subplots(1, 1, figsize=(12, 10))
#     ax = wntr.graphics.plot_network(wn, ax=ax, title="Poulakis Network",
#                                     node_labels=True, link_labels=True,)  # node_attribute='elevation',)
#     fig.savefig(f"out/network_poulakis-p-{pipes}.png")

# In[11]:

# Generate Dataset for increasing timespan


# elif args.variations == "time":
#     generateDatasetsForTimespan(1, 61)


# Otherwise (if args.variations == None)
# else:
#     results_folder = args.outputFolder
#     os.makedirs(results_folder, exist_ok=True)

#     if args.waterNetwork is None:
#         wn = generatePoulakisNetwork()
#     else:
#         wn = wntr.network.WaterNetworkModel(args.waterNetwork)

#     fig, ax = plt.subplots(1, 1, figsize=(12, 10))
#     ax = wntr.graphics.plot_network(
#         wn,
#         ax=ax,
#         title="Poulakis Network",
#         node_labels=True,
#         link_labels=True,
#     )  # node_attribute='elevation',)
#     # fig.savefig(os.path.join(results_folder, "model.png"))

#     # Call leak dataset creator
#     generator = DatasetGenerator(wn, config)
#     # Create scenario one-by-one
#     generator.generate()

#     # wntr.graphics.plot_network(leak_wn, node_attribute=results.node['pressure'].loc[8000*300, :], link_attribute=results.link['flowrate'].loc[8000*300, :].abs(
#     # ), node_size=100, node_colorbar_label='Pressure', link_colorbar_label="Flowrate")
#     generator.write_generated_data(results_folder)
