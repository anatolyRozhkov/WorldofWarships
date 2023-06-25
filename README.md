SOLUTION TO THE FIRST PROBLEM

```
docker-compose up
docker exec -it popular_languages bash
cd popular_languages/ && pytest -sv --tb long --log-path 'artifacts/'
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

In first terminal window:
```
sudo apt-get install x11-xserver-utils
xhost +
```
This will allow the container to use your machine's GUI
This setting resets automatically every time your reload your
PC, so no worries!

In the second terminal window:
```
docker exec -it engine2d bash
cd popular_languages/ && python3
from engine2d import DrawShapes
a = DrawShapes()
```
Dot coordinates for triangle and rectangle
should be provided like this: '23,43'.

The rest should be pretty much self-explanatory.

Super sorry to admit it, but I didn't have the time
to complete unit tests. Tho I haven't completed the
task, I've spent so much time
building the GUI for the engine that I decided to 
share my solution anyways 😐.