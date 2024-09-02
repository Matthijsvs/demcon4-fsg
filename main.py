class Planner:
    def __init__(self, data):
        self.stages = []
        self.end_time = 0

        show_list = [item.strip() for item in data]		# clean data
        for show in show_list:
            name, start, end = show.split()
            time_range = range(max(0,int(start)), int(end) + 1)# create range object for this show
            
            self.end_time = max(self.end_time, int(end) + 1)	# determine new end time
            
            ''' Here we try to find an empty stage, or create a new stage if all are full
            Using dictionary lookup, we can find if any hour is already used directly.'''
            for stage in self.stages:
                for time in time_range:
                    if time in stage:  		  # collision with existing show
                        break
                else:
                    self.book(stage, time_range, name)  # no collision, reserve stage with this show
                    break
            else:					  # no stages left
                new_stage = {}
                self.stages.append(new_stage)  	  # create new stage
                self.book(new_stage, time_range, name)

    def output(self,width=10):
        '''Print schedule to console, optional argument: column width'''
    	
        print(f"time|", end="")		#output header
        for i in range(len(self.stages)):
            s = f"Stage{i}"
            print(f"{s:^{width}.{width}}|", end="")
        print("")

        for i in range(self.end_time):	#output schedule
            print(f"{i:<4}|", end="")
            for stage in self.stages:
                s = stage.get(i, "-")   	#return "-" if key not found (stage is not booked)
                print(f"{s:^{width}.{width}}|", end="")
            print("")

    @classmethod
    def book(cls, stage, duration, name):  # reserve stage for this show
        for time in duration:
            stage[time] = name

    @classmethod
    def from_file(cls, fname):		
        with open(fname, "r") as f:
            return Planner(f.readlines())


if __name__ == "__main__":
    # Create planner object from iterable list
    ex1 = Planner(["show_1 36 39", "show_2 30 33", "show_3 29 36"])
    ex1.output()

    # Create planner object from file:
    ex2 = Planner.from_file("sample.txt")
    ex2.output(width=6)
    
    # Adjust column width for long names
    ex3 = Planner(["long_Show_name 6 9", "long_Show(tribute_band) 5 6", "show_3 0 3"])
    ex3.output(18)

