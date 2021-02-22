
__module__     = 'docker_registry_list.py'
__maintainer__ = 'rob.mitchell@objectstream.com'
__version__    = '0.2.0'
__status__     = 'tested against registry:2.7  https://hub.docker.com/_/registry'


import requests

class DockerRegistryList:
	'''
	Class that retrieves the container image names and tags from a Docker registry. 

	Args:
	  registry_url (str):  Docker Registry URL.  http://<host>:<port>
	'''
	def __init__(self,registry_url):
		self.url = registry_url
		self.repos = self._repo_list()


	def _repo_list(self):
		'''
		Private method that retrieves container image names and tags.

		Returns:
		  repos (dict):  dictionary of container names and tags.
		'''
		repos = []
		repos_response = requests.get(self.url+'/v2/_catalog')
		for repo in repos_response.json()['repositories']:
			tag_response = requests.get(self.url+'/v2/'+repo+'/tags/list')
			repos.append(tag_response.json())
		return repos


	def list(self):
		'''
		Returns:
		  self.repos (dict):  dictionary of container names and tags.
		'''
		return self.repos


	def print_list(self):
		'''
		Prints the list of container names and tags.

		Format:
		  container name
		    tag
		'''
		for repo in self.repos:
			print repo['name']
			for tag in repo['tags']:
				print '  ' + tag


if __name__ == '__main__':
	try:
		import sys
		DockerRegistryList(sys.argv[1]).print_list()
	except IndexError:
		pass


