from read_jobs import read_jobs

jobs = read_jobs('jobs.txt')

def job_scheduler(job_list, ratio=False):
	if ratio:
		def compare(job):
			return job[0]/job[1]
	else:
		def compare(job):
			return job[0]-job[1]
	jobs.sort(key=lambda x: (compare(x), x[0]), reverse=True)

	big_sum = 0
	completion_time = 0
	counter = 1
	for item in jobs:
		weight = item[0]
		time = item[1]
		completion_time += time
		big_sum += completion_time*weight
		counter +=1
	return big_sum

print('Difference: ' + str(job_scheduler(jobs)))
print('Ratio: ' + str(job_scheduler(jobs, True)))
