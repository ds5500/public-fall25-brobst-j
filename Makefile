setup:
	@echo "Installing dependencies" 
	pip install -r ./create_db/requirements.txt

	@echo "Running Records Merge"
	./create_db/merge_records.py