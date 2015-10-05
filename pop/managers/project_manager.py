import os
import shutil
from click import ClickException
from pop.exceptions.project_inexistant import ProjectInexistant

class ProjectManager(object):

	def __init__(self,ctx):
		self.ctx = ctx

	def create_project(self,name):
		if self.project_exists(name):
			raise ClickException('Project already exists')
		self.create_project_dir(name)
	
	def switch_project(self,project_name):
		if self.project_exists(project_name):
			with open(os.path.join(self.ctx.pop_home,'context.txt'),'w+') as f:
				f.write(project_name)
		else:
			raise ProjectInexistant()

	def get_projects(self):
		projects = []
		for top, dirs, files in os.walk(self.ctx.pop_home):
			for dir in dirs:
				projects.append({'name':dir})
		return projects

	def load_project(self):
		try:
			with open(os.path.join(self.ctx.pop_home,'context.txt'),'r') as f:
				project_name = f.read()

				if len(project_name) == 0:
					self.reset_project()
				else:
					self.ctx.project_name = project_name
					self.ctx.project_dir = self.ctx.project_home + '/' + project_name
					self.ctx.pop_dir = self.ctx.pop_home + '/' + project_name
					self.ctx.is_project_set = True
		except IOError as e:
			self.reset_project()

	def remove_project(self,project_name):
		if self.project_exists(project_name):
			self.remove_folder(os.path.join(self.ctx.pop_home,project_name))
			self.remove_folder(os.path.join(self.ctx.project_home,project_name))
			self.reset_project()
		else:
			raise ProjectInexistant()

	def remove_folder(self,folder):
		shutil.rmtree(folder)

	def remove_project_dir(self,folder):
		shutil.rmtree(folder)

	def create_project_dir(self,name):
		try:
			os.makedirs(os.path.join(self.ctx.pop_home,name))
			os.makedirs(os.path.join(self.ctx.project_home,name))
			project_structure=['data','conf','export']

			for leave in project_structure:
				os.makedirs(os.path.join(self.ctx.project_home,name,leave))

			with open(os.path.join(self.ctx.pop_home,'context.txt'),'w+') as f:
				f.write(name)

			self.load_project()
		except:
			raise

	def reset_project(self):
		self.ctx.project_name = None
		self.ctx.project_dir = None
		self.ctx.pop_dir = None

		try:
			with open(os.path.join(self.ctx.pop_home,'context.txt'),'w+') as f:
				f.write('')
		except:
			pass

		self.ctx.is_project_set = False

	def project_exists(self,name):
		return os.path.exists(os.path.join(self.ctx.pop_home,name)) and os.path.exists(os.path.join(self.ctx.project_home,name))