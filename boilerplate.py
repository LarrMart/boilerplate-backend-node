#!/usr/bin/env python

import os, os.path, json

def prompt_user():
    print("Ingrese el nombre del proyecto: ", end = " ")
    project_name = input()
    print("Ingrese su nombre: ", end = " ")
    project_author = input()
    return project_name, project_author 

def package_content(name, author):
    file_description = {
        "name": "",
        "version": "1.0.0",
        "description": "",
        "main": "server.js",
        "scripts": {
            "start": "node ./src/server.js",
            "test": "echo \"Error: no test specified\" && exit 1"
         },
        "repository": {
        
        },
        "keywords": [],
        "author": "",
        "license": "MIT",
    }
    
    file_description["name"] = name
    file_description["author"] = author
    
    return json.dumps(file_description, indent = 4)

def editor_config_content(): 
	return """
root = true 

[*]
end_of_line = lf
insert_final_newline = true
indent_style = tab  
indent_size = 4
"""

def gitignore_content():
	return """node_modules
.env
"""

def license_content(author):
    return """MIT License

Copyright (c) 2023 {}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 """.format(author)

def create_file(name, content, path="./"):
	if not os.path.exists(path):
		os.makedirs(path)

	with open(os.path.join(path, name), "w") as file:
			file.write(content)
            
def normalize_project_name(project_name):
    words = project_name.strip().lower().split()    
    return "-".join(words);

project_name, author = prompt_user()
project_root_path = normalize_project_name(project_name)

create_file("LICENSE", license_content(author), project_root_path)
create_file(".editorconfig", editor_config_content(), project_root_path)
create_file(".gitignore", gitignore_content(), project_root_path)
create_file("package.json", package_content(project_name, author), project_root_path)
create_file(".env", "", project_root_path)
create_file("README.md", "", project_root_path)
create_file("server.js", "", project_root_path + "/src")
create_file("database.js", "", project_root_path + "/src/database")
create_file("routes.js", "", project_root_path + "/src/routes")
create_file("controllers.js", "", project_root_path + "/src/controllers")
create_file("models.js", "", project_root_path + "/src/models")



