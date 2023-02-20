# UOCIS322 - Project 4 #
Cheyanne Kester
This project is a little more broad with what we need to learn and do.

To build and run this project in Docker, use the following commands:
`docker build -t myimage .`
`docker run myimage`

If you wish to run this program locally, follow this procedure:
`pip install -r requirements.txt` (if this doesn't work, install `pip` on your machine)
`python3 flask_brevets.py` (if this doesn't work, use `python flask_brevets.py`)

## The Application - Breakdown
This is an application to calculate and display the Open and Close times of checkpoints along a bicycle race of a certain distance, called the Brevet distance. A user should be able to select their desired Brevet distance by using the `Distance` drop down menu, and select their start date and time using the box with the words `Begins at` next to it. After the user has made these selections, they can then input checkpoints in the `Km` or `Miles` column, and the application will display the Open and Close date and times for each checkpoint. 


## What we had to do
### Write Tests
Firstly, we must write 5 test cases in `test_acp_times.py` for the algorithm file `acp_times.py`. I followed the procedure that Ali showed us in lab on Friday the 17th. I made a test function for each possible brevet distance, and within each I tested checkpoints for every 50 km. For example, the test for brevet 1000 tested 21 different checkpoints.

To execute these tests, follow this procedure: (this is how I did it, but there's probably a faster way)
`docker build -t myimage .`
`docker run myimage`
`^c` (to get your terminal back)
`docker start [containerName]`  (you can get the containerName by using `docker ps -a`)
`docker exec [containerName] app/run_tests.sh`

### Implement Algorithm
Secondly, we had to implement the algorithm in `acp_times.py` so that it would pass the test cases we made. 
The general idea is that for every checkpoint past a certain number of km (200 km for open time and 600km for close time) we had to incrementally calculate the start and close times. By this I mean that, for open time, every 200 km chunk up to the checkpoint distance had to use a different speed; and for close time, every 600km chunk had to use a different speed. A great example of this is `Example 3` on the website https://rusa.org/pages/acp-brevet-control-times-calculator. 

### Update Frontend to use proper start time and brevet distance
Next, we had to modify the `calc.html` file to send the start time (in the "Begins at" box) and the Brevet distance (in the Distance box) to `flask_brevets.py`. 

### Update Flask to accept the new start time and brevet distance
Lastly, we had to modify `flask_brevets.py` to accept the start time and brevet distance. I did this by using `request.args.get(what I need)`, as the given code did with getting `km`. Once the file was accepting the arguments, I had to modify a couple of the given code's lines to ensure that start time and brevet distance were being passed into `acp_times.py` correctly. 


## Authors of Original Overview and Project 
### (Content from Original README deleted for simplicity)

Michal Young, Ram Durairajan. Updated by Ali Hassani.
