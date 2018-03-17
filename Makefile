setup_example:
	cp -r ./wagtailaltgenerator ./example
	cp example/web.example.env example/web.env
	cd example && docker-compose up
