import subprocess
import pathlib
import os

from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

# First load the template yaml

with open('./../sky130_fd_sc_lp__inv_1.yml') as file:

    settings = yaml.load(file)


# General setting

settings['cells']['sky130_fd_sc_lp__inv_1']['netlist'] = "./../sky130_inv1.spice"

# Parameter setting

vdds    = [0.9]
slews   = [0.01]
loads   = [0.015]

for vdd in vdds:

    settings['settings']['named_nodes']['vdd']['voltage']   = vdd
    settings['settings']['named_nodes']['nwell']['voltage'] = vdd

    settings['cells']['sky130_fd_sc_lp__inv_1']['slews']    = slews
    settings['cells']['sky130_fd_sc_lp__inv_1']['loads']    = loads


    with open('tmp.yml', 'wb') as f:
    
        yaml.dump(settings, f)

    # Call Charlib on that tmp file

    subprocess.run(['charlib', 'run', './'])

    os.rename("./results/sky130_fd_sc_lp.lib", "./results/sky130_fd_sc_lp_" + str(vdd).replace(".","V") + ".lib")


# Clean up

os.remove("tmp.yml")






