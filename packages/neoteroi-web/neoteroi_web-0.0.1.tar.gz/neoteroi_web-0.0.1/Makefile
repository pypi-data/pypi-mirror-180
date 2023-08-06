test-cov:
	pytest --cov-report html --cov=foo tests


build:
	python -m build


uploadtest:
	twine upload --repository testpypi dist/*


release:
	twine upload --repository pypi dist/*
