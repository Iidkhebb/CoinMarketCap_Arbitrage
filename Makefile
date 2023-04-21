PROJECT_NAME=CMC

.PHONY: build up redo upd fclean down restart logs

all: build up
	@echo "Build complete and up"

build:
	@mkdir -p vl/react vl/django vl/mongodb
	sudo docker-compose build
	@echo "Build complete"

redo:
	sudo docker-compose up  --build
up:
	sudo docker-compose up

upd:
	sudo docker-compose up -d

down:
	sudo docker-compose down

restart:
	sudo docker-compose restart

fclean:
	sudo docker-compose stop $(docker ps -a -q)
	sudo docker-compose rm $(docker ps -a -q)
	sudo docker system prune -f
	sudo rm -rf vl/mongodb/*
	sudo rm -rf vl/django/*
	sudo rm -rf vl/react/*
	sudo rm -rf vl
	sudo docker volume rm mongodb django react


logs:
	sudo docker-compose logs -f

