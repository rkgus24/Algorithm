class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def fcfs_scheduling(processes):
    completion_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    waiting_times = [0] * len(processes)

    for i in range(len(processes)):
        if i > 0:
            completion_times[i] = completion_times[i-1] + processes[i].burst_time
        else:
            completion_times[i] = processes[i].burst_time

        turnaround_times[i] = completion_times[i] - processes[i].arrival_time
        waiting_times[i] = turnaround_times[i] - processes[i].burst_time

    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(len(processes)):
        print(f"{processes[i].pid}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

processes = [
    Process("P1", 0, 10),
    Process("P2", 3, 1),
    Process("P3", 4, 4),
    Process("P4", 7, 2),
    Process("P5", 9, 7)
]

fcfs_scheduling(processes)
