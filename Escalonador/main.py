class scheduler:
    def __init__(self,list):
        self.processes = list
        self.total_time = 0
        self.total_memory = 20
        self.memory_avaliable = 20
        self.current_process = 0
        self.processing = []
    def toString(self):
        return "total_process: {},\n" \
               "total_time:{},\n" \
               "Throughput : {},\n" \
               "average waiting time {}\n".format(
                len(self.processes),
                self.total_time,
                self.total_time /len(self.processes),
                self.waiting_time())

    def do_job(self):
        for index,i in enumerate(self.processes):
            if i.size < self.memory_avaliable:
                self.processing.append(i)
                self.memory_avaliable -= i.size
                self.current_process = index

        self.FCFS()
        print(self.toString())
        self.waiting_time()

    def execute(self, process):
        print(process.id)

    def FCFS(self):
        self.total_time += 1
        index = len(self.processing)
        while(index > 0):
            self.total_time += 1
            self.processing[0].waiting_time = self.total_time
            self.total_time += self.processing[0].time
            self.execute(self.processing[0])
            self.memory_avaliable += self.processing[0].size

            self.processing.pop(0)
            self.check()
            index = len(self.processing)

    def check(self):
        if(self.current_process < len(self.processes) - 1):
            if (self.memory_avaliable > self.processes[self.current_process + 1].size):
                self.current_process += 1
                self.processing.append(self.processes[self.current_process])
    def waiting_time(self):
        avg = 0
        for i in self.processes:
            avg += i.waiting_time
        return avg/len(self.processes)


class process:
    def __init__(self, id, size,io_perc,time):
        self.id = id
        self.size = size
        self.time = time
        self.io_percent = io_perc
        self.waiting_time = 0


def readFileIO(path):
    process_list =  []
    f = open(path)
    for index,line in enumerate(f):
        if(line[0] == '#'):
            continue
        line = line.rstrip('\n')
        items = line.split(',')
        process_list.append(process(int(items[0]),int(items[1]),int(items[2]),int(items[3])))
    return process_list

s = scheduler(readFileIO("merda.txt"))
s.do_job()
