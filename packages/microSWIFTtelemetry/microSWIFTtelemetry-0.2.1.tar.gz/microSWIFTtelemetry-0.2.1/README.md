# microSWIFTtelemetry
microSWIFTtelemetry provides Python-based functionality for pulling telemetry from the microSWIFT wave buoy developed at the University of Washington Applied Physics Laboratory (UW-APL). 

It contains collection of python functions for programmatically accessing and compiling data from the UW-APL SWIFT server at [http://swiftserver.apl.washington.edu/](http://swiftserver.apl.washington.edu/) (base URL).

See [examples/](https://github.com/jacobrdavis/microSWIFTtelemetry/tree/main/examples) for usage.





---
**NOTE:**

Please note this package is only developed to work with microSWIFTs and not the larger SWIFT buoys. 
For a MALTAB-based implementation that works for the entire suite of SWIFTs, see `SWIFT-codes` and the `pullSWIFTtelemetry.m` function at [https://github.com/SASlabgroup/SWIFT-codes/blob/master/GeneralTools/pullSWIFTtelemetry.m](https://github.com/SASlabgroup/SWIFT-codes/blob/master/GeneralTools/pullSWIFTtelemetry.m).

The server can also be queryed and explored using the web page and web-based map: 
* [http://faculty.washington.edu/jmt3rd/SWIFTdata/DynamicDataLinks.html](http://faculty.washington.edu/jmt3rd/SWIFTdata/DynamicDataLinks.html) (web page)
* [https://swiftserver.apl.washington.edu/map/](https://swiftserver.apl.washington.edu/map/) (map)


---


## Installation
The latest release of `microSWIFTtelemetry` can be installed from PyPI using pip: 

```
pip install microSWIFTtelemetry
```
## Organization
```
microSWIFTtelemetry/
├── LICENSE
├── README.md
├── docs
├── examples/
│   ├── create_telemetry_report_example.ipynb
│   └── pull_telemetry_example.ipynb
├── microSWIFTtelemetry/
│   ├── __init__.py
│   ├── pull_telemetry.py
│   ├── sbd/
│   │   ├── __init__.py
│   │   ├── compile_sbd.py
│   │   ├── definitions.py
│   │   └── read_sbd.py
│   └── version.py
├── pyproject.toml
├── requirements.txt
├── setup.py
└── tests/
    └── test_microSWIFTtelemetry.py
```
## microSWIFT
Learn more about the microSWIFT wave buoy:
* [https://apl.uw.edu/project/projects/swift/pdfs/microSWIFTspecsheet.pdf](https://apl.uw.edu/project/projects/swift/pdfs/microSWIFTspecsheet.pdf) (spec sheet)

* [https://github.com/SASlabgroup/microSWIFT](https://github.com/SASlabgroup/microSWIFT) (microSWIFTv1 operational code)

Schematic depicting buoys telemetering wave data from the ocean to a scientist on land via satellite:
![schematic depicting buoys telemetering wave data from the ocean to a scientist on land via satellite](./docs/imgs/how_telemetry_works.png)

