default:
	docker-compose up --build

enter:
	docker-compose exec web bash

test:
	docker-compose exec web bash -c "python manage.py test"

down:
	docker-compose down