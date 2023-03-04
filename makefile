.PHONY: clean watch

output.css: input.css
	npx tailwindcss -i $< -o $@ --minify

watch:
	npx tailwindcss -i input.css -o output.css --minify --watch

clean:
	rm output.css
