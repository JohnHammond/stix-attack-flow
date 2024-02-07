# STIX - Attack Flow


> John Hammond | Wednesday, February 7, 2024

-----------------------------------------------

Crappy code to work with MITRE Attack Flow with the `stix2` Python library.

These "Attack Flows" are an extension of STIX 2.1, and need some setup to be
easily used in code.

Note that this format will only generate a JSON file representing an Attack Flow... 
the Attack Flow "Builder" requires a `.afb` file type which will take other processing.

## Visualizing 

Since we do not yet generate `.afb` files, we can visualize an Attack Flow with the other tools 
suggested in their documentation.

On Windows, I have ran:

```
choco install GraphViz

pip install poetry
git clone https://github.com/center-for-threat-informed-defense/attack-flow/
cd .\attack-flow\
poetry install
poetry shell

af graphviz C:\Users\johnh\Desktop\test-flow.json C:\Users\johnh\Desktop\test-flow.dot
dot -Tpng .\test-flow.dot -O
```

This will generate a PNG image for our attack flow.

## Other Resources

* Attack Flow Builder: https://center-for-threat-informed-defense.github.io/attack-flow/ui/
* Attack Flow Documentation: https://center-for-threat-informed-defense.github.io/attack-flow/overview/
* STIX 2.1 Documentation: https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html
* Python Library `stix2` Documentation: https://stix2.readthedocs.io/en/latest/index.html
