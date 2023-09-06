

init:
	cat required_dirs.txt | xargs mkdir -p


web-up:
	docker compose up -d


web-down:
	docker compose down


listen-up:
	python sglisten.py --configfile config/sglisten.yaml


listen-regen:
	routegen -e config/sglisten.yaml > sglisten.py






