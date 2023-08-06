import os
import click
from repoutil.gitignores import get_gitignore
from repoutil.licenses import get_license
from repoutil.workflows import get_workflow

@click.version_option(version='0.1.0', prog_name='repoutil')
@click.group("repo")
def main():
	"""
	repo is a simple command line utility to write gitignores, licenses and workflows to a repo.
	"""
	pass

@main.command("g")
@click.argument("language", required = True)
def gitignore(language: str):
	"""
	Generates a gitignore file for the given language.
	"""
	with open("./.gitignore", 'w') as f:
		content = get_gitignore(language)
		if content == "": 
			print("No gitignore found for language: " + language)
			exit(1)
		f.write(content)

	print(f"gitignore file for {language} created.")

@main.command("l")
@click.argument("license", required = True)
def license(license: str):
	"""
	Generates a license file for the given license.
	"""
	with open("./LICENSE.txt", 'w') as f:
		content = get_license(license)
		if content == "": 
			print("No license found: " + license)
			exit(1)
		f.write(content)

	print(f"license file for {license} created.")

@main.command("w")
@click.argument("language", required = True)
def workflow(language: str):
	"""
	Generates a workflow file for the given language.
	"""
	if not os.path.exists("./.github"):
		os.mkdir("./.github")
	if not os.path.exists("./.github/workflows"):
		os.mkdir("./.github/workflows")
	with open("./.github/workflows/integrate.yml", 'w') as f:
		content = get_workflow(language)
		if content == "": 
			print("No gitignore found for language: " + language)
			exit(1)
		f.write(content)

	print(f"workflow file for {language} created.")