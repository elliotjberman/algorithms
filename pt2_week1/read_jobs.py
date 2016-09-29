def read_jobs(file):
	jobs = []
	with open(file) as f:
		for line in f:
			split_line = line.split()
			first_character = float(split_line[0])
			if len(split_line) > 1:
				second_character = float(split_line[1])
				jobs.append((first_character, second_character))
	return jobs
