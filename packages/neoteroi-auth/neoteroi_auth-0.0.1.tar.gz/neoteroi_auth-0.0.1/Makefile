test-cov:
	pytest --cov-report html --cov=foo tests


uploadtest:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


release:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
