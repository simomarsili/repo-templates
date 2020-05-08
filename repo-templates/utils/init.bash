git init
pip install -r requirements.txt
pre-commit install
pre-commit autoupdate

# commit configuration files
for file in *
do
    if [ -f "$file" ]; then
	git add "$file"
    fi
done

git commit -m "first commit"
