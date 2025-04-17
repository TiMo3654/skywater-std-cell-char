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

vdds    = [1.8, 1.5, 1.2, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5]
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

    filename = "./results/sky130_fd_sc_lp_" + str(vdd).replace(".","V") + ".lib"

    os.rename("./results/sky130_fd_sc_lp.lib", filename)

    print(f"Results stored in {filename}")


# Clean up

os.remove("tmp.yml")






