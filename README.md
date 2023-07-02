SOLUTION TO THE FIRST PROBLEM

```
docker-compose up
docker exec -it popular-languages bash
pytest -sv --tb long --log-path 'artifacts/'
```

1) I've modified the exception message a bit to include the 
difference between actual and required number of visitors.
I did so because it's not exactly easy to read those ginormous numbers.
2) in the artifacts/test_case_logs/ dir you can find
files that have some info about the tests.
Particularly data from the table and info about what rows
hadn't had enough monthly visitors. Each file corresponds 
to a test it's named after.
3) you can play with scrap_data_from_wiki_table function
to make it return data from the table in any dataclass format you want.
Since the task haven't given me any particulars on how the
dataclasses should be returned, I've taken the liberty to return 
the end result as a list of dicts


SOLUTION TO THE SECOND PROBLEM

In second terminal window:
```
sudo apt-get install x11-xserver-utils
xhost +
```
This will allow the container to use your machine's GUI
This setting resets automatically every time your reload your
PC, so no worries!

In second terminal window:
```
docker exec -it engine2d bash
python3
from engine2d import DrawShapes
a = DrawShapes()
```
Dot coordinates for triangle and rectangle
should be provided like this: '23,43'.

The rest should be pretty much self-explanatory.

TEST PLAN

Basics

| # |               Test               |
|---|:--------------------------------:|
| 1 | draw shapes of different colours |
| 2 |        erase shapes              |

GUI Layout

| # |                    Test                     |
|---|:-------------------------------------------:|
| 1 | presence of only expected widgets on page   |

Validation

| # |          Test          |
|---|:----------------------:|
| 1 | inputs have validation |

In third terminal window:
```
docker exec -it engine2d bash
pytest -sv --tb long
```
If you want to run a specific group of test
(basics, validation, buttons) do this:
```
pytest -m basics -sv --tb long
```

THE END

Thanks for giving me a chance! 

Normally when people ask me why I want to work on their
project things get awkward coz it's a bit hard to come up with
motivation for building a corporate app that would be 
used by a select group of bankers or company managers.

With WoW it's really easy to say why I'd like to work with you!
It's coz you are building a cool game that I've tried 
and really liked. I keep my fingers crossed that I'll get the chance
to be part of that project 🍀