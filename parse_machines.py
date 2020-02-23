__author__ = "jphaws"
__version__ = "0.0.1"
import json

def main():
	North = ['484', '490', '498', '510', '865-L', '865-U', '869-L', '869-U']
	north_machines = []
	south_machines = []
	with open('machines.json') as file:
		data = json.load(file)
		for machine in data:
			if machine['number'] in North:
				if machine['type'] == 'Washer':
					north_machines.insert(0, machine)
				else:
					north_machines.append(machine)
			else:
				
				if machine['type'] == 'Washer':
					south_machines.insert(0, machine)
				else:
					south_machines.append(machine)
		print('\n\tNorth Side Laundry Room \n')
		print_stats(north_machines)
		print('\n\n\tSouth Side Laundry Room \n')
		print_stats(south_machines)
		print('\n')

def print_stats(dict):
	
	for machine in dict:
		out = ( machine['type'] + ' #' + machine['number'] + ' is ' + machine['status'].lower())
		if(machine['status'] == 'In use'):
			out += (': ' + machine['time'])
		out += '.'
		print(out)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
