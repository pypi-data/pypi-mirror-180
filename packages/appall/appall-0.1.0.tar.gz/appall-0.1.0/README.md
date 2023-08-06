# Appall 😱

**a**bridged **p**retty **p**rinting **a**pp for **l**ong **l**ine **l**ogging a.k.a one **app** to log'em **all**

This tiny utility allows you to **horizontally** juxtapose some text in terminal

## Usage

The tool can be used the following way (see `examples` folder):

```py
from appall import AppallingLogger

logger = AppallingLogger()

logger.log("foo")
logger.log("qux")
logger.loop()

logger.log("bar")
logger.log("quux")

logger.log("baz")
logger.log("quuz")

logger.print(column_width = 10)
```

This example produces the following output:

```sh
foo       bar       baz       
qux       quux      quuz      
```

## Installation

Install the program using this command:

```sh
pip install appall
```

Or clone the repo and add path to the `appall` folder at the end of your `PYTHONPATH`. In this case `environment.yml` file will be useful for creating an environment. This can be done using the following command:

```sh
conda env create -f environment.yml
```

## Testing

Test the tool using following command:

```sh
python -m unittest discover test
```
